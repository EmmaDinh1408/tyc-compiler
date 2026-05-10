"""
Test cases for TyC code generation.
"""

from src.utils.nodes import *
from tests.utils import CodeGenerator


def test_001():
    """Test 1: Hello World - print string"""
    ast = Program([
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                ExprStmt(FuncCall("printString", [StringLiteral("Hello World")]))
            ])
        )
    ])
    expected = "Hello World"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_002():
    """Test 2: Print integer"""
    ast = Program([
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                ExprStmt(FuncCall("printInt", [IntLiteral(42)]))
            ])
        )
    ])
    expected = "42"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_003():
    """Test 3: Print float"""
    ast = Program([
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                ExprStmt(FuncCall("printFloat", [FloatLiteral(3.14)]))
            ])
        )
    ])
    expected = "3.14"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_004():
    """Test 4: Variable declaration and assignment"""
    ast = Program([
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                VarDecl(IntType(), "x", IntLiteral(10)),
                ExprStmt(FuncCall("printInt", [Identifier("x")]))
            ])
        )
    ])
    expected = "10"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_005():
    """Test 5: Binary operation - addition"""
    ast = Program([
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                ExprStmt(FuncCall("printInt", [
                    BinaryOp(IntLiteral(5), "+", IntLiteral(3))
                ]))
            ])
        )
    ])
    expected = "8"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_006():
    """Test 6: Binary operation - multiplication"""
    ast = Program([
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                ExprStmt(FuncCall("printInt", [
                    BinaryOp(IntLiteral(6), "*", IntLiteral(7))
                ]))
            ])
        )
    ])
    expected = "42"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_007():
    """Test 7: If statement"""
    ast = Program([
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                IfStmt(
                    BinaryOp(IntLiteral(1), "<", IntLiteral(2)),
                    ExprStmt(FuncCall("printString", [StringLiteral("yes")])),
                    ExprStmt(FuncCall("printString", [StringLiteral("no")]))
                )
            ])
        )
    ])
    expected = "yes"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_008():
    """Test 8: While loop"""
    ast = Program([
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                VarDecl(IntType(), "i", IntLiteral(0)),
                WhileStmt(
                    BinaryOp(Identifier("i"), "<", IntLiteral(3)),
                    BlockStmt([
                        ExprStmt(FuncCall("printInt", [Identifier("i")])),
                        ExprStmt(AssignExpr(
                            Identifier("i"),
                            BinaryOp(Identifier("i"), "+", IntLiteral(1))
                        ))
                    ])
                )
            ])
        )
    ])
    expected = "012"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_009():
    """Test 9: Function call with return value"""
    ast = Program([
        FuncDecl(
            IntType(),
            "add",
            [Param(IntType(), "a"), Param(IntType(), "b")],
            BlockStmt([
                ReturnStmt(BinaryOp(Identifier("a"), "+", Identifier("b")))
            ])
        ),
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                ExprStmt(FuncCall("printInt", [
                    FuncCall("add", [IntLiteral(20), IntLiteral(22)])
                ]))
            ])
        )
    ])
    expected = "42"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_010():
    """Test 10: Multiple statements - arithmetic operations"""
    ast = Program([
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                VarDecl(IntType(), "x", IntLiteral(10)),
                VarDecl(IntType(), "y", IntLiteral(20)),
                ExprStmt(FuncCall("printInt", [
                    BinaryOp(Identifier("x"), "+", Identifier("y"))
                ]))
            ])
        )
    ])
    expected = "30"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_011():
    """Test 11: Float arithmetic - addition"""
    ast = Program([
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                ExprStmt(FuncCall("printFloat", [
                    BinaryOp(FloatLiteral(1.5), "+", FloatLiteral(2.5))
                ]))
            ])
        )
    ])
    expected = "4.0"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_012():
    """Test 12: Float arithmetic - subtraction"""
    ast = Program([
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                ExprStmt(FuncCall("printFloat", [
                    BinaryOp(FloatLiteral(5.5), "-", FloatLiteral(2.5))
                ]))
            ])
        )
    ])
    expected = "3.0"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_013():
    """Test 13: Float arithmetic - multiplication"""
    ast = Program([
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                ExprStmt(FuncCall("printFloat", [
                    BinaryOp(FloatLiteral(2.5), "*", FloatLiteral(4.0))
                ]))
            ])
        )
    ])
    expected = "10.0"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_014():
    """Test 14: Float arithmetic - division"""
    ast = Program([
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                ExprStmt(FuncCall("printFloat", [
                    BinaryOp(FloatLiteral(10.0), "/", FloatLiteral(2.0))
                ]))
            ])
        )
    ])
    expected = "5.0"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_015():
    """Test 15: Mixed int-float arithmetic"""
    ast = Program([
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                ExprStmt(FuncCall("printFloat", [
                    BinaryOp(IntLiteral(5), "+", FloatLiteral(2.5))
                ]))
            ])
        )
    ])
    expected = "7.5"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_016():
    """Test 16: Integer division"""
    ast = Program([
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                ExprStmt(FuncCall("printInt", [
                    BinaryOp(IntLiteral(10), "/", IntLiteral(3))
                ]))
            ])
        )
    ])
    expected = "3"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_017():
    """Test 17: Modulo operation"""
    ast = Program([
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                ExprStmt(FuncCall("printInt", [
                    BinaryOp(IntLiteral(10), "%", IntLiteral(3))
                ]))
            ])
        )
    ])
    expected = "1"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_018():
    """Test 18: Comparison - less than true"""
    ast = Program([
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                ExprStmt(FuncCall("printInt", [
                    BinaryOp(IntLiteral(3), "<", IntLiteral(5))
                ]))
            ])
        )
    ])
    expected = "1"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_019():
    """Test 19: Comparison - less than false"""
    ast = Program([
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                ExprStmt(FuncCall("printInt", [
                    BinaryOp(IntLiteral(5), "<", IntLiteral(3))
                ]))
            ])
        )
    ])
    expected = "0"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_020():
    """Test 20: Comparison - equal"""
    ast = Program([
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                ExprStmt(FuncCall("printInt", [
                    BinaryOp(IntLiteral(42), "==", IntLiteral(42))
                ]))
            ])
        )
    ])
    expected = "1"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_021():
    """Test 21: Comparison - not equal"""
    ast = Program([
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                ExprStmt(FuncCall("printInt", [
                    BinaryOp(IntLiteral(5), "!=", IntLiteral(3))
                ]))
            ])
        )
    ])
    expected = "1"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_022():
    """Test 22: Comparison - greater than"""
    ast = Program([
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                ExprStmt(FuncCall("printInt", [
                    BinaryOp(IntLiteral(5), ">", IntLiteral(3))
                ]))
            ])
        )
    ])
    expected = "1"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_023():
    """Test 23: Comparison - less or equal"""
    ast = Program([
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                ExprStmt(FuncCall("printInt", [
                    BinaryOp(IntLiteral(5), "<=", IntLiteral(5))
                ]))
            ])
        )
    ])
    expected = "1"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_024():
    """Test 24: Comparison - greater or equal"""
    ast = Program([
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                ExprStmt(FuncCall("printInt", [
                    BinaryOp(IntLiteral(5), ">=", IntLiteral(3))
                ]))
            ])
        )
    ])
    expected = "1"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_025():
    """Test 25: Complex expression - multiple operations"""
    ast = Program([
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                ExprStmt(FuncCall("printInt", [
                    BinaryOp(
                        BinaryOp(IntLiteral(2), "+", IntLiteral(3)),
                        "*",
                        IntLiteral(4)
                    )
                ]))
            ])
        )
    ])
    expected = "20"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_026():
    """Test 26: Complex expression - nested operations"""
    ast = Program([
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                ExprStmt(FuncCall("printInt", [
                    BinaryOp(
                        BinaryOp(IntLiteral(10), "-", IntLiteral(2)),
                        "/",
                        BinaryOp(IntLiteral(2), "+", IntLiteral(2))
                    )
                ]))
            ])
        )
    ])
    expected = "2"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_027():
    """Test 27: Variable assignment and modification"""
    ast = Program([
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                VarDecl(IntType(), "x", IntLiteral(5)),
                ExprStmt(AssignExpr(Identifier("x"), IntLiteral(10))),
                ExprStmt(FuncCall("printInt", [Identifier("x")]))
            ])
        )
    ])
    expected = "10"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_028():
    """Test 28: Variable assignment with expression"""
    ast = Program([
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                VarDecl(IntType(), "x", IntLiteral(5)),
                ExprStmt(AssignExpr(
                    Identifier("x"),
                    BinaryOp(Identifier("x"), "+", IntLiteral(3))
                )),
                ExprStmt(FuncCall("printInt", [Identifier("x")]))
            ])
        )
    ])
    expected = "8"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_029():
    """Test 29: Multiple variables"""
    ast = Program([
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                VarDecl(IntType(), "x", IntLiteral(10)),
                VarDecl(IntType(), "y", IntLiteral(20)),
                VarDecl(IntType(), "z", IntLiteral(30)),
                ExprStmt(FuncCall("printInt", [
                    BinaryOp(
                        BinaryOp(Identifier("x"), "+", Identifier("y")),
                        "+",
                        Identifier("z")
                    )
                ]))
            ])
        )
    ])
    expected = "60"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_030():
    """Test 30: Float variables"""
    ast = Program([
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                VarDecl(FloatType(), "x", FloatLiteral(1.5)),
                VarDecl(FloatType(), "y", FloatLiteral(2.5)),
                ExprStmt(FuncCall("printFloat", [
                    BinaryOp(Identifier("x"), "+", Identifier("y"))
                ]))
            ])
        )
    ])
    expected = "4.0"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_031():
    """Test 31: If statement - else branch"""
    ast = Program([
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                IfStmt(
                    BinaryOp(IntLiteral(5), "<", IntLiteral(3)),
                    ExprStmt(FuncCall("printString", [StringLiteral("yes")])),
                    ExprStmt(FuncCall("printString", [StringLiteral("no")]))
                )
            ])
        )
    ])
    expected = "no"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_032():
    """Test 32: If statement - without else"""
    ast = Program([
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                IfStmt(
                    BinaryOp(IntLiteral(1), "<", IntLiteral(2)),
                    ExprStmt(FuncCall("printString", [StringLiteral("yes")])),
                    None
                )
            ])
        )
    ])
    expected = "yes"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_033():
    """Test 33: If statement - complex condition"""
    ast = Program([
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                VarDecl(IntType(), "x", IntLiteral(10)),
                IfStmt(
                    BinaryOp(Identifier("x"), ">", IntLiteral(5)),
                    ExprStmt(FuncCall("printString", [StringLiteral("big")])),
                    ExprStmt(FuncCall("printString", [StringLiteral("small")]))
                )
            ])
        )
    ])
    expected = "big"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_034():
    """Test 34: Nested if statements"""
    ast = Program([
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                VarDecl(IntType(), "x", IntLiteral(10)),
                VarDecl(IntType(), "y", IntLiteral(5)),
                IfStmt(
                    BinaryOp(Identifier("x"), ">", IntLiteral(5)),
                    IfStmt(
                        BinaryOp(Identifier("y"), "<", IntLiteral(10)),
                        ExprStmt(FuncCall("printString", [StringLiteral("yes")])),
                        ExprStmt(FuncCall("printString", [StringLiteral("no")]))
                    ),
                    ExprStmt(FuncCall("printString", [StringLiteral("false")]))
                )
            ])
        )
    ])
    expected = "yes"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_035():
    """Test 35: While loop - multiple iterations"""
    ast = Program([
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                VarDecl(IntType(), "i", IntLiteral(0)),
                VarDecl(IntType(), "sum", IntLiteral(0)),
                WhileStmt(
                    BinaryOp(Identifier("i"), "<", IntLiteral(5)),
                    BlockStmt([
                        ExprStmt(AssignExpr(
                            Identifier("sum"),
                            BinaryOp(Identifier("sum"), "+", Identifier("i"))
                        )),
                        ExprStmt(AssignExpr(
                            Identifier("i"),
                            BinaryOp(Identifier("i"), "+", IntLiteral(1))
                        ))
                    ])
                ),
                ExprStmt(FuncCall("printInt", [Identifier("sum")]))
            ])
        )
    ])
    expected = "10"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_036():
    """Test 36: While loop - factorial calculation"""
    ast = Program([
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                VarDecl(IntType(), "n", IntLiteral(5)),
                VarDecl(IntType(), "result", IntLiteral(1)),
                WhileStmt(
                    BinaryOp(Identifier("n"), ">", IntLiteral(1)),
                    BlockStmt([
                        ExprStmt(AssignExpr(
                            Identifier("result"),
                            BinaryOp(Identifier("result"), "*", Identifier("n"))
                        )),
                        ExprStmt(AssignExpr(
                            Identifier("n"),
                            BinaryOp(Identifier("n"), "-", IntLiteral(1))
                        ))
                    ])
                ),
                ExprStmt(FuncCall("printInt", [Identifier("result")]))
            ])
        )
    ])
    expected = "120"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_037():
    """Test 37: Nested while loops"""
    ast = Program([
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                VarDecl(IntType(), "i", IntLiteral(0)),
                VarDecl(IntType(), "count", IntLiteral(0)),
                WhileStmt(
                    BinaryOp(Identifier("i"), "<", IntLiteral(2)),
                    BlockStmt([
                        VarDecl(IntType(), "j", IntLiteral(0)),
                        WhileStmt(
                            BinaryOp(Identifier("j"), "<", IntLiteral(3)),
                            BlockStmt([
                                ExprStmt(AssignExpr(
                                    Identifier("count"),
                                    BinaryOp(Identifier("count"), "+", IntLiteral(1))
                                )),
                                ExprStmt(AssignExpr(
                                    Identifier("j"),
                                    BinaryOp(Identifier("j"), "+", IntLiteral(1))
                                ))
                            ])
                        ),
                        ExprStmt(AssignExpr(
                            Identifier("i"),
                            BinaryOp(Identifier("i"), "+", IntLiteral(1))
                        ))
                    ])
                ),
                ExprStmt(FuncCall("printInt", [Identifier("count")]))
            ])
        )
    ])
    expected = "6"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_038():
    """Test 38: If-while combination"""
    ast = Program([
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                VarDecl(IntType(), "x", IntLiteral(10)),
                IfStmt(
                    BinaryOp(Identifier("x"), ">", IntLiteral(5)),
                    BlockStmt([
                        VarDecl(IntType(), "i", IntLiteral(0)),
                        WhileStmt(
                            BinaryOp(Identifier("i"), "<", IntLiteral(3)),
                            BlockStmt([
                                ExprStmt(FuncCall("printInt", [Identifier("i")])),
                                ExprStmt(AssignExpr(
                                    Identifier("i"),
                                    BinaryOp(Identifier("i"), "+", IntLiteral(1))
                                ))
                            ])
                        )
                    ]),
                    None
                )
            ])
        )
    ])
    expected = "012"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_039():
    """Test 39: Function with no parameters"""
    ast = Program([
        FuncDecl(
            IntType(),
            "getValue",
            [],
            BlockStmt([
                ReturnStmt(IntLiteral(42))
            ])
        ),
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                ExprStmt(FuncCall("printInt", [FuncCall("getValue", [])]))
            ])
        )
    ])
    expected = "42"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_040():
    """Test 40: Function with multiple return paths"""
    ast = Program([
        FuncDecl(
            IntType(),
            "max",
            [Param(IntType(), "a"), Param(IntType(), "b")],
            BlockStmt([
                IfStmt(
                    BinaryOp(Identifier("a"), ">", Identifier("b")),
                    ReturnStmt(Identifier("a")),
                    ReturnStmt(Identifier("b"))
                )
            ])
        ),
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                ExprStmt(FuncCall("printInt", [
                    FuncCall("max", [IntLiteral(15), IntLiteral(8)])
                ]))
            ])
        )
    ])
    expected = "15"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_041():
    """Test 41: Function with float return"""
    ast = Program([
        FuncDecl(
            FloatType(),
            "average",
            [Param(FloatType(), "a"), Param(FloatType(), "b")],
            BlockStmt([
                ReturnStmt(BinaryOp(
                    BinaryOp(Identifier("a"), "+", Identifier("b")),
                    "/",
                    FloatLiteral(2.0)
                ))
            ])
        ),
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                ExprStmt(FuncCall("printFloat", [
                    FuncCall("average", [FloatLiteral(5.0), FloatLiteral(3.0)])
                ]))
            ])
        )
    ])
    expected = "4.0"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_042():
    """Test 42: Function with void return"""
    ast = Program([
        FuncDecl(
            VoidType(),
            "printTwice",
            [Param(IntType(), "x")],
            BlockStmt([
                ExprStmt(FuncCall("printInt", [Identifier("x")])),
                ExprStmt(FuncCall("printInt", [Identifier("x")]))
            ])
        ),
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                ExprStmt(FuncCall("printTwice", [IntLiteral(5)]))
            ])
        )
    ])
    expected = "55"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_043():
    """Test 43: Recursive function - fibonacci"""
    ast = Program([
        FuncDecl(
            IntType(),
            "fib",
            [Param(IntType(), "n")],
            BlockStmt([
                IfStmt(
                    BinaryOp(Identifier("n"), "<=", IntLiteral(1)),
                    ReturnStmt(Identifier("n")),
                    ReturnStmt(BinaryOp(
                        FuncCall("fib", [BinaryOp(Identifier("n"), "-", IntLiteral(1))]),
                        "+",
                        FuncCall("fib", [BinaryOp(Identifier("n"), "-", IntLiteral(2))])
                    ))
                )
            ])
        ),
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                ExprStmt(FuncCall("printInt", [FuncCall("fib", [IntLiteral(6)])]))
            ])
        )
    ])
    expected = "8"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_044():
    """Test 44: Multiple function calls in sequence"""
    ast = Program([
        FuncDecl(
            IntType(),
            "add",
            [Param(IntType(), "a"), Param(IntType(), "b")],
            BlockStmt([
                ReturnStmt(BinaryOp(Identifier("a"), "+", Identifier("b")))
            ])
        ),
        FuncDecl(
            IntType(),
            "multiply",
            [Param(IntType(), "a"), Param(IntType(), "b")],
            BlockStmt([
                ReturnStmt(BinaryOp(Identifier("a"), "*", Identifier("b")))
            ])
        ),
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                ExprStmt(FuncCall("printInt", [
                    FuncCall("multiply", [
                        FuncCall("add", [IntLiteral(2), IntLiteral(3)]),
                        IntLiteral(4)
                    ])
                ]))
            ])
        )
    ])
    expected = "20"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_045():
    """Test 45: String variable declaration"""
    ast = Program([
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                VarDecl(StringType(), "msg", StringLiteral("Hello")),
                ExprStmt(FuncCall("printString", [Identifier("msg")]))
            ])
        )
    ])
    expected = "Hello"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_046():
    """Test 46: String assignment"""
    ast = Program([
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                VarDecl(StringType(), "msg", StringLiteral("Hello")),
                ExprStmt(AssignExpr(Identifier("msg"), StringLiteral("World"))),
                ExprStmt(FuncCall("printString", [Identifier("msg")]))
            ])
        )
    ])
    expected = "World"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_047():
    """Test 47: Auto type inference - integer"""
    ast = Program([
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                VarDecl(None, "x", IntLiteral(42)),
                ExprStmt(FuncCall("printInt", [Identifier("x")]))
            ])
        )
    ])
    expected = "42"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_048():
    """Test 48: Auto type inference - float"""
    ast = Program([
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                VarDecl(None, "x", FloatLiteral(3.14)),
                ExprStmt(FuncCall("printFloat", [Identifier("x")]))
            ])
        )
    ])
    expected = "3.14"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_049():
    """Test 49: Auto type inference - string"""
    ast = Program([
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                VarDecl(None, "msg", StringLiteral("test")),
                ExprStmt(FuncCall("printString", [Identifier("msg")]))
            ])
        )
    ])
    expected = "test"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_050():
    """Test 50: Block scope - variable shadowing"""
    ast = Program([
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                VarDecl(IntType(), "x", IntLiteral(10)),
                BlockStmt([
                    VarDecl(IntType(), "x", IntLiteral(20)),
                    ExprStmt(FuncCall("printInt", [Identifier("x")]))
                ]),
                ExprStmt(FuncCall("printInt", [Identifier("x")]))
            ])
        )
    ])
    expected = "2010"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_051():
    """Test 51: Zero value"""
    ast = Program([
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                ExprStmt(FuncCall("printInt", [IntLiteral(0)]))
            ])
        )
    ])
    expected = "0"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_052():
    """Test 52: Negative numbers"""
    ast = Program([
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                ExprStmt(FuncCall("printInt", [IntLiteral(-42)]))
            ])
        )
    ])
    expected = "-42"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_053():
    """Test 53: Large numbers"""
    ast = Program([
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                ExprStmt(FuncCall("printInt", [IntLiteral(1000000)]))
            ])
        )
    ])
    expected = "1000000"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_054():
    """Test 54: Float precision"""
    ast = Program([
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                ExprStmt(FuncCall("printFloat", [FloatLiteral(0.1)]))
            ])
        )
    ])
    expected = "0.1"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_055():
    """Test 55: Empty string"""
    ast = Program([
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                ExprStmt(FuncCall("printString", [StringLiteral("")]))
            ])
        )
    ])
    expected = ""
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_056():
    """Test 56: Function with three parameters"""
    ast = Program([
        FuncDecl(
            IntType(),
            "sum3",
            [Param(IntType(), "a"), Param(IntType(), "b"), Param(IntType(), "c")],
            BlockStmt([
                ReturnStmt(BinaryOp(
                    BinaryOp(Identifier("a"), "+", Identifier("b")),
                    "+",
                    Identifier("c")
                ))
            ])
        ),
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                ExprStmt(FuncCall("printInt", [
                    FuncCall("sum3", [IntLiteral(10), IntLiteral(20), IntLiteral(30)])
                ]))
            ])
        )
    ])
    expected = "60"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_057():
    """Test 057: Struct Declaration and Basic Usage"""
    ast = Program([
        StructDecl("Point", [
            MemberDecl(IntType(), "x"),
            MemberDecl(IntType(), "y")
        ]),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(StructType("Point"), "p", None),
            ExprStmt(AssignExpr(MemberAccess(Identifier("p"), "x"), IntLiteral(10))),
            ExprStmt(AssignExpr(MemberAccess(Identifier("p"), "y"), IntLiteral(20))),
            ExprStmt(FuncCall("printInt", [MemberAccess(Identifier("p"), "x")])),
            ExprStmt(FuncCall("printInt", [MemberAccess(Identifier("p"), "y")]))
        ]))
    ])
    expected = "1020"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

