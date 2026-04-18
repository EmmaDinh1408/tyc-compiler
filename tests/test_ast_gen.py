"""
AST Generation test cases for TyC compiler.
TODO: Implement 100 test cases for AST generation
"""

import pytest
from tests.utils import ASTGenerator

#DECLARATION TESTS
def test_ast_gen_001():
    source = """
    struct Point {
        int x;
        int y;
    };
    """
    expected = "Program([StructDecl(Point, [MemberDecl(IntType(), x), MemberDecl(IntType(), y)])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_002():
    source = """
    void main() {
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], [])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_003():
    source = """
    int add(int x, int y) {
        return x + y;
    }
    """
    expected = "Program([FuncDecl(IntType(), add, [Param(IntType(), x), Param(IntType(), y)], [ReturnStmt(return BinaryOp(Identifier(x), +, Identifier(y)))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_004():
    source = """
    void main() {
        string s = "hello";
        float f = 3.14;
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], [VarDecl(StringType(), s = StringLiteral('hello')), VarDecl(FloatType(), f = FloatLiteral(3.14))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_005():
    source = """
    add(int x) {
        return x;
    }
    """
    expected = "Program([FuncDecl(auto, add, [Param(IntType(), x)], [ReturnStmt(return Identifier(x))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_006():
    source = """
    void main() {
        int x;
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], [VarDecl(IntType(), x)])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_007():
    source = """
    struct Point { int x; };
    void main() {
        Point p;
    }
    """
    expected = "Program([StructDecl(Point, [MemberDecl(IntType(), x)]), FuncDecl(VoidType(), main, [], [VarDecl(StructType(Point), p)])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_008():
    source = """
    void process(int a, float b, string c) {
    }
    """
    expected = "Program([FuncDecl(VoidType(), process, [Param(IntType(), a), Param(FloatType(), b), Param(StringType(), c)], [])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_009():
    source = """
    void greet() {
        print("Hello, World!");
    }
    """
    expected = "Program([FuncDecl(VoidType(), greet, [], [ExprStmt(FuncCall(print, [StringLiteral('Hello, World!')]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_010():
    source = """
    struct A { int x; };
    struct B { float y; };
    """
    expected = "Program([StructDecl(A, [MemberDecl(IntType(), x)]), StructDecl(B, [MemberDecl(FloatType(), y)])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_011():
    source = """
    struct Color { int r; };
    struct Point { Color c; };
    """
    expected = "Program([StructDecl(Color, [MemberDecl(IntType(), r)]), StructDecl(Point, [MemberDecl(StructType(Color), c)])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_012():
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
    expected = "Program([StructDecl(Point, [MemberDecl(IntType(), x), MemberDecl(IntType(), y)]), FuncDecl(StructType(Point), createPoint, [Param(IntType(), x), Param(IntType(), y)], [VarDecl(StructType(Point), p), ExprStmt(AssignExpr(MemberAccess(Identifier(p).x) = Identifier(x))), ExprStmt(AssignExpr(MemberAccess(Identifier(p).y) = Identifier(y))), ReturnStmt(return Identifier(p))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_013():
    source = """
    struct Point { int x; };
    Point getPoint() {
        Point p;
        return p;
    }
    """
    expected = "Program([StructDecl(Point, [MemberDecl(IntType(), x)]), FuncDecl(StructType(Point), getPoint, [], [VarDecl(StructType(Point), p), ReturnStmt(return Identifier(p))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_014():
    source = """
    struct Data {
        int i;
        float f;
        string s;
    };
    """
    expected = "Program([StructDecl(Data, [MemberDecl(IntType(), i), MemberDecl(FloatType(), f), MemberDecl(StringType(), s)])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_015():
    source = """
    void main() {
        auto x = 5 + 3 * 2;
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], [VarDecl(auto, x = BinaryOp(IntLiteral(5), +, BinaryOp(IntLiteral(3), *, IntLiteral(2))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_016():
    source = """
    void main() {
        auto x = (5 + 3) * 2;
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], [VarDecl(auto, x = BinaryOp(BinaryOp(IntLiteral(5), +, IntLiteral(3)), *, IntLiteral(2)))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_017():
    source = """
    struct Point { int x; };
    void main() {
        Point p;
        auto val = p.x;
    }
    """
    expected = "Program([StructDecl(Point, [MemberDecl(IntType(), x)]), FuncDecl(VoidType(), main, [], [VarDecl(StructType(Point), p), VarDecl(auto, val = MemberAccess(Identifier(p).x))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_018():
    source = """
    struct Color {
        int r;
        int g;
        int b;
    };
    struct Point {
        int x;
        int y;
        Color c;
    };
    """
    expected = "Program([StructDecl(Color, [MemberDecl(IntType(), r), MemberDecl(IntType(), g), MemberDecl(IntType(), b)]), StructDecl(Point, [MemberDecl(IntType(), x), MemberDecl(IntType(), y), MemberDecl(StructType(Color), c)])])" 
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_019():
    source = """
    int foo() { return 1; }
    int bar() { return foo(); }
    """
    expected = "Program([FuncDecl(IntType(), foo, [], [ReturnStmt(return IntLiteral(1))]), FuncDecl(IntType(), bar, [], [ReturnStmt(return FuncCall(foo, []))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_020():
    source = """
    struct Color {
        int r;
        int g;
        int b;
    };
    struct Point {
        int x;
        int y;
        Color color;
    };
    void move(Point p, int dx, int dy) {
        p.x = p.x + dx;
        p.y = p.y + dy;
    }
    """
    expected = "Program([StructDecl(Color, [MemberDecl(IntType(), r), MemberDecl(IntType(), g), MemberDecl(IntType(), b)]), StructDecl(Point, [MemberDecl(IntType(), x), MemberDecl(IntType(), y), MemberDecl(StructType(Color), color)]), FuncDecl(VoidType(), move, [Param(StructType(Point), p), Param(IntType(), dx), Param(IntType(), dy)], [ExprStmt(AssignExpr(MemberAccess(Identifier(p).x) = BinaryOp(MemberAccess(Identifier(p).x), +, Identifier(dx)))), ExprStmt(AssignExpr(MemberAccess(Identifier(p).y) = BinaryOp(MemberAccess(Identifier(p).y), +, Identifier(dy))))])])"
    assert str(ASTGenerator(source).generate()) == expected

#EXPRESSION TESTS
def test_ast_gen_021():
    source = """
    void main() {
        int result = (5 + 3) * 2;
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], [VarDecl(IntType(), result = BinaryOp(BinaryOp(IntLiteral(5), +, IntLiteral(3)), *, IntLiteral(2)))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_022():
    source = """
    void main() {
        bool flag = (true && false) || !false;
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], [VarDecl(StructType(bool), flag = BinaryOp(BinaryOp(Identifier(true), &&, Identifier(false)), ||, PrefixOp(!Identifier(false))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_023():
    source = """
    struct Point { int x; };
    void main() {
        Point p;
        int val = p.x;
    }
    """
    expected = "Program([StructDecl(Point, [MemberDecl(IntType(), x)]), FuncDecl(VoidType(), main, [], [VarDecl(StructType(Point), p), VarDecl(IntType(), val = MemberAccess(Identifier(p).x))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_024():
    source = """
    void greet(string name) {
        print("Hello, " + name);
    }
    void main() {
        greet("Alice");
    }
    """
    expected = "Program([FuncDecl(VoidType(), greet, [Param(StringType(), name)], [ExprStmt(FuncCall(print, [BinaryOp(StringLiteral('Hello, '), +, Identifier(name))]))]), FuncDecl(VoidType(), main, [], [ExprStmt(FuncCall(greet, [StringLiteral('Alice')]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_025():
    source = """
    int add(int x, int y) {
        return x + y;
    }
    void main() {
        int result = add(add(1, 2), 3);
    }
    """
    expected = "Program([FuncDecl(IntType(), add, [Param(IntType(), x), Param(IntType(), y)], [ReturnStmt(return BinaryOp(Identifier(x), +, Identifier(y)))]), FuncDecl(VoidType(), main, [], [VarDecl(IntType(), result = FuncCall(add, [FuncCall(add, [IntLiteral(1), IntLiteral(2)]), IntLiteral(3)]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_026():
    source = """
    void main() {
        auto x = (5 + 3) * (2 - 1) / 4;
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], [VarDecl(auto, x = BinaryOp(BinaryOp(BinaryOp(IntLiteral(5), +, IntLiteral(3)), *, BinaryOp(IntLiteral(2), -, IntLiteral(1))), /, IntLiteral(4)))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_027():
    source = """
    void main() {
        int x = -5;
        bool flag = !true;
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], [VarDecl(IntType(), x = PrefixOp(-IntLiteral(5))), VarDecl(StructType(bool), flag = PrefixOp(!Identifier(true)))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_028():
    source = """
    void main() {
        auto result = (5 + 3) * 2 > 10 && !false;
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], [VarDecl(auto, result = BinaryOp(BinaryOp(BinaryOp(BinaryOp(IntLiteral(5), +, IntLiteral(3)), *, IntLiteral(2)), >, IntLiteral(10)), &&, PrefixOp(!Identifier(false))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_029():
    source = """
    struct Point { int x; };
    void main() {
        Point p;
        int val = p.x + 5;
    }
    """
    expected = "Program([StructDecl(Point, [MemberDecl(IntType(), x)]), FuncDecl(VoidType(), main, [], [VarDecl(StructType(Point), p), VarDecl(IntType(), val = BinaryOp(MemberAccess(Identifier(p).x), +, IntLiteral(5)))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_030():
    source = """
    void printSum(int a, int b) {
        print(a + b);
    }
    void main() {
        printSum(5, 3 * 2);
    }
    """
    expected = "Program([FuncDecl(VoidType(), printSum, [Param(IntType(), a), Param(IntType(), b)], [ExprStmt(FuncCall(print, [BinaryOp(Identifier(a), +, Identifier(b))]))]), FuncDecl(VoidType(), main, [], [ExprStmt(FuncCall(printSum, [IntLiteral(5), BinaryOp(IntLiteral(3), *, IntLiteral(2))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_031():
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
    expected = "Program([FuncDecl(VoidType(), main, [], [VarDecl(IntType(), x = IntLiteral(5)), IfStmt(if BinaryOp(Identifier(x), >, IntLiteral(0)) then BlockStmt([ExprStmt(FuncCall(print, [StringLiteral('Positive')]))]), else BlockStmt([ExprStmt(FuncCall(print, [StringLiteral('Non-positive')]))]))])])" 
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_032():
    source = """
    void main() {
        for (int i = 0; i < 10; i = i + 1) {
            print(i);
        }
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], [ForStmt(for VarDecl(IntType(), i = IntLiteral(0)); BinaryOp(Identifier(i), <, IntLiteral(10)); AssignExpr(Identifier(i) = BinaryOp(Identifier(i), +, IntLiteral(1))) do BlockStmt([ExprStmt(FuncCall(print, [Identifier(i)]))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_033():
    source = """
    void main() {
        int i = 0;
        while (i < 10) {
            print(i);
            i = i + 1;
        }
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], [VarDecl(IntType(), i = IntLiteral(0)), WhileStmt(while BinaryOp(Identifier(i), <, IntLiteral(10)) do BlockStmt([ExprStmt(FuncCall(print, [Identifier(i)])), ExprStmt(AssignExpr(Identifier(i) = BinaryOp(Identifier(i), +, IntLiteral(1))))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_034():
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
    expected = "Program([FuncDecl(VoidType(), main, [], [VarDecl(IntType(), x = IntLiteral(2)), SwitchStmt(switch Identifier(x) cases [CaseStmt(case IntLiteral(1): [ExprStmt(FuncCall(print, [StringLiteral('One')])), BreakStmt()]), CaseStmt(case IntLiteral(2): [ExprStmt(FuncCall(print, [StringLiteral('Two')])), BreakStmt()])], default DefaultStmt(default: [ExprStmt(FuncCall(print, [StringLiteral('Other')]))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_035():
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
    expected = "Program([FuncDecl(VoidType(), main, [], [ForStmt(for VarDecl(IntType(), i = IntLiteral(0)); BinaryOp(Identifier(i), <, IntLiteral(5)); AssignExpr(Identifier(i) = BinaryOp(Identifier(i), +, IntLiteral(1))) do BlockStmt([IfStmt(if BinaryOp(BinaryOp(Identifier(i), %, IntLiteral(2)), ==, IntLiteral(0)) then BlockStmt([ExprStmt(FuncCall(print, [Identifier(i)]))]), else BlockStmt([ExprStmt(FuncCall(print, [StringLiteral('Odd')]))]))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_036():
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
    expected = "Program([FuncDecl(VoidType(), main, [], [VarDecl(IntType(), x = IntLiteral(5)), IfStmt(if BinaryOp(BinaryOp(Identifier(x), >, IntLiteral(0)), &&, BinaryOp(Identifier(x), <, IntLiteral(10))) then BlockStmt([ExprStmt(FuncCall(print, [StringLiteral('In range')]))]), else BlockStmt([ExprStmt(FuncCall(print, [StringLiteral('Out of range')]))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_037():
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
    expected = "Program([FuncDecl(VoidType(), main, [], [ForStmt(for VarDecl(IntType(), i = IntLiteral(0)); BinaryOp(Identifier(i), <, IntLiteral(10)); AssignExpr(Identifier(i) = BinaryOp(Identifier(i), +, IntLiteral(1))) do BlockStmt([IfStmt(if BinaryOp(Identifier(i), ==, IntLiteral(5)) then BlockStmt([BreakStmt()])), ExprStmt(FuncCall(print, [Identifier(i)]))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_038():
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
    expected = "Program([FuncDecl(VoidType(), main, [], [VarDecl(IntType(), i = IntLiteral(0)), WhileStmt(while BinaryOp(Identifier(i), <, IntLiteral(10)) do BlockStmt([ExprStmt(AssignExpr(Identifier(i) = BinaryOp(Identifier(i), +, IntLiteral(1)))), IfStmt(if BinaryOp(BinaryOp(Identifier(i), %, IntLiteral(2)), ==, IntLiteral(0)) then BlockStmt([ContinueStmt()])), ExprStmt(FuncCall(print, [Identifier(i)]))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_039():
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
    expected = "Program([FuncDecl(VoidType(), main, [], [VarDecl(IntType(), x = IntLiteral(1)), SwitchStmt(switch Identifier(x) cases [CaseStmt(case IntLiteral(1): [ExprStmt(FuncCall(print, [StringLiteral('One')]))]), CaseStmt(case IntLiteral(2): [ExprStmt(FuncCall(print, [StringLiteral('Two')])), BreakStmt()])], default DefaultStmt(default: [ExprStmt(FuncCall(print, [StringLiteral('Other')]))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_040():
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
    expected = "Program([FuncDecl(VoidType(), main, [], [VarDecl(IntType(), x = IntLiteral(1)), SwitchStmt(switch Identifier(x) cases [CaseStmt(case IntLiteral(1): [VarDecl(IntType(), y = IntLiteral(2)), SwitchStmt(switch Identifier(y) cases [CaseStmt(case IntLiteral(2): [ExprStmt(FuncCall(print, [StringLiteral('Nested Two')])), BreakStmt()])], default DefaultStmt(default: [ExprStmt(FuncCall(print, [StringLiteral('Nested Other')]))])), BreakStmt()])], default DefaultStmt(default: [ExprStmt(FuncCall(print, [StringLiteral('Other')]))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_041():
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
    expected = "Program([FuncDecl(VoidType(), main, [], [VarDecl(IntType(), x = IntLiteral(5)), IfStmt(if BinaryOp(Identifier(x), >, IntLiteral(0)) then BlockStmt([ForStmt(for VarDecl(IntType(), i = IntLiteral(0)); BinaryOp(Identifier(i), <, Identifier(x)); AssignExpr(Identifier(i) = BinaryOp(Identifier(i), +, IntLiteral(1))) do BlockStmt([ExprStmt(FuncCall(print, [Identifier(i)]))]))]), else BlockStmt([ExprStmt(FuncCall(print, [StringLiteral('Non-positive')]))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_042():
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
    expected = "Program([FuncDecl(VoidType(), main, [], [ForStmt(for VarDecl(IntType(), i = IntLiteral(0)); BinaryOp(Identifier(i), <, IntLiteral(5)); AssignExpr(Identifier(i) = BinaryOp(Identifier(i), +, IntLiteral(1))) do BlockStmt([IfStmt(if BinaryOp(BinaryOp(Identifier(i), %, IntLiteral(2)), ==, IntLiteral(0)) then BlockStmt([ExprStmt(FuncCall(print, [Identifier(i)]))]), else BlockStmt([ExprStmt(FuncCall(print, [StringLiteral('Odd')]))]))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_043():
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
    expected = "Program([FuncDecl(VoidType(), main, [], [VarDecl(IntType(), i = IntLiteral(0)), WhileStmt(while BinaryOp(Identifier(i), <, IntLiteral(3)) do BlockStmt([SwitchStmt(switch Identifier(i) cases [CaseStmt(case IntLiteral(0): [ExprStmt(FuncCall(print, [StringLiteral('Zero')])), BreakStmt()]), CaseStmt(case IntLiteral(1): [ExprStmt(FuncCall(print, [StringLiteral('One')])), BreakStmt()])], default DefaultStmt(default: [ExprStmt(FuncCall(print, [StringLiteral('Other')]))])), ExprStmt(AssignExpr(Identifier(i) = BinaryOp(Identifier(i), +, IntLiteral(1))))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_044():
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
    expected = "Program([FuncDecl(VoidType(), main, [], [VarDecl(IntType(), x = IntLiteral(1)), SwitchStmt(switch Identifier(x) cases [CaseStmt(case IntLiteral(1): [IfStmt(if BinaryOp(Identifier(x), >, IntLiteral(0)) then BlockStmt([ExprStmt(FuncCall(print, [StringLiteral('Positive One')]))]), else BlockStmt([ExprStmt(FuncCall(print, [StringLiteral('Non-positive One')]))])), BreakStmt()])], default DefaultStmt(default: [ExprStmt(FuncCall(print, [StringLiteral('Other')]))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_045():
    source = """
    void main() {
        int a; int b; int c;
        a = b = c = 10;
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], [VarDecl(IntType(), a), VarDecl(IntType(), b), VarDecl(IntType(), c), ExprStmt(AssignExpr(Identifier(a) = AssignExpr(Identifier(b) = AssignExpr(Identifier(c) = IntLiteral(10)))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_046():
    source = """
    void main() {
        int i = 0;
        i++;
        i--;
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], [VarDecl(IntType(), i = IntLiteral(0)), ExprStmt(PostfixOp(Identifier(i)++)), ExprStmt(PostfixOp(Identifier(i)--))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_047():
    source = """
    void main() {
        int x = 5;
        int y = - ++x;
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], [VarDecl(IntType(), x = IntLiteral(5)), VarDecl(IntType(), y = PrefixOp(-PrefixOp(++Identifier(x))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_048():
    source = """
    void main() {
        auto result = (5 > 3) && !(10 == 10) || (1 < 0);
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], [VarDecl(auto, result = BinaryOp(BinaryOp(BinaryOp(IntLiteral(5), >, IntLiteral(3)), &&, PrefixOp(!BinaryOp(IntLiteral(10), ==, IntLiteral(10)))), ||, BinaryOp(IntLiteral(1), <, IntLiteral(0))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_049():
    source = """
    struct Inner { int val; };
    struct Outer { Inner in; };
    void main() {
        Outer out;
        out.in.val = 100;
    }
    """
    expected = "Program([StructDecl(Inner, [MemberDecl(IntType(), val)]), StructDecl(Outer, [MemberDecl(StructType(Inner), in)]), FuncDecl(VoidType(), main, [], [VarDecl(StructType(Outer), out), ExprStmt(AssignExpr(MemberAccess(MemberAccess(Identifier(out).in).val) = IntLiteral(100)))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_050():
    source = """
    int mult(int a, int b) { return a * b; }
    void main() {
        int result = mult(mult(2, 3), 4);
    }
    """
    expected = "Program([FuncDecl(IntType(), mult, [Param(IntType(), a), Param(IntType(), b)], [ReturnStmt(return BinaryOp(Identifier(a), *, Identifier(b)))]), FuncDecl(VoidType(), main, [], [VarDecl(IntType(), result = FuncCall(mult, [FuncCall(mult, [IntLiteral(2), IntLiteral(3)]), IntLiteral(4)]))])])"
    assert str(ASTGenerator(source).generate()) == expected   

#STATEMENT TESTS
def test_ast_gen_051():
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
    expected = "Program([FuncDecl(VoidType(), main, [], [VarDecl(IntType(), x = IntLiteral(5)), IfStmt(if BinaryOp(Identifier(x), >, IntLiteral(0)) then BlockStmt([ExprStmt(FuncCall(print, [StringLiteral('Positive')]))]), else BlockStmt([ExprStmt(FuncCall(print, [StringLiteral('Non-positive')]))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_052():
    source = """
    void main() {
        for (int i = 0; i < 10; i = i + 1) {
            print(i);
        }
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], [ForStmt(for VarDecl(IntType(), i = IntLiteral(0)); BinaryOp(Identifier(i), <, IntLiteral(10)); AssignExpr(Identifier(i) = BinaryOp(Identifier(i), +, IntLiteral(1))) do BlockStmt([ExprStmt(FuncCall(print, [Identifier(i)]))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_053():
    source = """
    void main() {
        int i = 0;
        while (i < 10) {
            print(i);
            i = i + 1;
        }
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], [VarDecl(IntType(), i = IntLiteral(0)), WhileStmt(while BinaryOp(Identifier(i), <, IntLiteral(10)) do BlockStmt([ExprStmt(FuncCall(print, [Identifier(i)])), ExprStmt(AssignExpr(Identifier(i) = BinaryOp(Identifier(i), +, IntLiteral(1))))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_054():
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
    expected = "Program([FuncDecl(VoidType(), main, [], [VarDecl(IntType(), x = IntLiteral(2)), SwitchStmt(switch Identifier(x) cases [CaseStmt(case IntLiteral(1): [ExprStmt(FuncCall(print, [StringLiteral('One')])), BreakStmt()]), CaseStmt(case IntLiteral(2): [ExprStmt(FuncCall(print, [StringLiteral('Two')])), BreakStmt()])], default DefaultStmt(default: [ExprStmt(FuncCall(print, [StringLiteral('Other')]))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_055():
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
    expected = "Program([FuncDecl(VoidType(), main, [], [ForStmt(for VarDecl(IntType(), i = IntLiteral(0)); BinaryOp(Identifier(i), <, IntLiteral(5)); AssignExpr(Identifier(i) = BinaryOp(Identifier(i), +, IntLiteral(1))) do BlockStmt([IfStmt(if BinaryOp(BinaryOp(Identifier(i), %, IntLiteral(2)), ==, IntLiteral(0)) then BlockStmt([ExprStmt(FuncCall(print, [Identifier(i)]))]), else BlockStmt([ExprStmt(FuncCall(print, [StringLiteral('Odd')]))]))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_056():
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
    expected = "Program([FuncDecl(VoidType(), main, [], [VarDecl(IntType(), x = IntLiteral(5)), IfStmt(if BinaryOp(BinaryOp(Identifier(x), >, IntLiteral(0)), &&, BinaryOp(Identifier(x), <, IntLiteral(10))) then BlockStmt([ExprStmt(FuncCall(print, [StringLiteral('In range')]))]), else BlockStmt([ExprStmt(FuncCall(print, [StringLiteral('Out of range')]))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_057():
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
    expected = "Program([FuncDecl(VoidType(), main, [], [ForStmt(for VarDecl(IntType(), i = IntLiteral(0)); BinaryOp(Identifier(i), <, IntLiteral(10)); AssignExpr(Identifier(i) = BinaryOp(Identifier(i), +, IntLiteral(1))) do BlockStmt([IfStmt(if BinaryOp(Identifier(i), ==, IntLiteral(5)) then BlockStmt([BreakStmt()])), ExprStmt(FuncCall(print, [Identifier(i)]))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_058():
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
    expected = "Program([FuncDecl(VoidType(), main, [], [VarDecl(IntType(), i = IntLiteral(0)), WhileStmt(while BinaryOp(Identifier(i), <, IntLiteral(10)) do BlockStmt([ExprStmt(AssignExpr(Identifier(i) = BinaryOp(Identifier(i), +, IntLiteral(1)))), IfStmt(if BinaryOp(BinaryOp(Identifier(i), %, IntLiteral(2)), ==, IntLiteral(0)) then BlockStmt([ContinueStmt()])), ExprStmt(FuncCall(print, [Identifier(i)]))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_059():
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
    expected = "Program([FuncDecl(VoidType(), main, [], [VarDecl(IntType(), x = IntLiteral(1)), SwitchStmt(switch Identifier(x) cases [CaseStmt(case IntLiteral(1): [ExprStmt(FuncCall(print, [StringLiteral('One')]))]), CaseStmt(case IntLiteral(2): [ExprStmt(FuncCall(print, [StringLiteral('Two')])), BreakStmt()])], default DefaultStmt(default: [ExprStmt(FuncCall(print, [StringLiteral('Other')]))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_060():
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
    expected = "Program([FuncDecl(VoidType(), main, [], [VarDecl(IntType(), x = IntLiteral(1)), SwitchStmt(switch Identifier(x) cases [CaseStmt(case IntLiteral(1): [VarDecl(IntType(), y = IntLiteral(2)), SwitchStmt(switch Identifier(y) cases [CaseStmt(case IntLiteral(2): [ExprStmt(FuncCall(print, [StringLiteral('Nested Two')])), BreakStmt()])], default DefaultStmt(default: [ExprStmt(FuncCall(print, [StringLiteral('Nested Other')]))])), BreakStmt()])], default DefaultStmt(default: [ExprStmt(FuncCall(print, [StringLiteral('Other')]))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_061():
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
    expected = "Program([FuncDecl(VoidType(), main, [], [VarDecl(IntType(), x = IntLiteral(5)), IfStmt(if BinaryOp(Identifier(x), >, IntLiteral(0)) then BlockStmt([ForStmt(for VarDecl(IntType(), i = IntLiteral(0)); BinaryOp(Identifier(i), <, Identifier(x)); AssignExpr(Identifier(i) = BinaryOp(Identifier(i), +, IntLiteral(1))) do BlockStmt([ExprStmt(FuncCall(print, [Identifier(i)]))]))]), else BlockStmt([ExprStmt(FuncCall(print, [StringLiteral('Non-positive')]))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_062():
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
    expected = "Program([FuncDecl(VoidType(), main, [], [ForStmt(for VarDecl(IntType(), i = IntLiteral(0)); BinaryOp(Identifier(i), <, IntLiteral(5)); AssignExpr(Identifier(i) = BinaryOp(Identifier(i), +, IntLiteral(1))) do BlockStmt([IfStmt(if BinaryOp(BinaryOp(Identifier(i), %, IntLiteral(2)), ==, IntLiteral(0)) then BlockStmt([ExprStmt(FuncCall(print, [Identifier(i)]))]), else BlockStmt([ExprStmt(FuncCall(print, [StringLiteral('Odd')]))]))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_063():
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
    expected = "Program([FuncDecl(VoidType(), main, [], [VarDecl(IntType(), i = IntLiteral(0)), WhileStmt(while BinaryOp(Identifier(i), <, IntLiteral(3)) do BlockStmt([SwitchStmt(switch Identifier(i) cases [CaseStmt(case IntLiteral(0): [ExprStmt(FuncCall(print, [StringLiteral('Zero')])), BreakStmt()]), CaseStmt(case IntLiteral(1): [ExprStmt(FuncCall(print, [StringLiteral('One')])), BreakStmt()])], default DefaultStmt(default: [ExprStmt(FuncCall(print, [StringLiteral('Other')]))])), ExprStmt(AssignExpr(Identifier(i) = BinaryOp(Identifier(i), +, IntLiteral(1))))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_064():
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
    expected = "Program([FuncDecl(VoidType(), main, [], [VarDecl(IntType(), x = IntLiteral(1)), SwitchStmt(switch Identifier(x) cases [CaseStmt(case IntLiteral(1): [IfStmt(if BinaryOp(Identifier(x), >, IntLiteral(0)) then BlockStmt([ExprStmt(FuncCall(print, [StringLiteral('Positive One')]))]), else BlockStmt([ExprStmt(FuncCall(print, [StringLiteral('Non-positive One')]))])), BreakStmt()])], default DefaultStmt(default: [ExprStmt(FuncCall(print, [StringLiteral('Other')]))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_065():
    source = """
    void main() {
        int a; int b; int c;
        a = b = c = 10;
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], [VarDecl(IntType(), a), VarDecl(IntType(), b), VarDecl(IntType(), c), ExprStmt(AssignExpr(Identifier(a) = AssignExpr(Identifier(b) = AssignExpr(Identifier(c) = IntLiteral(10)))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_066():
    source = """
    void main() {
        int i = 0;
        i++;
        i--;
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], [VarDecl(IntType(), i = IntLiteral(0)), ExprStmt(PostfixOp(Identifier(i)++)), ExprStmt(PostfixOp(Identifier(i)--))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_067():
    source = """
    void main() {
        int x = 5;
        int y = - ++x;
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], [VarDecl(IntType(), x = IntLiteral(5)), VarDecl(IntType(), y = PrefixOp(-PrefixOp(++Identifier(x))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_068():
    source = """
    void main() {
        auto result = (5 > 3) && !(10 == 10) || (1 < 0);
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], [VarDecl(auto, result = BinaryOp(BinaryOp(BinaryOp(IntLiteral(5), >, IntLiteral(3)), &&, PrefixOp(!BinaryOp(IntLiteral(10), ==, IntLiteral(10)))), ||, BinaryOp(IntLiteral(1), <, IntLiteral(0))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_069():
    source = """
    struct Inner { int val; };
    struct Outer { Inner in; };
    void main() {
        Outer out;
        out.in.val = 100;
    }
    """
    expected = "Program([StructDecl(Inner, [MemberDecl(IntType(), val)]), StructDecl(Outer, [MemberDecl(StructType(Inner), in)]), FuncDecl(VoidType(), main, [], [VarDecl(StructType(Outer), out), ExprStmt(AssignExpr(MemberAccess(MemberAccess(Identifier(out).in).val) = IntLiteral(100)))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_070():
    source = """
    int mult(int a, int b) { return a * b; }
    void main() {
        int result = mult(mult(2, 3), 4);
    }
    """
    expected = "Program([FuncDecl(IntType(), mult, [Param(IntType(), a), Param(IntType(), b)], [ReturnStmt(return BinaryOp(Identifier(a), *, Identifier(b)))]), FuncDecl(VoidType(), main, [], [VarDecl(IntType(), result = FuncCall(mult, [FuncCall(mult, [IntLiteral(2), IntLiteral(3)]), IntLiteral(4)]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_071():
    source = """
    void main() {
        int x = 5;
        if (x > 0) {
            x = x - 1;
        }
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], [VarDecl(IntType(), x = IntLiteral(5)), IfStmt(if BinaryOp(Identifier(x), >, IntLiteral(0)) then BlockStmt([ExprStmt(AssignExpr(Identifier(x) = BinaryOp(Identifier(x), -, IntLiteral(1))))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_072():
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
    expected = "Program([FuncDecl(VoidType(), main, [], [VarDecl(IntType(), x = IntLiteral(0)), IfStmt(if BinaryOp(Identifier(x), >, IntLiteral(0)) then BlockStmt([ExprStmt(AssignExpr(Identifier(x) = IntLiteral(1)))]), else IfStmt(if BinaryOp(Identifier(x), <, IntLiteral(0)) then BlockStmt([ExprStmt(AssignExpr(Identifier(x) = PrefixOp(-IntLiteral(1))))]), else BlockStmt([ExprStmt(AssignExpr(Identifier(x) = IntLiteral(0)))])))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_073():
    source = """
    void doNothing() {
        return;
    }
    """
    expected = "Program([FuncDecl(VoidType(), doNothing, [], [ReturnStmt(return)])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_074():
    source = """
    void main() {
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                print(i, j);
            }
        }
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], [ForStmt(for VarDecl(IntType(), i = IntLiteral(0)); BinaryOp(Identifier(i), <, IntLiteral(3)); PostfixOp(Identifier(i)++) do BlockStmt([ForStmt(for VarDecl(IntType(), j = IntLiteral(0)); BinaryOp(Identifier(j), <, IntLiteral(3)); PostfixOp(Identifier(j)++) do BlockStmt([ExprStmt(FuncCall(print, [Identifier(i), Identifier(j)]))]))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_075():
    source = """
    void main() {
        while (1 < 0) {}
        if (1 == 1) {} else {}
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], [WhileStmt(while BinaryOp(IntLiteral(1), <, IntLiteral(0)) do BlockStmt([])), IfStmt(if BinaryOp(IntLiteral(1), ==, IntLiteral(1)) then BlockStmt([]), else BlockStmt([]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_076():
    source = """
    void main() {
        5 + 3;
        foo();
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(BinaryOp(IntLiteral(5), +, IntLiteral(3))), ExprStmt(FuncCall(foo, []))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_077():
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
    expected = "Program([FuncDecl(VoidType(), main, [], [BlockStmt([VarDecl(IntType(), x = IntLiteral(5))]), BlockStmt([VarDecl(IntType(), y = IntLiteral(10))])])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_078():
    source = """
    void main() {
        for (int i = 0; i < 100; i = i * 2 + 1) {
            print(i);
        }
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], [ForStmt(for VarDecl(IntType(), i = IntLiteral(0)); BinaryOp(Identifier(i), <, IntLiteral(100)); AssignExpr(Identifier(i) = BinaryOp(BinaryOp(Identifier(i), *, IntLiteral(2)), +, IntLiteral(1))) do BlockStmt([ExprStmt(FuncCall(print, [Identifier(i)]))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_079():
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
    expected = "Program([FuncDecl(VoidType(), main, [], [VarDecl(IntType(), x = IntLiteral(1)), SwitchStmt(switch Identifier(x) cases [CaseStmt(case IntLiteral(1): []), CaseStmt(case IntLiteral(2): []), CaseStmt(case IntLiteral(3): [ExprStmt(FuncCall(print, [StringLiteral('1, 2 or 3')])), BreakStmt()])])])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_080():
    source = """
    void main() {
        int a = 1;
        while (a == 1 && a != 2 || a > 0) {
            a--;
        }
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], [VarDecl(IntType(), a = IntLiteral(1)), WhileStmt(while BinaryOp(BinaryOp(BinaryOp(Identifier(a), ==, IntLiteral(1)), &&, BinaryOp(Identifier(a), !=, IntLiteral(2))), ||, BinaryOp(Identifier(a), >, IntLiteral(0))) do BlockStmt([ExprStmt(PostfixOp(Identifier(a)--))]))])])"
    assert str(ASTGenerator(source).generate()) == expected
#DIFFICULT TESTS
def test_ast_gen_081():
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
    expected = "Program([FuncDecl(IntType(), gcd, [Param(IntType(), a), Param(IntType(), b)], [WhileStmt(while BinaryOp(Identifier(a), !=, Identifier(b)) do BlockStmt([IfStmt(if BinaryOp(Identifier(a), >, Identifier(b)) then BlockStmt([ExprStmt(AssignExpr(Identifier(a) = BinaryOp(Identifier(a), -, Identifier(b))))]), else BlockStmt([ExprStmt(AssignExpr(Identifier(b) = BinaryOp(Identifier(b), -, Identifier(a))))]))])), ReturnStmt(return Identifier(a))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_082():
    source = """
    int factorial(int n) {
        if (n <= 1) {
            return 1;
        }
        return n * factorial(n - 1);
    }
    """
    expected = "Program([FuncDecl(IntType(), factorial, [Param(IntType(), n)], [IfStmt(if BinaryOp(Identifier(n), <=, IntLiteral(1)) then BlockStmt([ReturnStmt(return IntLiteral(1))])), ReturnStmt(return BinaryOp(Identifier(n), *, FuncCall(factorial, [BinaryOp(Identifier(n), -, IntLiteral(1))])))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_083():
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
    expected = "Program([FuncDecl(IntType(), fibonacci, [Param(IntType(), n)], [VarDecl(IntType(), a = IntLiteral(0)), VarDecl(IntType(), b = IntLiteral(1)), VarDecl(IntType(), next), ForStmt(for VarDecl(IntType(), i = IntLiteral(2)); BinaryOp(Identifier(i), <=, Identifier(n)); PostfixOp(Identifier(i)++) do BlockStmt([ExprStmt(AssignExpr(Identifier(next) = BinaryOp(Identifier(a), +, Identifier(b)))), ExprStmt(AssignExpr(Identifier(a) = Identifier(b))), ExprStmt(AssignExpr(Identifier(b) = Identifier(next)))])), ReturnStmt(return Identifier(b))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_084():
    source = """
    struct Point { int x; int y; };
    Point midpoint(Point p1, Point p2) {
        Point mid;
        mid.x = (p1.x + p2.x) / 2;
        mid.y = (p1.y + p2.y) / 2;
        return mid;
    }
    """
    expected = "Program([StructDecl(Point, [MemberDecl(IntType(), x), MemberDecl(IntType(), y)]), FuncDecl(StructType(Point), midpoint, [Param(StructType(Point), p1), Param(StructType(Point), p2)], [VarDecl(StructType(Point), mid), ExprStmt(AssignExpr(MemberAccess(Identifier(mid).x) = BinaryOp(BinaryOp(MemberAccess(Identifier(p1).x), +, MemberAccess(Identifier(p2).x)), /, IntLiteral(2)))), ExprStmt(AssignExpr(MemberAccess(Identifier(mid).y) = BinaryOp(BinaryOp(MemberAccess(Identifier(p1).y), +, MemberAccess(Identifier(p2).y)), /, IntLiteral(2)))), ReturnStmt(return Identifier(mid))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_085():
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
    expected = "Program([FuncDecl(IntType(), isEven, [Param(IntType(), n)], [IfStmt(if BinaryOp(Identifier(n), ==, IntLiteral(0)) then BlockStmt([ReturnStmt(return IntLiteral(1))])), ReturnStmt(return FuncCall(isOdd, [BinaryOp(Identifier(n), -, IntLiteral(1))]))]), FuncDecl(IntType(), isOdd, [Param(IntType(), n)], [IfStmt(if BinaryOp(Identifier(n), ==, IntLiteral(0)) then BlockStmt([ReturnStmt(return IntLiteral(0))])), ReturnStmt(return FuncCall(isEven, [BinaryOp(Identifier(n), -, IntLiteral(1))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_086():
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
    expected = "Program([FuncDecl(VoidType(), processDates, [], [ForStmt(for VarDecl(IntType(), month = IntLiteral(1)); BinaryOp(Identifier(month), <=, IntLiteral(12)); PostfixOp(Identifier(month)++) do BlockStmt([SwitchStmt(switch Identifier(month) cases [CaseStmt(case IntLiteral(2): [ExprStmt(FuncCall(print, [StringLiteral('28 or 29 days')])), BreakStmt()]), CaseStmt(case IntLiteral(4): []), CaseStmt(case IntLiteral(6): []), CaseStmt(case IntLiteral(9): []), CaseStmt(case IntLiteral(11): [ExprStmt(FuncCall(print, [StringLiteral('30 days')])), BreakStmt()])], default DefaultStmt(default: [ExprStmt(FuncCall(print, [StringLiteral('31 days')]))]))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_087():
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
    expected = "Program([FuncDecl(VoidType(), complexLogic, [Param(IntType(), max)], [VarDecl(IntType(), count = IntLiteral(0)), WhileStmt(while BinaryOp(Identifier(count), <, Identifier(max)) do BlockStmt([IfStmt(if BinaryOp(BinaryOp(Identifier(count), %, IntLiteral(2)), ==, IntLiteral(0)) then BlockStmt([ForStmt(for VarDecl(IntType(), i = IntLiteral(0)); BinaryOp(Identifier(i), <, Identifier(count)); PostfixOp(Identifier(i)++) do BlockStmt([ExprStmt(FuncCall(print, [Identifier(i)]))]))])), ExprStmt(PostfixOp(Identifier(count)++))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_088():
    source = """
    struct A { int val; };
    struct B { A a; };
    struct C { B b; };
    void main() {
        C obj;
        obj.b.a.val = 42;
    }
    """
    expected = "Program([StructDecl(A, [MemberDecl(IntType(), val)]), StructDecl(B, [MemberDecl(StructType(A), a)]), StructDecl(C, [MemberDecl(StructType(B), b)]), FuncDecl(VoidType(), main, [], [VarDecl(StructType(C), obj), ExprStmt(AssignExpr(MemberAccess(MemberAccess(MemberAccess(Identifier(obj).b).a).val) = IntLiteral(42)))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_089():
    source = """
    void main() {
        int x = 5;
        int y = 10;
        auto z = -x++ + --y * !(x == y);
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], [VarDecl(IntType(), x = IntLiteral(5)), VarDecl(IntType(), y = IntLiteral(10)), VarDecl(auto, z = BinaryOp(PrefixOp(-PostfixOp(Identifier(x)++)), +, BinaryOp(PrefixOp(--Identifier(y)), *, PrefixOp(!BinaryOp(Identifier(x), ==, Identifier(y))))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_090():
    source = """
    void check(int a, int b) {
        if (a > 0)
            if (b > 0)
                print("Both positive");
            else
                print("a positive, b not");
    }
    """
    expected = "Program([FuncDecl(VoidType(), check, [Param(IntType(), a), Param(IntType(), b)], [IfStmt(if BinaryOp(Identifier(a), >, IntLiteral(0)) then IfStmt(if BinaryOp(Identifier(b), >, IntLiteral(0)) then ExprStmt(FuncCall(print, [StringLiteral('Both positive')])), else ExprStmt(FuncCall(print, [StringLiteral('a positive, b not')]))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_091():
    source = """
    int isValid() { return 1; }
    void run() {
        while (isValid() == 1) {
            print("Running...");
        }
    }
    """
    expected = "Program([FuncDecl(IntType(), isValid, [], [ReturnStmt(return IntLiteral(1))]), FuncDecl(VoidType(), run, [], [WhileStmt(while BinaryOp(FuncCall(isValid, []), ==, IntLiteral(1)) do BlockStmt([ExprStmt(FuncCall(print, [StringLiteral('Running...')]))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_092():
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
    expected = "Program([FuncDecl(IntType(), find, [Param(IntType(), target)], [ForStmt(for VarDecl(IntType(), i = IntLiteral(0)); BinaryOp(Identifier(i), <, IntLiteral(10)); PostfixOp(Identifier(i)++) do BlockStmt([ForStmt(for VarDecl(IntType(), j = IntLiteral(0)); BinaryOp(Identifier(j), <, IntLiteral(10)); PostfixOp(Identifier(j)++) do BlockStmt([IfStmt(if BinaryOp(BinaryOp(Identifier(i), *, Identifier(j)), ==, Identifier(target)) then BlockStmt([ReturnStmt(return IntLiteral(1))]))]))])), ReturnStmt(return IntLiteral(0))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_093():
    source = """
    int getMultiplier() { return 5; }
    void main() {
        auto value = (10 + 20) * getMultiplier() / 2;
    }
    """
    expected = "Program([FuncDecl(IntType(), getMultiplier, [], [ReturnStmt(return IntLiteral(5))]), FuncDecl(VoidType(), main, [], [VarDecl(auto, value = BinaryOp(BinaryOp(BinaryOp(IntLiteral(10), +, IntLiteral(20)), *, FuncCall(getMultiplier, [])), /, IntLiteral(2)))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_094():
    source = """
    struct Empty1 {};
    struct Empty2 {};
    """
    expected = "Program([StructDecl(Empty1, []), StructDecl(Empty2, [])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_095():
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
    expected = "Program([FuncDecl(VoidType(), main, [], [VarDecl(IntType(), x = IntLiteral(1)), BlockStmt([VarDecl(IntType(), x = IntLiteral(2)), BlockStmt([VarDecl(IntType(), x = IntLiteral(3))])])])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_096():
    source = """
    int init() { return 0; }
    void main() {
        int a; int b; int c;
        a = b = c = init();
    }
    """
    expected = "Program([FuncDecl(IntType(), init, [], [ReturnStmt(return IntLiteral(0))]), FuncDecl(VoidType(), main, [], [VarDecl(IntType(), a), VarDecl(IntType(), b), VarDecl(IntType(), c), ExprStmt(AssignExpr(Identifier(a) = AssignExpr(Identifier(b) = AssignExpr(Identifier(c) = FuncCall(init, [])))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_097():
    source = """
    void main() {
        int i = 0;
        for (; i < 10; ) {
            i++;
        }
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], [VarDecl(IntType(), i = IntLiteral(0)), ForStmt(for None; BinaryOp(Identifier(i), <, IntLiteral(10)); None do BlockStmt([ExprStmt(PostfixOp(Identifier(i)++))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_098():
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
    expected = "Program([FuncDecl(VoidType(), main, [], [VarDecl(IntType(), code = IntLiteral(404)), SwitchStmt(switch Identifier(code) cases [CaseStmt(case IntLiteral(200): [ExprStmt(FuncCall(print, [StringLiteral('OK')])), BreakStmt()]), CaseStmt(case IntLiteral(404): [BlockStmt([VarDecl(StringType(), msg = StringLiteral('Not Found')), ExprStmt(FuncCall(print, [Identifier(msg)]))]), BreakStmt()])])])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_099():
    source = """
    void calculate() {
        float res = 3.14 * 2.0 * (15.5 - 4.2) / 3.0 + 7.5 % 2.0;
    }
    """
    expected = "Program([FuncDecl(VoidType(), calculate, [], [VarDecl(FloatType(), res = BinaryOp(BinaryOp(BinaryOp(BinaryOp(FloatLiteral(3.14), *, FloatLiteral(2.0)), *, BinaryOp(FloatLiteral(15.5), -, FloatLiteral(4.2))), /, FloatLiteral(3.0)), +, BinaryOp(FloatLiteral(7.5), %, FloatLiteral(2.0))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_100():
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
    expected = "Program([StructDecl(Date, [MemberDecl(IntType(), d), MemberDecl(IntType(), m), MemberDecl(IntType(), y)]), StructDecl(Student, [MemberDecl(IntType(), id), MemberDecl(FloatType(), gpa), MemberDecl(StructType(Date), dob)]), FuncDecl(VoidType(), processStudent, [Param(StructType(Student), s)], [IfStmt(if BinaryOp(MemberAccess(Identifier(s).gpa), >=, FloatLiteral(8.5)) then BlockStmt([ExprStmt(FuncCall(print, [StringLiteral('Excellent')]))]), else IfStmt(if BinaryOp(MemberAccess(Identifier(s).gpa), >=, FloatLiteral(7.0)) then BlockStmt([ExprStmt(FuncCall(print, [StringLiteral('Good')]))]), else BlockStmt([ExprStmt(FuncCall(print, [StringLiteral('Average')]))]))), WhileStmt(while BinaryOp(MemberAccess(Identifier(s).id), >, IntLiteral(0)) do BlockStmt([ExprStmt(AssignExpr(MemberAccess(Identifier(s).id) = BinaryOp(MemberAccess(Identifier(s).id), /, IntLiteral(10))))]))])])"
    assert str(ASTGenerator(source).generate()) == expected