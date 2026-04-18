"""
Test cases for TyC Static Semantic Checker

This module contains test cases for the static semantic checker.
100 test cases covering all error types and comprehensive scenarios.
"""

from tests.utils import Checker
from src.utils.nodes import (
    Program,
    FuncDecl,
    BlockStmt,
    VarDecl,
    AssignExpr,
    ExprStmt,
    IntType,
    FloatType,
    StringType,
    VoidType,
    StructType,
    IntLiteral,
    FloatLiteral,
    StringLiteral,
    Identifier,
    BinaryOp,
    MemberAccess,
    FuncCall,
    StructDecl,
    MemberDecl,
    Param,
    ReturnStmt,
)


# ============================================================================
# Valid Programs (test_001 - test_020)
# ============================================================================


def test_001():
    """Test a valid program that should pass all checks"""
    source = """
void main() {
    int x = 5;
    int y = x + 1;
}
"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected


def test_002():
    """Test valid program with auto type inference"""
    source = """
void main() {
    auto x = 10;
    auto y = 3.14;
    auto z = x + y;
}
"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected


def test_003():
    """Test valid program with functions"""
    source = """
int add(int x, int y) {
    return x + y;
}
void main() {
    int sum = add(5, 3);
}
"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected


def test_004():
    """Test valid program with struct"""
    source = """
struct Point {
    int x;
    int y;
};
void main() {
    Point p;
    p.x = 10;
    p.y = 20;
}
"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected


def test_005():
    """Test valid program with nested blocks"""
    source = """
void main() {
    int x = 10;
    {
        int y = 20;
        int z = x + y;
    }
}
"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected



# ============================================================================
# Declare (test_021 - test_040)
# ============================================================================

def test_021():
    """Test error: Local variable reuses parameter name"""
    source = """
    void func(int x) {
        int x = 10; 
    }
    """
    # Cần check chính xác message từ file static_error.py
    expected = "Redeclared Variable: x" 
    assert Checker(source).check_from_source() == expected

# ============================================================================
# Control Flow (test_041 - test_050)
# ============================================================================

def test_041():
    """Test error: continue is not allowed in switch"""
    source = """
    void main() {
        int x = 1;
        switch(x) {
            case 1: continue;
        }
    }
    """
    expected = "MustInLoop: ContinueStmt()" # Dựa theo hàm __str__ của node
    assert Checker(source).check_from_source() == expected

# ============================================================================
# Type Mismatch Expression (test_051 - test_070)
# ============================================================================

def test_051():
    """Test error: Type mismatch in expression"""
    source = """
    void main() {
        int x = 5 + "hello";
    }
    """
    expected = "TypeMismatchInExpression: BinaryOp(IntLiteral(5), +, StringLiteral('hello'))"
    assert Checker(source).check_from_source() == expected


# ============================================================================
# Type Mismatch Statement (test_071 - test_085)
# ============================================================================



# ============================================================================
# Type Cannot Be Inferred (test_086 - test_100)
# ============================================================================

def test_086():
    """Test error: Type cannot be inferred for circular assignment"""
    source = """
    void main() {
        auto a; auto b;
        a = b;
    }
    """
    expected = "TypeCannotBeInferred: AssignExpr(Identifier(a) = Identifier(b))"
    assert Checker(source).check_from_source() == expected