def test_058():
    """Test 58: Power calculation - 2^10"""
    ast = Program([
        FuncDecl(
            IntType(),
            "power",
            [Param(IntType(), "base"), Param(IntType(), "exp")],
            BlockStmt([
                VarDecl(IntType(), "result", IntLiteral(1)),
                VarDecl(IntType(), "i", IntLiteral(0)),
                WhileStmt(
                    BinaryOp(Identifier("i"), "<", Identifier("exp")),
                    BlockStmt([
                        ExprStmt(AssignExpr(
                            Identifier("result"),
                            BinaryOp(Identifier("result"), "*", Identifier("base"))
                        )),
                        ExprStmt(AssignExpr(
                            Identifier("i"),
                            BinaryOp(Identifier("i"), "+", IntLiteral(1))
                        ))
                    ])
                ),
                ReturnStmt(Identifier("result"))
            ])
        ),
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                ExprStmt(FuncCall("printInt", [
                    FuncCall("power", [IntLiteral(2), IntLiteral(10)])
                ]))
            ])
        )
    ])
    expected = "1024"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_059():
    """Test 59: Bubble sort - sorting array via variables"""
    ast = Program([
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                VarDecl(IntType(), "a", IntLiteral(3)),
                VarDecl(IntType(), "b", IntLiteral(1)),
                VarDecl(IntType(), "c", IntLiteral(2)),
                VarDecl(IntType(), "temp", IntLiteral(0)),
                IfStmt(
                    BinaryOp(Identifier("a"), ">", Identifier("b")),
                    BlockStmt([
                        ExprStmt(AssignExpr(Identifier("temp"), Identifier("a"))),
                        ExprStmt(AssignExpr(Identifier("a"), Identifier("b"))),
                        ExprStmt(AssignExpr(Identifier("b"), Identifier("temp")))
                    ]),
                    None
                ),
                IfStmt(
                    BinaryOp(Identifier("b"), ">", Identifier("c")),
                    BlockStmt([
                        ExprStmt(AssignExpr(Identifier("temp"), Identifier("b"))),
                        ExprStmt(AssignExpr(Identifier("b"), Identifier("c"))),
                        ExprStmt(AssignExpr(Identifier("c"), Identifier("temp")))
                    ]),
                    None
                ),
                IfStmt(
                    BinaryOp(Identifier("a"), ">", Identifier("b")),
                    BlockStmt([
                        ExprStmt(AssignExpr(Identifier("temp"), Identifier("a"))),
                        ExprStmt(AssignExpr(Identifier("a"), Identifier("b"))),
                        ExprStmt(AssignExpr(Identifier("b"), Identifier("temp")))
                    ]),
                    None
                ),
                ExprStmt(FuncCall("printInt", [Identifier("a")])),
                ExprStmt(FuncCall("printInt", [Identifier("b")])),
                ExprStmt(FuncCall("printInt", [Identifier("c")]))
            ])
        )
    ])
    expected = "123"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_060():
    """Test 60: GCD - greatest common divisor"""
    ast = Program([
        FuncDecl(
            IntType(),
            "gcd",
            [Param(IntType(), "a"), Param(IntType(), "b")],
            BlockStmt([
                WhileStmt(
                    BinaryOp(Identifier("b"), "!=", IntLiteral(0)),
                    BlockStmt([
                        VarDecl(IntType(), "temp", Identifier("b")),
                        ExprStmt(AssignExpr(
                            Identifier("b"),
                            BinaryOp(Identifier("a"), "%", Identifier("b"))
                        )),
                        ExprStmt(AssignExpr(Identifier("a"), Identifier("temp")))
                    ])
                ),
                ReturnStmt(Identifier("a"))
            ])
        ),
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                ExprStmt(FuncCall("printInt", [
                    FuncCall("gcd", [IntLiteral(48), IntLiteral(18)])
                ]))
            ])
        )
    ])
    expected = "6"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_061():
    """Test 061: Struct Literal Initialization"""
    ast = Program([
        StructDecl("Point", [
            MemberDecl(IntType(), "x"),
            MemberDecl(IntType(), "y")
        ]),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(StructType("Point"), "p", StructLiteral([IntLiteral(30), IntLiteral(40)])),
            ExprStmt(FuncCall("printInt", [MemberAccess(Identifier("p"), "x")])),
            ExprStmt(FuncCall("printInt", [MemberAccess(Identifier("p"), "y")]))
        ]))
    ])
    expected = "3040"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

