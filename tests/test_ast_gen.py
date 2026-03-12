"""
AST Generation test cases for TyC compiler.
TODO: Implement 100 test cases for AST generation
"""

import pytest
from tests.utils import ASTGenerator

#DECLARATION TESTS
def test_ast_gen_001_struct_decl():
    source = """
    struct Point {
        int x;
        int y;
    };
    """
    expected = "Program([StructDecl(Point, [MemberDecl(IntType(), x), MemberDecl(IntType(), y)])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_002_empty_function():
    source = """
    void main() {
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_003_func_with_expressions():
    source = """
    int add(int x, int y) {
        return x + y;
    }
    """
    expected = "Program([FuncDecl(IntType(), add, [Param(IntType(), x), Param(IntType(), y)], BlockStmt([ReturnStmt(return BinaryOp(Identifier(x), +, Identifier(y)))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_004_string_and_float_var():
    source = """
    void main() {
        string s = "hello";
        float f = 3.14;
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(StringType(), s, StringLiteral(hello)), VarDecl(FloatType(), f, FloatLiteral(3.14))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_005_inferred_return_type():
    source = """
    add(int x) {
        return x;
    }
    """
    expected = "Program([FuncDecl(auto, add, [Param(IntType(), x)], BlockStmt([ReturnStmt(return Identifier(x))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_006_var_decl_without_init():
    source = """
    void main() {
        int x;
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(IntType(), x, None)]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_007_struct_var_decl():
    source = """
    struct Point { int x; };
    void main() {
        Point p;
    }
    """
    expected = "Program([StructDecl(Point, [MemberDecl(IntType(), x)]), FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(StructType(Point), p, None)]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_008_multiple_parameters():
    source = """
    void process(int a, float b, string c) {
    }
    """
    expected = "Program([FuncDecl(VoidType(), process, [Param(IntType(), a), Param(FloatType(), b), Param(StringType(), c)], BlockStmt([]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_009_func_with_no_params():
    source = """
    void greet() {
        print("Hello, World!");
    }
    """
    expected = "Program([FuncDecl(VoidType(), greet, [], BlockStmt([FuncCall(Identifier(print), [StringLiteral(Hello, World!)])]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_010_sequential_structs():
    source = """
    struct A { int x; };
    struct B { float y; };
    """
    expected = "Program([StructDecl(A, [MemberDecl(IntType(), x)]), StructDecl(B, [MemberDecl(FloatType(), y)])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_011_struct_member_is_struct():
    source = """
    struct Color { int r; };
    struct Point { Color c; };
    """
    expected = "Program([StructDecl(Color, [MemberDecl(IntType(), r)]), StructDecl(Point, [MemberDecl(StructType(Color), c)])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_012_func_with_struct_return():
    source = """
    struct Point {
        int x;
        int y;
    };
    Point createPoint(int x, int y) {
        Point p;
        p.x = x;
        p.y = y;
        return p;
    }
    """
    expected = "Program([StructDecl(Point, [MemberDecl(IntType(), x), MemberDecl(IntType(), y)]), FuncDecl(StructType(Point), createPoint, [Param(IntType(), x), Param(IntType(), y)], BlockStmt([VarDecl(StructType(Point), p, None), AssignExpr(MemberAccess(Identifier(p), x), Identifier(x)), AssignExpr(MemberAccess(Identifier(p), y), Identifier(y)), ReturnStmt(return Identifier(p))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_013_function_returning_struct():
    source = """
    struct Point { int x; };
    Point getPoint() {
        Point p;
        return p;
    }
    """
    expected = "Program([StructDecl(Point, [MemberDecl(IntType(), x)]), FuncDecl(StructType(Point), getPoint, [], BlockStmt([VarDecl(StructType(Point), p, None), ReturnStmt(return Identifier(p))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_014_struct_with_various_members():
    source = """
    struct Data {
        int i;
        float f;
        string s;
    };
    """
    expected = "Program([StructDecl(Data, [MemberDecl(IntType(), i), MemberDecl(FloatType(), f), MemberDecl(StringType(), s)])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_015_auto_var_complex_math():
    source = """
    void main() {
        auto x = 5 + 3 * 2;
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(auto, x, BinaryOp(IntLiteral(5), +, BinaryOp(IntLiteral(3), *, IntLiteral(2))))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_016_auto_var_parentheses():
    source = """
    void main() {
        auto x = (5 + 3) * 2;
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(auto, x, BinaryOp(BinaryOp(IntLiteral(5), +, IntLiteral(3)), *, IntLiteral(2)))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_017_auto_var_member_access():
    source = """
    struct Point { int x; };
    void main() {
        Point p;
        auto val = p.x;
    }
    """
    expected = "Program([StructDecl(Point, [MemberDecl(IntType(), x)]), FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(StructType(Point), p, None), VarDecl(auto, val, MemberAccess(Identifier(p), x))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_018_struct_with_nested_struct():
    source = """
    struct Point {
        int x;
        int y;
        struct Color {
            int r;
            int g;
            int b;
        };
    };
    """
    expected = "Program([StructDecl(Point, [MemberDecl(IntType(), x), MemberDecl(IntType(), y), MemberDecl(StructType(Color), Color, [MemberDecl(IntType(), r), MemberDecl(IntType(), g), MemberDecl(IntType(), b)])])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_019_sequential_functions():
    source = """
    int foo() { return 1; }
    int bar() { return foo(); }
    """
    expected = "Program([FuncDecl(IntType(), foo, [], BlockStmt([ReturnStmt(return IntLiteral(1))])), FuncDecl(IntType(), bar, [], BlockStmt([ReturnStmt(return FuncCall(Identifier(foo), []))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_020_struct_with_func_and_nested_struct():
    source = """
    struct Point {
        int x;
        int y;
        struct Color {
            int r;
            int g;
            int b;
            void printColor() {
                print(r, g, b);
            }
        };
        void move(int dx, int dy) {
            x = x + dx;
            y = y + dy;
        }
    };
    """
    expected = "Program([StructDecl(Point, [MemberDecl(IntType(), x), MemberDecl(IntType(), y), MemberDecl(StructType(Color), Color, [MemberDecl(IntType(), r), MemberDecl(IntType(), g), MemberDecl(IntType(), b), MemberDecl(VoidType(), printColor, [], BlockStmt([FuncCall(Identifier(print), [Identifier(r), Identifier(g), Identifier(b)])]))]), MemberDecl(VoidType(), move, [Param(IntType(), dx), Param(IntType(), dy)], BlockStmt([AssignExpr(Identifier(x), BinaryOp(Identifier(x), +, Identifier(dx))), AssignExpr(Identifier(y), BinaryOp(Identifier(y), +, Identifier(dy)))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

#021 - 050: Chỉ test Biểu thức (Cộng trừ nhân chia, logic, truy cập member, gọi hàm...).
def test_ast_gen_021_binary_expression():
    source = """
    void main() {
        int result = (5 + 3) * 2;
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(IntType(), result, BinaryOp(BinaryOp(IntLiteral(5), +, IntLiteral(3)), *, IntLiteral(2)))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_022_logical_expression():
    source = """
    void main() {
        bool flag = (true && false) || !false;
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(BoolType(), flag, BinaryOp(BinaryOp(BoolLiteral(true), &&, BoolLiteral(false)), ||, UnaryOp(!, BoolLiteral(false)))))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_023_member_access():
    source = """
    struct Point { int x; };
    void main() {
        Point p;
        int val = p.x;
    }
    """
    expected = "Program([StructDecl(Point, [MemberDecl(IntType(), x)]), FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(StructType(Point), p, None), VarDecl(IntType(), val, MemberAccess(Identifier(p), x))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_024_function_call():
    source = """
    void greet(string name) {
        print("Hello, " + name);
    }
    void main() {
        greet("Alice");
    }
    """
    expected = "Program([FuncDecl(VoidType(), greet, [Param(StringType(), name)], BlockStmt([FuncCall(Identifier(print), [BinaryOp(StringLiteral(Hello, ), +, Identifier(name))])])), FuncDecl(VoidType(), main, [], BlockStmt([FuncCall(Identifier(greet), [StringLiteral(Alice)])]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_025_nested_function_calls():
    source = """
    int add(int x, int y) {
        return x + y;
    }
    void main() {
        int result = add(add(1, 2), 3);
    }
    """
    expected = "Program([FuncDecl(IntType(), add, [Param(IntType(), x), Param(IntType(), y)], BlockStmt([ReturnStmt(return BinaryOp(Identifier(x), +, Identifier(y)))])), FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(IntType(), result, FuncCall(Identifier(add), [FuncCall(Identifier(add), [IntLiteral(1), IntLiteral(2)]), IntLiteral(3)])))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_026_complex_expression():
    source = """
    void main() {
        auto x = (5 + 3) * (2 - 1) / 4;
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(auto, x, BinaryOp(BinaryOp(BinaryOp(IntLiteral(5), +, IntLiteral(3)), *, BinaryOp(IntLiteral(2), -, IntLiteral(1))), /, IntLiteral(4)))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_027_unary_expression():
    source = """
    void main() {
        int x = -5;
        bool flag = !true;
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(IntType(), x, UnaryOp(-, IntLiteral(5))), VarDecl(BoolType(), flag, UnaryOp(!, BoolLiteral(true)))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_028_mixed_expression():
    source = """
    void main() {
        auto result = (5 + 3) * 2 > 10 && !false;
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(auto, result, BinaryOp(BinaryOp(BinaryOp(IntLiteral(5), +, IntLiteral(3)), *, IntLiteral(2)), >, IntLiteral(10)), &&, UnaryOp(!, BoolLiteral(false)))))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_029_member_access_with_function_call():
    source = """
    struct Point { int x; };
    void main() {
        Point p;
        int val = p.x + 5;
    }
    """
    expected = "Program([StructDecl(Point, [MemberDecl(IntType(), x)]), FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(StructType(Point), p, None), VarDecl(IntType(), val, BinaryOp(MemberAccess(Identifier(p), x), +, IntLiteral(5)))]))])"
    assert str(ASTGenerator(source).generate()) == expected



#051 - 080: Chỉ test Câu lệnh (If, For, While, Switch...).

#081 - 100: Test các chương trình tổng hợp, lồng nhau phức tạp.