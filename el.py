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

    if value(e1) != value(e2)
        return False

    return True

def value(e):
    assert isinstance(e, Expr)

    if type(e) is BoolExpr:
        return 1

    if type(e) is NotExpr:
        return not value(e.expr)

    if type(e) is AndExpr:
        return value(e.lhs) and value(e.rhs)

    if type(e) is OrExpr:
        return value(e.lhs) or value(e.rhs)

def step(e):
    return

def reduce(e1, e2):
    return

def searchTree(e):
    return

return 0