def test_062():
    """Test 62: Complex arithmetic with proper precedence"""
    ast = Program([
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                ExprStmt(FuncCall("printInt", [
                    BinaryOp(
                        BinaryOp(IntLiteral(2), "+", IntLiteral(3)),
                        "*",
                        BinaryOp(IntLiteral(4), "-", IntLiteral(1))
                    )
                ]))
            ])
        )
    ])
    expected = "15"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_063():
    """Test 63: Float variable in calculations"""
    ast = Program([
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                VarDecl(FloatType(), "pi", FloatLiteral(3.14)),
                VarDecl(FloatType(), "radius", FloatLiteral(2.0)),
                ExprStmt(FuncCall("printFloat", [
                    BinaryOp(pi := Identifier("pi"), "*", BinaryOp(Identifier("radius"), "*", Identifier("radius")))
                ]))
            ])
        )
    ])
    expected = "12.56"
    result = CodeGenerator().generate_and_run(ast)


def test_064():
    """Test 064: Switch-Case Basic (with Break)"""
    ast = Program([
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(IntType(), "x", IntLiteral(2)),
            SwitchStmt(Identifier("x"), [
                CaseStmt(IntLiteral(1), [ExprStmt(FuncCall("printInt", [IntLiteral(10)])), BreakStmt()]),
                CaseStmt(IntLiteral(2), [ExprStmt(FuncCall("printInt", [IntLiteral(20)])), BreakStmt()])
            ], DefaultStmt([ExprStmt(FuncCall("printInt", [IntLiteral(30)]))]))
        ]))
    ])
    expected = "20"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

