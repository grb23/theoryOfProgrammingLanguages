# Gwendolyn Brunot
# grb23@zips.uakron.edu
# The University of Akron - Theory of Programming Languages
# Project 2 - Expression Language

# size -- compute the size of an expression
# height -- compute the height of an expression
# same -- Return true if two expressions are identical
# value -- compute the value of an expression
# step -- Return an expression representing a single step of evaluation
# reduce -- Calls step repeatedly until the expression is non-reducible

from el import *

class expr:
    pass

def size(e):
    assert isinstance(e, Expr)

    if type(e) is BoolExpr:
        return 1

    if type(e) is NotExpr:
        return 1 + size(e.expr)

    if isinstance(e, BinaryExpr):
        return 1 + size(e.lhs) + size(e.rhs)

def height(e):
    assert isinstance(e, Expr)

    if type(e) is BoolExpr:
        return 1

    if type(e) is NotExpr:
        return 1 + height(e.expr)

    if isinstance(e, BinaryExpr):
        return 1 + height(e.lhs) + height(e.rhs)

def same(e1, e2):
    assert isinstance(e1, Expr)
    assert isinstance(e2, Expr)

    if isinstance(e1, BinaryExpr) and is isinstance(e2, BinaryExpr):
        return e1.value == e2.value

    if isinstance(e1, BoolExpr) and isinstance(e2, BoolExpr):
        return e1.expr == e2.expr

    if isinstance(e1, NotExpr) and isinstance(e2, NotExpr):
        return e1.expr == e2.expr

    if isinstance(e1, AndExpr) and isinstance(e2, AndExpr):
        return e1.lhs == e2.rhs

    if isinstance(e1, OrExpr) and isinstance(e2, OrExpr):
        return e1.lhs == e2.rhs

    else
        return False

def value(e):
    assert isinstance(e, Expr)

    if type(e) is BoolExpr:
        return value(e.value)

    if type(e) is NotExpr:
        return not value(e.expr)

    if type(e) is AndExpr:
        return value(e.lhs) and value(e.rhs)

    if type(e) is OrExpr:
        return value(e.lhs) or value(e.rhs)

def step(e1, op, e2):
    assert isinstance(e1, Expr)
    assert isinstance(e2, Expr)
    assert isinstance(e, Expr)

    exprResult = value(e1) and value(e2.expr)

    return exprResult and value(op)

def reduce(e1, e2):
    assert isinstance(e, Expr)

    return

return 0
