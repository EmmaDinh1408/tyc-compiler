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
    expected = "Program([FuncDecl(VoidType(), main, [], [])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_003_func_with_expressions():
    source = """
    int add(int x, int y) {
        return x + y;
    }
    """
    expected = "Program([FuncDecl(IntType(), add, [Param(IntType(), x), Param(IntType(), y)], [ReturnStmt(return BinaryOp(Identifier(x), +, Identifier(y)))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_004_string_and_float_var():
    source = """
    void main() {
        string s = "hello";
        float f = 3.14;
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], [VarDecl(StringType(), s, StringLiteral(hello)), VarDecl(FloatType(), f, FloatLiteral(3.14))])])"
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

#EXPRESSION TESTS
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

def test_ast_gen_030_function_call_with_expression():
    source = """
    void printSum(int a, int b) {
        print(a + b);
    }
    void main() {
        printSum(5, 3 * 2);
    }
    """
    expected = "Program([FuncDecl(VoidType(), printSum, [Param(IntType(), a), Param(IntType(), b)], BlockStmt([FuncCall(Identifier(print), [BinaryOp(Identifier(a), +, Identifier(b))])])), FuncDecl(VoidType(), main, [], BlockStmt([FuncCall(Identifier(printSum), [IntLiteral(5), BinaryOp(IntLiteral(3), *, IntLiteral(2))])]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_031_if_statement():
    source = """
    void main() {
        int x = 5;
        if (x > 0) {
            print("Positive");
        } else {
            print("Non-positive");
        }
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(IntType(), x, IntLiteral(5)), IfStmt(if BinaryOp(Identifier(x), >, IntLiteral(0)) then BlockStmt([FuncCall(Identifier(print), [StringLiteral('Positive')])]), else BlockStmt([FuncCall(Identifier(print), [StringLiteral('Non-positive')])]))]))])" 
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_032_for_loop():
    source = """
    void main() {
        for (int i = 0; i < 10; i = i + 1) {
            print(i);
        }
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ForStmt(VarDecl(IntType(), i, IntLiteral(0)), BinaryOp(Identifier(i), <, IntLiteral(10)), AssignExpr(Identifier(i), BinaryOp(Identifier(i), +, IntLiteral(1))), BlockStmt([FuncCall(Identifier(print), [Identifier(i)])]))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_033_while_loop():
    source = """
    void main() {
        int i = 0;
        while (i < 10) {
            print(i);
            i = i + 1;
        }
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(IntType(), i, IntLiteral(0)), WhileStmt(BinaryOp(Identifier(i), <, IntLiteral(10)), BlockStmt([FuncCall(Identifier(print), [Identifier(i)]), AssignExpr(Identifier(i), BinaryOp(Identifier(i), +, IntLiteral(1)))]))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_034_switch_statement():
    source = """
    void main() {
        int x = 2;
        switch (x) {
            case 1:
                print("One");
                break;
            case 2:
                print("Two");
                break;
            default:
                print("Other");
        }       
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(IntType(), x, IntLiteral(2)), SwitchStmt(Identifier(x), [Case(IntLiteral(1), BlockStmt([FuncCall(Identifier(print), [StringLiteral(One)]), BreakStmt()])), Case(IntLiteral(2), BlockStmt([FuncCall(Identifier(print), [StringLiteral(Two)]), BreakStmt()])), DefaultCase(BlockStmt([FuncCall(Identifier(print), [StringLiteral(Other)])]))])]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_035_nested_control_structures():
    source = """
    void main() {
        for (int i = 0; i < 5; i = i + 1) {
            if (i % 2 == 0) {
                print(i);
            } else {
                print("Odd");
            }
        }
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ForStmt(VarDecl(IntType(), i, IntLiteral(0)), BinaryOp(Identifier(i), <, IntLiteral(5)), AssignExpr(Identifier(i), BinaryOp(Identifier(i), +, IntLiteral(1))), BlockStmt([IfStmt(BinaryOp(BinaryOp(Identifier(i), %, IntLiteral(2)), ==, IntLiteral(0)), BlockStmt([FuncCall(Identifier(print), [Identifier(i)])]), BlockStmt([FuncCall(Identifier(print), [StringLiteral(Odd)])]))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_036_if_with_logical_conditions():
    source = """
    void main() {
        int x = 5;
        if (x > 0 && x < 10) {
            print("In range");
        } else {
            print("Out of range");
        }
    }
    """ 
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(IntType(), x, IntLiteral(5)), IfStmt(BinaryOp(BinaryOp(Identifier(x), >, IntLiteral(0)), &&, BinaryOp(Identifier(x), <, IntLiteral(10))), BlockStmt([FuncCall(Identifier(print), [StringLiteral(In range)])]), BlockStmt([FuncCall(Identifier(print), [StringLiteral(Out of range)])]))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_037_for_loop_with_break():
    source = """
    void main() {
        for (int i = 0; i < 10; i = i + 1) {
            if (i == 5) {
                break;
            }
            print(i);
        }
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ForStmt(VarDecl(IntType(), i, IntLiteral(0)), BinaryOp(Identifier(i), <, IntLiteral(10)), AssignExpr(Identifier(i), BinaryOp(Identifier(i), +, IntLiteral(1))), BlockStmt([IfStmt(BinaryOp(Identifier(i), ==, IntLiteral(5)), BlockStmt([BreakStmt()]), BlockStmt([])), FuncCall(Identifier(print), [Identifier(i)]))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_038_while_loop_with_continue():
    source = """
    void main() {
        int i = 0;
        while (i < 10) {
            i = i + 1;
            if (i % 2 == 0) {
                continue;
            }
            print(i);
        }
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(IntType(), i, IntLiteral(0)), WhileStmt(BinaryOp(Identifier(i), <, IntLiteral(10)), BlockStmt([AssignExpr(Identifier(i), BinaryOp(Identifier(i), +, IntLiteral(1))), IfStmt(BinaryOp(BinaryOp(Identifier(i), %, IntLiteral(2)), ==, IntLiteral(0)), BlockStmt([ContinueStmt()]), BlockStmt([])), FuncCall(Identifier(print), [Identifier(i)]))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_039_switch_with_fallthrough():
    source = """
    void main() {
        int x = 1;
        switch (x) {
            case 1:
                print("One");
            case 2:
                print("Two");
                break;
            default:
                print("Other");
        }
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(IntType(), x, IntLiteral(1)), SwitchStmt(Identifier(x), [Case(IntLiteral(1), BlockStmt([FuncCall(Identifier(print), [StringLiteral(One)])])), Case(IntLiteral(2), BlockStmt([FuncCall(Identifier(print), [StringLiteral(Two)]), BreakStmt()])), DefaultCase(BlockStmt([FuncCall(Identifier(print), [StringLiteral(Other)])]))])]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_040_nested_switch():
    source = """
    void main() {
        int x = 1;
        switch (x) {
            case 1:
                int y = 2;
                switch (y) {
                    case 2:
                        print("Nested Two");
                        break;
                    default:
                        print("Nested Other");
                }
                break;
            default:
                print("Other"); 
        }
    }   
    """
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(IntType(), x, IntLiteral(1)), SwitchStmt(Identifier(x), [Case(IntLiteral(1), BlockStmt([VarDecl(IntType(), y, IntLiteral(2)), SwitchStmt(Identifier(y), [Case(IntLiteral(2), BlockStmt([FuncCall(Identifier(print), [StringLiteral(Nested Two)]), BreakStmt()]), DefaultCase(BlockStmt([FuncCall(Identifier(print), [StringLiteral(Nested Other)])]))])])), DefaultCase(BlockStmt([FuncCall(Identifier(print), [StringLiteral(Other)])]))])]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_041_if_with_nested_for():
    source = """
    void main() {
        int x = 5;
        if (x > 0) {
            for (int i = 0; i < x; i = i + 1) {
                print(i);
            }     
        } else {
            print("Non-positive");
        }
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(IntType(), x, IntLiteral(5)), IfStmt(BinaryOp(Identifier(x), >, IntLiteral(0)), BlockStmt([ForStmt(VarDecl(IntType(), i, IntLiteral(0)), BinaryOp(Identifier(i), <, Identifier(x)), AssignExpr(Identifier(i), BinaryOp(Identifier(i), +, IntLiteral(1))), BlockStmt([FuncCall(Identifier(print), [Identifier(i)])]))]), BlockStmt([FuncCall(Identifier(print), [StringLiteral(Non-positive)])]))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_042_for_with_nested_if():
    source = """
    void main() {
        for (int i = 0; i < 5; i = i + 1) {
            if (i % 2 == 0) {
                print(i);
            } else {
                print("Odd");
            }
        }
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ForStmt(VarDecl(IntType(), i, IntLiteral(0)), BinaryOp(Identifier(i), <, IntLiteral(5)), AssignExpr(Identifier(i), BinaryOp(Identifier(i), +, IntLiteral(1))), BlockStmt([IfStmt(BinaryOp(BinaryOp(Identifier(i), %, IntLiteral(2)), ==, IntLiteral(0)), BlockStmt([FuncCall(Identifier(print), [Identifier(i)])]), BlockStmt([FuncCall(Identifier(print), [StringLiteral(Odd)])]))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_043_while_with_nested_switch():
    source = """
    void main() {
        int i = 0;
        while (i < 3) {
            switch (i) {
                case 0:
                    print("Zero");
                    break;
                case 1:
                    print("One");
                    break;
                default:
                    print("Other");
            }   
            i = i + 1;
        }           
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(IntType(), i, IntLiteral(0)), WhileStmt(BinaryOp(Identifier(i), <, IntLiteral(3)), BlockStmt([SwitchStmt(Identifier(i), [Case(IntLiteral(0), BlockStmt([FuncCall(Identifier(print), [StringLiteral(Zero)]), BreakStmt()]), Case(IntLiteral(1), BlockStmt([FuncCall(Identifier(print), [StringLiteral(One)]), BreakStmt()]), DefaultCase(BlockStmt([FuncCall(Identifier(print), [StringLiteral(Other)])]))]), AssignExpr(Identifier(i), BinaryOp(Identifier(i), +, IntLiteral(1)))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_044_switch_with_nested_if():
    source = """
    void main() {
        int x = 1;
        switch (x) {
            case 1:
                if (x > 0) {
                    print("Positive One");
                } else {
                    print("Non-positive One");
                }
                break;
            default:
                print("Other");     
        }
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(IntType(), x, IntLiteral(1)), SwitchStmt(Identifier(x), [Case(IntLiteral(1), BlockStmt([IfStmt(BinaryOp(Identifier(x), >, IntLiteral(0)), BlockStmt([FuncCall(Identifier(print), [StringLiteral(Positive One)])]), BlockStmt([FuncCall(Identifier(print), [StringLiteral(Non-positive One)])]))]), DefaultCase(BlockStmt([FuncCall(Identifier(print), [StringLiteral(Other)])]))])]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_045_chained_assignment():
    source = """
    void main() {
        int a; int b; int c;
        a = b = c = 10;
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(IntType(), a, None), VarDecl(IntType(), b, None), VarDecl(IntType(), c, None), AssignExpr(Identifier(a), AssignExpr(Identifier(b), AssignExpr(Identifier(c), IntLiteral(10))))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_046_postfix_increment():
    source = """
    void main() {
        int i = 0;
        i++;
        i--;
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(IntType(), i, IntLiteral(0)), PostfixOp(Identifier(i), ++), PostfixOp(Identifier(i), --)]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_047_prefix_unary_operations():
    source = """
    void main() {
        int x = 5;
        int y = - ++x;
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(IntType(), x, IntLiteral(5)), VarDecl(IntType(), y, PrefixOp(-, PrefixOp(++, Identifier(x))))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_048_complex_logical_no_bool():
    source = """
    void main() {
        auto result = (5 > 3) && !(10 == 10) || (1 < 0);
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(auto, result, BinaryOp(BinaryOp(BinaryOp(IntLiteral(5), >, IntLiteral(3)), &&, PrefixOp(!, BinaryOp(IntLiteral(10), ==, IntLiteral(10)))), ||, BinaryOp(IntLiteral(1), <, IntLiteral(0))))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_049_nested_member_access():
    source = """
    struct Inner { int val; };
    struct Outer { Inner in; };
    void main() {
        Outer out;
        out.in.val = 100;
    }
    """
    expected = "Program([StructDecl(Inner, [MemberDecl(IntType(), val)]), StructDecl(Outer, [MemberDecl(StructType(Inner), in)]), FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(StructType(Outer), out, None), AssignExpr(MemberAccess(MemberAccess(Identifier(out), in), val), IntLiteral(100))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_050_function_call_as_argument():
    source = """
    int mult(int a, int b) { return a * b; }
    void main() {
        int result = mult(mult(2, 3), 4);
    }
    """
    expected = "Program([FuncDecl(IntType(), mult, [Param(IntType(), a), Param(IntType(), b)], BlockStmt([ReturnStmt(return BinaryOp(Identifier(a), *, Identifier(b)))])), FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(IntType(), result, FuncCall(Identifier(mult), [FuncCall(Identifier(mult), [IntLiteral(2), IntLiteral(3)]), IntLiteral(4)]))]))])"
    assert str(ASTGenerator(source).generate()) == expected   

#STATEMENT TESTS
def test_ast_gen_051_if_statement():
    source = """
    void main() {
        int x = 5;
        if (x > 0) {
            print("Positive");
        } else {
            print("Non-positive");
        }
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(IntType(), x, IntLiteral(5)), IfStmt(BinaryOp(Identifier(x), >, IntLiteral(0)), BlockStmt([FuncCall(Identifier(print), [StringLiteral(Positive)])]), BlockStmt([FuncCall(Identifier(print), [StringLiteral(Non-positive)])]))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_052_for_loop():
    source = """
    void main() {
        for (int i = 0; i < 10; i = i + 1) {
            print(i);
        }
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ForStmt(VarDecl(IntType(), i, IntLiteral(0)), BinaryOp(Identifier(i), <, IntLiteral(10)), AssignExpr(Identifier(i), BinaryOp(Identifier(i), +, IntLiteral(1))), BlockStmt([FuncCall(Identifier(print), [Identifier(i)])]))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_053_while_loop():
    source = """
    void main() {
        int i = 0;
        while (i < 10) {
            print(i);
            i = i + 1;
        }
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(IntType(), i, IntLiteral(0)), WhileStmt(BinaryOp(Identifier(i), <, IntLiteral(10)), BlockStmt([FuncCall(Identifier(print), [Identifier(i)]), AssignExpr(Identifier(i), BinaryOp(Identifier(i), +, IntLiteral(1)))]))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_054_switch_statement():
    source = """
    void main() {
        int x = 2;
        switch (x) {
            case 1:
                print("One");
                break;
            case 2:
                print("Two");
                break;
            default:
                print("Other");
        }       
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(IntType(), x, IntLiteral(2)), SwitchStmt(Identifier(x), [Case(IntLiteral(1), BlockStmt([FuncCall(Identifier(print), [StringLiteral(One)]), BreakStmt()])), Case(IntLiteral(2), BlockStmt([FuncCall(Identifier(print), [StringLiteral(Two)]), BreakStmt()])), DefaultCase(BlockStmt([FuncCall(Identifier(print), [StringLiteral(Other)])]))])]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_055_nested_control_structures():
    source = """
    void main() {
        for (int i = 0; i < 5; i = i + 1) {
            if (i % 2 == 0) {
                print(i);
            } else {
                print("Odd");
            }
        }
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ForStmt(VarDecl(IntType(), i, IntLiteral(0)), BinaryOp(Identifier(i), <, IntLiteral(5)), AssignExpr(Identifier(i), BinaryOp(Identifier(i), +, IntLiteral(1))), BlockStmt([IfStmt(BinaryOp(BinaryOp(Identifier(i), %, IntLiteral(2)), ==, IntLiteral(0)), BlockStmt([FuncCall(Identifier(print), [Identifier(i)])]), BlockStmt([FuncCall(Identifier(print), [StringLiteral(Odd)])]))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_056_if_with_logical_conditions():
    source = """
    void main() {
        int x = 5;
        if (x > 0 && x < 10) {
            print("In range");
        } else {
            print("Out of range");
        }
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(IntType(), x, IntLiteral(5)), IfStmt(BinaryOp(BinaryOp(Identifier(x), >, IntLiteral(0)), &&, BinaryOp(Identifier(x), <, IntLiteral(10))), BlockStmt([FuncCall(Identifier(print), [StringLiteral(In range)])]), BlockStmt([FuncCall(Identifier(print), [StringLiteral(Out of range)])]))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_057_for_loop_with_break():
    source = """
    void main() {
        for (int i = 0; i < 10; i = i + 1) {
            if (i == 5) {
                break;
            }
            print(i);
        }
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ForStmt(VarDecl(IntType(), i, IntLiteral(0)), BinaryOp(Identifier(i), <, IntLiteral(10)), AssignExpr(Identifier(i), BinaryOp(Identifier(i), +, IntLiteral(1))), BlockStmt([IfStmt(BinaryOp(Identifier(i), ==, IntLiteral(5)), BlockStmt([BreakStmt()]), BlockStmt([])), FuncCall(Identifier(print), [Identifier(i)]))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_058_while_loop_with_continue():
    source = """
    void main() {
        int i = 0;
        while (i < 10) {
            i = i + 1;
            if (i % 2 == 0) {
                continue;
            }
            print(i);
        }   
    }   
    """ 
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(IntType(), i, IntLiteral(0)), WhileStmt(BinaryOp(Identifier(i), <, IntLiteral(10)), BlockStmt([AssignExpr(Identifier(i), BinaryOp(Identifier(i), +, IntLiteral(1))), IfStmt(BinaryOp(BinaryOp(Identifier(i), %, IntLiteral(2)), ==, IntLiteral(0)), BlockStmt([ContinueStmt()]), BlockStmt([])), FuncCall(Identifier(print), [Identifier(i)]))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_059_switch_with_fallthrough():
    source = """
    void main() {
        int x = 1;
        switch (x) {
            case 1:
                print("One");
            case 2:
                print("Two");
                break;
            default:
                print("Other");
        }
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(IntType(), x, IntLiteral(1)), SwitchStmt(Identifier(x), [Case(IntLiteral(1), BlockStmt([FuncCall(Identifier(print), [StringLiteral(One)])])), Case(IntLiteral(2), BlockStmt([FuncCall(Identifier(print), [StringLiteral(Two)]), BreakStmt()])), DefaultCase(BlockStmt([FuncCall(Identifier(print), [StringLiteral(Other)])]))])]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_060_nested_switch():
    source = """
    void main() {
        int x = 1;
        switch (x) {
            case 1:
                int y = 2;
                switch (y) {
                    case 2:
                        print("Nested Two");
                        break;
                    default:
                        print("Nested Other");
                }
                break;
            default:
                print("Other");
        }
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(IntType(), x, IntLiteral(1)), SwitchStmt(Identifier(x), [Case(IntLiteral(1), BlockStmt([VarDecl(IntType(), y, IntLiteral(2)), SwitchStmt(Identifier(y), [Case(IntLiteral(2), BlockStmt([FuncCall(Identifier(print), [StringLiteral(Nested Two)]), BreakStmt()]), DefaultCase(BlockStmt([FuncCall(Identifier(print), [StringLiteral(Nested Other)])]))])])), DefaultCase(BlockStmt([FuncCall(Identifier(print), [StringLiteral(Other)])]))])]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_061_if_with_nested_for():
    source = """
    void main() {
        int x = 5;
        if (x > 0) {
            for (int i = 0; i < x; i = i + 1) {
                print(i);
            }
        } else {
            print("Non-positive");
        }
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(IntType(), x, IntLiteral(5)), IfStmt(BinaryOp(Identifier(x), >, IntLiteral(0)), BlockStmt([ForStmt(VarDecl(IntType(), i, IntLiteral(0)), BinaryOp(Identifier(i), <, Identifier(x)), AssignExpr(Identifier(i), BinaryOp(Identifier(i), +, IntLiteral(1))), BlockStmt([FuncCall(Identifier(print), [Identifier(i)])]))]), BlockStmt([FuncCall(Identifier(print), [StringLiteral(Non-positive)])]))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_062_for_with_nested_if():
    source = """
    void main() {
        for (int i = 0; i < 5; i = i + 1) {
            if (i % 2 == 0) {
                print(i);
            } else {
                print("Odd");
            }
        }
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ForStmt(VarDecl(IntType(), i, IntLiteral(0)), BinaryOp(Identifier(i), <, IntLiteral(5)), AssignExpr(Identifier(i), BinaryOp(Identifier(i), +, IntLiteral(1))), BlockStmt([IfStmt(BinaryOp(BinaryOp(Identifier(i), %, IntLiteral(2)), ==, IntLiteral(0)), BlockStmt([FuncCall(Identifier(print), [Identifier(i)])]), BlockStmt([FuncCall(Identifier(print), [StringLiteral(Odd)])]))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_063_while_with_nested_switch():
    source = """
    void main() {
        int i = 0;
        while (i < 3) {
            switch (i) {
                case 0:
                    print("Zero");
                    break;
                case 1:
                    print("One");
                    break;
                default:
                    print("Other");
            }
            i = i + 1;
        }
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(IntType(), i, IntLiteral(0)), WhileStmt(BinaryOp(Identifier(i), <, IntLiteral(3)), BlockStmt([SwitchStmt(Identifier(i), [Case(IntLiteral(0), BlockStmt([FuncCall(Identifier(print), [StringLiteral(Zero)]), BreakStmt()]), Case(IntLiteral(1), BlockStmt([FuncCall(Identifier(print), [StringLiteral(One)]), BreakStmt()]), DefaultCase(BlockStmt([FuncCall(Identifier(print), [StringLiteral(Other)])]))]), AssignExpr(Identifier(i), BinaryOp(Identifier(i), +, IntLiteral(1)))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_064_switch_with_nested_if():
    source = """
    void main() {
        int x = 1;
        switch (x) {
            case 1:
                if (x > 0) {
                    print("Positive One");
                } else {
                    print("Non-positive One");
                }
                break;
            default:
                print("Other");
        }
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(IntType(), x, IntLiteral(1)), SwitchStmt(Identifier(x), [Case(IntLiteral(1), BlockStmt([IfStmt(BinaryOp(Identifier(x), >, IntLiteral(0)), BlockStmt([FuncCall(Identifier(print), [StringLiteral(Positive One)])]), BlockStmt([FuncCall(Identifier(print), [StringLiteral(Non-positive One)])]))]), DefaultCase(BlockStmt([FuncCall(Identifier(print), [StringLiteral(Other)])]))])]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_065_chained_assignment():
    source = """
    void main() {
        int a; int b; int c;
        a = b = c = 10;
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(IntType(), a, None), VarDecl(IntType(), b, None), VarDecl(IntType(), c, None), AssignExpr(Identifier(a), AssignExpr(Identifier(b), AssignExpr(Identifier(c), IntLiteral(10))))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_066_postfix_increment():
    source = """
    void main() {
        int i = 0;
        i++;
        i--;
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(IntType(), i, IntLiteral(0)), PostfixOp(Identifier(i), ++), PostfixOp(Identifier(i), --)]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_067_prefix_unary_operations():
    source = """
    void main() {
        int x = 5;
        int y = - ++x;
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(IntType(), x, IntLiteral(5)), VarDecl(IntType(), y, PrefixOp(-, PrefixOp(++, Identifier(x))))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_068_complex_logical_no_bool():
    source = """
    void main() {
        auto result = (5 > 3) && !(10 == 10) || (1 < 0);
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(auto, result, BinaryOp(BinaryOp(BinaryOp(IntLiteral(5), >, IntLiteral(3)), &&, PrefixOp(!, BinaryOp(IntLiteral(10), ==, IntLiteral(10)))), ||, BinaryOp(IntLiteral(1), <, IntLiteral(0))))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_069_nested_member_access():
    source = """
    struct Inner { int val; };
    struct Outer { Inner in; };
    void main() {
        Outer out;
        out.in.val = 100;
    }
    """
    expected = "Program([StructDecl(Inner, [MemberDecl(IntType(), val)]), StructDecl(Outer, [MemberDecl(StructType(Inner), in)]), FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(StructType(Outer), out, None), AssignExpr(MemberAccess(MemberAccess(Identifier(out), in), val), IntLiteral(100))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_070_function_call_as_argument():
    source = """
    int mult(int a, int b) { return a * b; }
    void main() {
        int result = mult(mult(2, 3), 4);
    }
    """
    expected = "Program([FuncDecl(IntType(), mult, [Param(IntType(), a), Param(IntType(), b)], BlockStmt([ReturnStmt(return BinaryOp(Identifier(a), *, Identifier(b)))])), FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(IntType(), result, FuncCall(Identifier(mult), [FuncCall(Identifier(mult), [IntLiteral(2), IntLiteral(3)]), IntLiteral(4)]))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_071_if_without_else():
    source = """
    void main() {
        int x = 5;
        if (x > 0) {
            x = x - 1;
        }
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(IntType(), x, IntLiteral(5)), IfStmt(BinaryOp(Identifier(x), >, IntLiteral(0)), BlockStmt([AssignExpr(Identifier(x), BinaryOp(Identifier(x), -, IntLiteral(1)))]), None)]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_072_if_elseif_else():
    source = """
    void main() {
        int x = 0;
        if (x > 0) {
            x = 1;
        } else if (x < 0) {
            x = -1;
        } else {
            x = 0;
        }
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(IntType(), x, IntLiteral(0)), IfStmt(BinaryOp(Identifier(x), >, IntLiteral(0)), BlockStmt([AssignExpr(Identifier(x), IntLiteral(1))]), IfStmt(BinaryOp(Identifier(x), <, IntLiteral(0)), BlockStmt([AssignExpr(Identifier(x), UnaryOp(-, IntLiteral(1)))]), BlockStmt([AssignExpr(Identifier(x), IntLiteral(0))]))) ]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_073_return_void():
    source = """
    void doNothing() {
        return;
    }
    """
    expected = "Program([FuncDecl(VoidType(), doNothing, [], BlockStmt([ReturnStmt(None)]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_074_nested_for_loops():
    source = """
    void main() {
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                print(i, j);
            }
        }
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ForStmt(VarDecl(IntType(), i, IntLiteral(0)), BinaryOp(Identifier(i), <, IntLiteral(3)), PostfixOp(Identifier(i), ++), BlockStmt([ForStmt(VarDecl(IntType(), j, IntLiteral(0)), BinaryOp(Identifier(j), <, IntLiteral(3)), PostfixOp(Identifier(j), ++), BlockStmt([FuncCall(Identifier(print), [Identifier(i), Identifier(j)])]))]))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_075_empty_blocks():
    source = """
    void main() {
        while (1 < 0) {}
        if (1 == 1) {} else {}
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([WhileStmt(BinaryOp(IntLiteral(1), <, IntLiteral(0)), BlockStmt([])), IfStmt(BinaryOp(IntLiteral(1), ==, IntLiteral(1)), BlockStmt([]), BlockStmt([]))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_076_expression_as_statement():
    source = """
    void main() {
        5 + 3;
        foo();
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([BinaryOp(IntLiteral(5), +, IntLiteral(3)), FuncCall(Identifier(foo), [])]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_077_standalone_blocks():
    source = """
    void main() {
        {
            int x = 5;
        }
        {
            int y = 10;
        }
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([BlockStmt([VarDecl(IntType(), x, IntLiteral(5))]), BlockStmt([VarDecl(IntType(), y, IntLiteral(10))])]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_078_for_loop_with_complex_update():
    source = """
    void main() {
        for (int i = 0; i < 100; i = i * 2 + 1) {
            print(i);
        }
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([ForStmt(VarDecl(IntType(), i, IntLiteral(0)), BinaryOp(Identifier(i), <, IntLiteral(100)), AssignExpr(Identifier(i), BinaryOp(BinaryOp(Identifier(i), *, IntLiteral(2)), +, IntLiteral(1))), BlockStmt([FuncCall(Identifier(print), [Identifier(i)])]))]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_079_switch_multiple_cases_no_break():
    source = """
    void main() {
        int x = 1;
        switch (x) {
            case 1:
            case 2:
            case 3:
                print("1, 2 or 3");
                break;
        }
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(IntType(), x, IntLiteral(1)), SwitchStmt(Identifier(x), [Case(IntLiteral(1), BlockStmt([])), Case(IntLiteral(2), BlockStmt([])), Case(IntLiteral(3), BlockStmt([FuncCall(Identifier(print), [StringLiteral(1, 2 or 3)]), BreakStmt()]))])]))])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_080_complex_condition_while():
    source = """
    void main() {
        int a = 1;
        while (a == 1 && a != 2 || a > 0) {
            a--;
        }
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(IntType(), a, IntLiteral(1)), WhileStmt(BinaryOp(BinaryOp(BinaryOp(Identifier(a), ==, IntLiteral(1)), &&, BinaryOp(Identifier(a), !=, IntLiteral(2))), ||, BinaryOp(Identifier(a), >, IntLiteral(0))), BlockStmt([PostfixOp(Identifier(a), --)]))]))])"
    assert str(ASTGenerator(source).generate()) == expected
#DIFFICULT TESTS
def test_ast_gen_081_algorithm_gcd():
    source = """
    int gcd(int a, int b) {
        while (a != b) {
            if (a > b) {
                a = a - b;
            } else {
                b = b - a;
            }
        }
        return a;
    }
    """
    expected = ""
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_082_algorithm_factorial_recursive():
    source = """
    int factorial(int n) {
        if (n <= 1) {
            return 1;
        }
        return n * factorial(n - 1);
    }
    """
    expected = ""
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_083_algorithm_fibonacci_for_loop():
    source = """
    int fibonacci(int n) {
        int a = 0;
        int b = 1;
        int next;
        for (int i = 2; i <= n; i++) {
            next = a + b;
            a = b;
            b = next;
        }
        return b;
    }
    """
    expected = ""
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_084_struct_manipulation():
    source = """
    struct Point { int x; int y; };
    Point midpoint(Point p1, Point p2) {
        Point mid;
        mid.x = (p1.x + p2.x) / 2;
        mid.y = (p1.y + p2.y) / 2;
        return mid;
    }
    """
    expected = ""
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_085_mutual_recursion():
    source = """
    int isEven(int n) {
        if (n == 0) { return 1; }
        return isOdd(n - 1);
    }
    int isOdd(int n) {
        if (n == 0) { return 0; }
        return isEven(n - 1);
    }
    """
    expected = ""
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_086_nested_switch_in_for():
    source = """
    void processDates() {
        for (int month = 1; month <= 12; month++) {
            switch (month) {
                case 2:
                    print("28 or 29 days");
                    break;
                case 4: case 6: case 9: case 11:
                    print("30 days");
                    break;
                default:
                    print("31 days");
            }
        }
    }
    """
    expected = ""
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_087_deeply_nested_control_flow():
    source = """
    void complexLogic(int max) {
        int count = 0;
        while (count < max) {
            if (count % 2 == 0) {
                for (int i = 0; i < count; i++) {
                    print(i);
                }
            }
            count++;
        }
    }
    """
    expected = ""
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_088_chained_member_access():
    source = """
    struct A { int val; };
    struct B { A a; };
    struct C { B b; };
    void main() {
        C obj;
        obj.b.a.val = 42;
    }
    """
    expected = ""
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_089_mixed_unary_binary():
    source = """
    void main() {
        int x = 5;
        int y = 10;
        auto z = -x++ + --y * !(x == y);
    }
    """
    expected = ""
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_090_dangling_else_simulation():
    source = """
    void check(int a, int b) {
        if (a > 0)
            if (b > 0)
                print("Both positive");
            else
                print("a positive, b not");
    }
    """
    expected = ""
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_091_function_call_in_condition():
    source = """
    int isValid() { return 1; }
    void run() {
        while (isValid() == 1) {
            print("Running...");
        }
    }
    """
    expected = ""
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_092_return_inside_nested_loops():
    source = """
    int find(int target) {
        for (int i = 0; i < 10; i++) {
            for (int j = 0; j < 10; j++) {
                if (i * j == target) {
                    return 1;
                }
            }
        }
        return 0;
    }
    """
    expected = ""
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_093_complex_auto_inference():
    source = """
    int getMultiplier() { return 5; }
    void main() {
        auto value = (10 + 20) * getMultiplier() / 2;
    }
    """
    expected = ""
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_094_empty_program_structures():
    source = """
    struct Empty1 {};
    struct Empty2 {};
    """
    expected = ""
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_095_shadowing_variable_simulation():
    source = """
    void main() {
        int x = 1;
        {
            int x = 2;
            {
                int x = 3;
            }
        }
    }
    """
    expected = ""
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_096_multiple_assignments_with_function():
    source = """
    int init() { return 0; }
    void main() {
        int a; int b; int c;
        a = b = c = init();
    }
    """
    expected = ""
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_097_unconventional_for_loop():
    source = """
    void main() {
        int i = 0;
        for (; i < 10; ) {
            i++;
        }
    }
    """
    expected = ""
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_098_switch_with_complex_cases():
    source = """
    void main() {
        int code = 404;
        switch (code) {
            case 200:
                print("OK");
                break;
            case 404:
                {
                    string msg = "Not Found";
                    print(msg);
                }
                break;
        }
    }
    """
    expected = ""
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_099_heavy_math_formula():
    source = """
    void calculate() {
        float res = 3.14 * 2.0 * (15.5 - 4.2) / 3.0 + 7.5 % 2.0;
    }
    """
    expected = ""
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_100_the_final_boss():
    source = """
    struct Date { int d; int m; int y; };
    struct Student { int id; float gpa; Date dob; };

    void processStudent(Student s) {
        if (s.gpa >= 8.5) {
            print("Excellent");
        } else if (s.gpa >= 7.0) {
            print("Good");
        } else {
            print("Average");
        }
        
        while (s.id > 0) {
            s.id = s.id / 10;
        }
    }
    """
    expected = ""
    assert str(ASTGenerator(source).generate()) == expected