def test_065():
    """Test 065: Switch-Case Fallthrough and Default"""
    ast = Program([
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(IntType(), "x", IntLiteral(1)),
            SwitchStmt(Identifier("x"), [
                CaseStmt(IntLiteral(1), [ExprStmt(FuncCall("printInt", [IntLiteral(10)]))]), # no break!
                CaseStmt(IntLiteral(2), [ExprStmt(FuncCall("printInt", [IntLiteral(20)])), BreakStmt()])
            ], DefaultStmt([ExprStmt(FuncCall("printInt", [IntLiteral(30)]))]))
        ]))
    ])
    expected = "1020"  
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

def test_066():
    """Test 66: Print mixed types"""
    ast = Program([
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                ExprStmt(FuncCall("printString", [StringLiteral("a")])),
                ExprStmt(FuncCall("printInt", [IntLiteral(1)])),
                ExprStmt(FuncCall("printString", [StringLiteral("b")]))
            ])
        )
    ])
    expected = "a1b"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_067():
    """Test 67: While loop with zero iterations"""
    ast = Program([
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                VarDecl(IntType(), "i", IntLiteral(0)),
                WhileStmt(
                    BinaryOp(Identifier("i"), "<", IntLiteral(0)),
                    BlockStmt([
                        ExprStmt(FuncCall("printInt", [Identifier("i")])),
                        ExprStmt(AssignExpr(
                            Identifier("i"),
                            BinaryOp(Identifier("i"), "+", IntLiteral(1))
                        ))
                    ])
                ),
                ExprStmt(FuncCall("printString", [StringLiteral("done")]))
            ])
        )
    ])
    expected = "done"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_068():
    """Test 68: If statement with variable condition"""
    ast = Program([
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                VarDecl(IntType(), "x", IntLiteral(1)),
                IfStmt(
                    Identifier("x"),
                    ExprStmt(FuncCall("printString", [StringLiteral("yes")])),
                    ExprStmt(FuncCall("printString", [StringLiteral("no")]))
                )
            ])
        )
    ])
    expected = "yes"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_069():
    """Test 69: Else-if using nested if"""
    ast = Program([
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                VarDecl(IntType(), "x", IntLiteral(5)),
                IfStmt(
                    BinaryOp(Identifier("x"), "<", IntLiteral(0)),
                    ExprStmt(FuncCall("printString", [StringLiteral("negative")])),
                    IfStmt(
                        BinaryOp(Identifier("x"), "==", IntLiteral(0)),
                        ExprStmt(FuncCall("printString", [StringLiteral("zero")])),
                        ExprStmt(FuncCall("printString", [StringLiteral("positive")]))
                    )
                )
            ])
        )
    ])
    expected = "positive"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_070():
    """Test 70: Multiple assignments in sequence"""
    ast = Program([
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                VarDecl(IntType(), "x", IntLiteral(1)),
                VarDecl(IntType(), "y", IntLiteral(2)),
                ExprStmt(AssignExpr(Identifier("x"), IntLiteral(10))),
                ExprStmt(AssignExpr(Identifier("y"), IntLiteral(20))),
                ExprStmt(FuncCall("printInt", [
                    BinaryOp(Identifier("x"), "+", Identifier("y"))
                ]))
            ])
        )
    ])
    expected = "30"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_071():
    """Test 071: Break and Continue in For Loop"""
    ast = Program([
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ForStmt(
                VarDecl(IntType(), "i", IntLiteral(0)),
                BinaryOp(Identifier("i"), "<", IntLiteral(5)),
                AssignExpr(Identifier("i"), BinaryOp(Identifier("i"), "+", IntLiteral(1))),
                BlockStmt([
                    IfStmt(BinaryOp(Identifier("i"), "==", IntLiteral(2)), ContinueStmt(), None),
                    IfStmt(BinaryOp(Identifier("i"), "==", IntLiteral(4)), BreakStmt(), None),
                    ExprStmt(FuncCall("printInt", [Identifier("i")]))
                ])
            )
        ]))
    ])
    expected = "013" 
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

def test_072():
    """Test 072: Logical AND / OR (Short-circuit Evaluation)"""
    ast = Program([
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("printInt", [BinaryOp(IntLiteral(1), "||", IntLiteral(0))])),
            ExprStmt(FuncCall("printInt", [BinaryOp(IntLiteral(0), "&&", IntLiteral(1))])),
            ExprStmt(FuncCall("printInt", [BinaryOp(IntLiteral(1), "&&", IntLiteral(1))]))
        ]))
    ])
    expected = "101"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

def test_073():
    """Test 073: Unary NOT and Minus"""
    ast = Program([
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("printInt", [PrefixOp("!", IntLiteral(1))])),
            ExprStmt(FuncCall("printInt", [PrefixOp("!", IntLiteral(0))])),
            ExprStmt(FuncCall("printInt", [PrefixOp("-", IntLiteral(5))]))
        ]))
    ])
    expected = "01-5"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

def test_074():
    """Test 074: Struct Member Increment/Decrement"""
    ast = Program([
        StructDecl("Point", [MemberDecl(IntType(), "x")]),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(StructType("Point"), "p", StructLiteral([IntLiteral(10)])),
            ExprStmt(PostfixOp("++", MemberAccess(Identifier("p"), "x"))),
            ExprStmt(FuncCall("printInt", [MemberAccess(Identifier("p"), "x")]))
        ]))
    ])
    expected = "11"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

def test_075():
    """Test 75: Return value used in expression"""
    ast = Program([
        FuncDecl(
            IntType(),
            "getValue",
            [],
            BlockStmt([
                ReturnStmt(IntLiteral(10))
            ])
        ),
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                ExprStmt(FuncCall("printInt", [
                    BinaryOp(FuncCall("getValue", []), "+", IntLiteral(5))
                ]))
            ])
        )
    ])
    expected = "15"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_076():
    """Test 076: Chained Assignment and Assignment as Expression"""
    ast = Program([
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(IntType(), "a", IntLiteral(0)),
            VarDecl(IntType(), "b", IntLiteral(0)),
            VarDecl(IntType(), "c", IntLiteral(0)),
            ExprStmt(AssignExpr(Identifier("a"), AssignExpr(Identifier("b"), AssignExpr(Identifier("c"), IntLiteral(5))))),
            ExprStmt(FuncCall("printInt", [Identifier("a")])),
            ExprStmt(FuncCall("printInt", [Identifier("b")])),
            ExprStmt(FuncCall("printInt", [Identifier("c")])),
            VarDecl(IntType(), "d", BinaryOp(AssignExpr(Identifier("a"), IntLiteral(2)), "+", IntLiteral(3))),
            ExprStmt(FuncCall("printInt", [Identifier("d")]))
        ]))
    ])
    expected = "5555" 
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

def test_077():
    """Test 77: While with early variable initialization"""
    ast = Program([
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                VarDecl(IntType(), "x", IntLiteral(5)),
                VarDecl(IntType(), "sum", IntLiteral(0)),
                WhileStmt(
                    BinaryOp(Identifier("x"), ">", IntLiteral(0)),
                    BlockStmt([
                        ExprStmt(AssignExpr(
                            Identifier("sum"),
                            BinaryOp(Identifier("sum"), "+", Identifier("x"))
                        )),
                        ExprStmt(AssignExpr(
                            Identifier("x"),
                            BinaryOp(Identifier("x"), "-", IntLiteral(1))
                        ))
                    ])
                ),
                ExprStmt(FuncCall("printInt", [Identifier("sum")]))
            ])
        )
    ])
    expected = "15"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_078():
    """Test 78: Function called multiple times"""
    ast = Program([
        FuncDecl(
            IntType(),
            "double",
            [Param(IntType(), "x")],
            BlockStmt([
                ReturnStmt(BinaryOp(Identifier("x"), "*", IntLiteral(2)))
            ])
        ),
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                ExprStmt(FuncCall("printInt", [FuncCall("double", [IntLiteral(5)])])),
                ExprStmt(FuncCall("printInt", [FuncCall("double", [IntLiteral(10)])]))
            ])
        )
    ])
    expected = "1020"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_079():
    """Test 79: Nested function calls"""
    ast = Program([
        FuncDecl(
            IntType(),
            "add",
            [Param(IntType(), "a"), Param(IntType(), "b")],
            BlockStmt([
                ReturnStmt(BinaryOp(Identifier("a"), "+", Identifier("b")))
            ])
        ),
        FuncDecl(
            IntType(),
            "triple",
            [Param(IntType(), "x")],
            BlockStmt([
                ReturnStmt(BinaryOp(Identifier("x"), "*", IntLiteral(3)))
            ])
        ),
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                ExprStmt(FuncCall("printInt", [
                    FuncCall("triple", [
                        FuncCall("add", [IntLiteral(2), IntLiteral(3)])
                    ])
                ]))
            ])
        )
    ])
    expected = "15"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_080():
    """Test 80: Variable scope across functions"""
    ast = Program([
        FuncDecl(
            IntType(),
            "getConstant",
            [],
            BlockStmt([
                VarDecl(IntType(), "value", IntLiteral(42)),
                ReturnStmt(Identifier("value"))
            ])
        ),
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                VarDecl(IntType(), "result", FuncCall("getConstant", [])),
                ExprStmt(FuncCall("printInt", [Identifier("result")]))
            ])
        )
    ])
    expected = "42"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_081():
    """Test 81: For loop statement"""
    ast = Program([
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(IntType(), "sum", IntLiteral(0)),
            ForStmt(
                VarDecl(IntType(), "i", IntLiteral(1)),
                BinaryOp(Identifier("i"), "<=", IntLiteral(3)),
                AssignExpr(Identifier("i"), BinaryOp(Identifier("i"), "+", IntLiteral(1))),
                BlockStmt([
                    ExprStmt(AssignExpr(Identifier("sum"), BinaryOp(Identifier("sum"), "+", Identifier("i"))))
                ])
            ),
            ExprStmt(FuncCall("printInt", [Identifier("sum")]))
        ]))
    ])
    expected = "6"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

def test_082():
    """Test 82: Postfix and Prefix operators"""
    ast = Program([
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(IntType(), "x", IntLiteral(5)),
            ExprStmt(FuncCall("printInt", [PostfixOp("++", Identifier("x"))])), 
            ExprStmt(FuncCall("printInt", [PrefixOp("++", Identifier("x"))]))  
        ]))
    ])
    expected = "57"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

def test_083():
    """Test 083: Nested Structs and Member Access"""
    ast = Program([
        StructDecl("Inner", [MemberDecl(IntType(), "v")]),
        StructDecl("Outer", [MemberDecl(StructType("Inner"), "in")]),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(StructType("Outer"), "o", StructLiteral([StructLiteral([IntLiteral(77)])])),
            ExprStmt(FuncCall("printInt", [MemberAccess(MemberAccess(Identifier("o"), "in"), "v")]))
        ]))
    ])
    expected = "77"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

def test_084():
    """Test 084: Auto Type Inference with Structs"""
    ast = Program([
        StructDecl("Data", [MemberDecl(IntType(), "val")]),
        FuncDecl(StructType("Data"), "getData", [], BlockStmt([
            ReturnStmt(StructLiteral([IntLiteral(99)]))
        ])),
        FuncDecl(VoidType(), "main", [], BlockStmt([
            VarDecl(None, "d", FuncCall("getData", [])),
            ExprStmt(FuncCall("printInt", [MemberAccess(Identifier("d"), "val")]))
        ]))
    ])
    expected = "99"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

def test_085():
    """Test 085: Unary Plus Operator"""
    ast = Program([
        FuncDecl(VoidType(), "main", [], BlockStmt([
            ExprStmt(FuncCall("printInt", [PrefixOp("+", IntLiteral(42))]))
        ]))
    ])
    expected = "42"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

def test_086():
    """Test 86: Complex condition in if"""
    ast = Program([
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                VarDecl(IntType(), "age", IntLiteral(25)),
                IfStmt(
                    BinaryOp(
                        BinaryOp(Identifier("age"), ">=", IntLiteral(18)),
                        ">",
                        IntLiteral(0)
                    ),
                    ExprStmt(FuncCall("printString", [StringLiteral("adult")])),
                    ExprStmt(FuncCall("printString", [StringLiteral("minor")]))
                )
            ])
        )
    ])
    expected = "adult"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_087():
    """Test 87: Print float - integer value"""
    ast = Program([
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                ExprStmt(FuncCall("printFloat", [FloatLiteral(5.0)]))
            ])
        )
    ])
    expected = "5.0"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_088():
    """Test 88: String with spaces"""
    ast = Program([
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                ExprStmt(FuncCall("printString", [StringLiteral("Hello World")]))
            ])
        )
    ])
    expected = "Hello World"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_089():
    """Test 89: Sum of sequence"""
    ast = Program([
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                VarDecl(IntType(), "sum", IntLiteral(0)),
                VarDecl(IntType(), "i", IntLiteral(1)),
                WhileStmt(
                    BinaryOp(Identifier("i"), "<=", IntLiteral(10)),
                    BlockStmt([
                        ExprStmt(AssignExpr(
                            Identifier("sum"),
                            BinaryOp(Identifier("sum"), "+", Identifier("i"))
                        )),
                        ExprStmt(AssignExpr(
                            Identifier("i"),
                            BinaryOp(Identifier("i"), "+", IntLiteral(1))
                        ))
                    ])
                ),
                ExprStmt(FuncCall("printInt", [Identifier("sum")]))
            ])
        )
    ])
    expected = "55"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_090():
    """Test 90: Float division precision"""
    ast = Program([
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                ExprStmt(FuncCall("printFloat", [
                    BinaryOp(FloatLiteral(1.0), "/", FloatLiteral(3.0))
                ]))
            ])
        )
    ])
    expected = "0.33333334"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_091():
    """Test 91: Combination of if and while"""
    ast = Program([
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                VarDecl(IntType(), "x", IntLiteral(0)),
                VarDecl(IntType(), "total", IntLiteral(0)),
                WhileStmt(
                    BinaryOp(Identifier("x"), "<", IntLiteral(5)),
                    BlockStmt([
                        IfStmt(
                            BinaryOp(Identifier("x"), "!=", IntLiteral(0)),
                            ExprStmt(AssignExpr(
                                Identifier("total"),
                                BinaryOp(Identifier("total"), "+", Identifier("x"))
                            )),
                            None
                        ),
                        ExprStmt(AssignExpr(
                            Identifier("x"),
                            BinaryOp(Identifier("x"), "+", IntLiteral(1))
                        ))
                    ])
                ),
                ExprStmt(FuncCall("printInt", [Identifier("total")]))
            ])
        )
    ])
    expected = "10"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_092():
    """Test 92: Multiple nested blocks"""
    ast = Program([
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                BlockStmt([
                    BlockStmt([
                        ExprStmt(FuncCall("printString", [StringLiteral("nested")]))
                    ])
                ])
            ])
        )
    ])
    expected = "nested"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_093():
    """Test 93: Function returning void"""
    ast = Program([
        FuncDecl(
            VoidType(),
            "printHello",
            [],
            BlockStmt([
                ExprStmt(FuncCall("printString", [StringLiteral("hello")]))
            ])
        ),
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                ExprStmt(FuncCall("printHello", [])),
                ExprStmt(FuncCall("printHello", []))
            ])
        )
    ])
    expected = "hellohello"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_094():
    """Test 94: Parameter shadowing"""
    ast = Program([
        FuncDecl(
            IntType(),
            "test",
            [Param(IntType(), "x")],
            BlockStmt([
                VarDecl(IntType(), "x", IntLiteral(10)),
                ReturnStmt(Identifier("x"))
            ])
        ),
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                ExprStmt(FuncCall("printInt", [
                    FuncCall("test", [IntLiteral(5)])
                ]))
            ])
        )
    ])
    expected = "10"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_095():
    """Test 95: Swap values using temporary"""
    ast = Program([
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                VarDecl(IntType(), "a", IntLiteral(5)),
                VarDecl(IntType(), "b", IntLiteral(10)),
                VarDecl(IntType(), "temp", IntLiteral(0)),
                ExprStmt(AssignExpr(Identifier("temp"), Identifier("a"))),
                ExprStmt(AssignExpr(Identifier("a"), Identifier("b"))),
                ExprStmt(AssignExpr(Identifier("b"), Identifier("temp"))),
                ExprStmt(FuncCall("printInt", [Identifier("a")])),
                ExprStmt(FuncCall("printInt", [Identifier("b")]))
            ])
        )
    ])
    expected = "105"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_096():
    """Test 96: LCM calculation"""
    ast = Program([
        FuncDecl(
            IntType(),
            "gcd",
            [Param(IntType(), "a"), Param(IntType(), "b")],
            BlockStmt([
                WhileStmt(
                    BinaryOp(Identifier("b"), "!=", IntLiteral(0)),
                    BlockStmt([
                        VarDecl(IntType(), "temp", Identifier("b")),
                        ExprStmt(AssignExpr(
                            Identifier("b"),
                            BinaryOp(Identifier("a"), "%", Identifier("b"))
                        )),
                        ExprStmt(AssignExpr(Identifier("a"), Identifier("temp")))
                    ])
                ),
                ReturnStmt(Identifier("a"))
            ])
        ),
        FuncDecl(
            IntType(),
            "lcm",
            [Param(IntType(), "a"), Param(IntType(), "b")],
            BlockStmt([
                ReturnStmt(BinaryOp(
                    BinaryOp(Identifier("a"), "*", Identifier("b")),
                    "/",
                    FuncCall("gcd", [Identifier("a"), Identifier("b")])
                ))
            ])
        ),
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                ExprStmt(FuncCall("printInt", [
                    FuncCall("lcm", [IntLiteral(12), IntLiteral(18)])
                ]))
            ])
        )
    ])
    expected = "36"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_097():
    """Test 97: Print countdown"""
    ast = Program([
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                VarDecl(IntType(), "i", IntLiteral(5)),
                WhileStmt(
                    BinaryOp(Identifier("i"), ">", IntLiteral(0)),
                    BlockStmt([
                        ExprStmt(FuncCall("printInt", [Identifier("i")])),
                        ExprStmt(AssignExpr(
                            Identifier("i"),
                            BinaryOp(Identifier("i"), "-", IntLiteral(1))
                        ))
                    ])
                )
            ])
        )
    ])
    expected = "54321"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_098():
    """Test 98: Alternating operations"""
    ast = Program([
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                ExprStmt(FuncCall("printInt", [
                    BinaryOp(IntLiteral(10), "-", BinaryOp(IntLiteral(3), "+", IntLiteral(2)))
                ]))
            ])
        )
    ])
    expected = "5"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_099():
    """Test 99: Incremental sum"""
    ast = Program([
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                VarDecl(IntType(), "sum", IntLiteral(0)),
                ExprStmt(AssignExpr(Identifier("sum"), BinaryOp(Identifier("sum"), "+", IntLiteral(1)))),
                ExprStmt(FuncCall("printInt", [Identifier("sum")])),
                ExprStmt(AssignExpr(Identifier("sum"), BinaryOp(Identifier("sum"), "+", IntLiteral(2)))),
                ExprStmt(FuncCall("printInt", [Identifier("sum")])),
                ExprStmt(AssignExpr(Identifier("sum"), BinaryOp(Identifier("sum"), "+", IntLiteral(3)))),
                ExprStmt(FuncCall("printInt", [Identifier("sum")]))
            ])
        )
    ])
    expected = "136"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_100():
    """Test 100: Comprehensive program"""
    ast = Program([
        FuncDecl(
            IntType(),
            "isEven",
            [Param(IntType(), "n")],
            BlockStmt([
                ReturnStmt(BinaryOp(
                    BinaryOp(Identifier("n"), "%", IntLiteral(2)),
                    "==",
                    IntLiteral(0)
                ))
            ])
        ),
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                VarDecl(IntType(), "count", IntLiteral(0)),
                VarDecl(IntType(), "i", IntLiteral(1)),
                WhileStmt(
                    BinaryOp(Identifier("i"), "<=", IntLiteral(10)),
                    BlockStmt([
                        IfStmt(
                            FuncCall("isEven", [Identifier("i")]),
                            BlockStmt([
                                ExprStmt(AssignExpr(
                                    Identifier("count"),
                                    BinaryOp(Identifier("count"), "+", IntLiteral(1))
                                )),
                                ExprStmt(FuncCall("printInt", [Identifier("i")]))
                            ]),
                            None
                        ),
                        ExprStmt(AssignExpr(
                            Identifier("i"),
                            BinaryOp(Identifier("i"), "+", IntLiteral(1))
                        ))
                    ])
                ),
                ExprStmt(FuncCall("printInt", [Identifier("count")]))
            ])
        )
    ])
    expected = "246810" + "5"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"