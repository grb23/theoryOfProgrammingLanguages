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

# Returns true when e1 and e2 are the same
def same(e1, e2):
    assert isinstance(e1, Expr)
    assert isinstance(e2, Expr)

    # All values not on the diagonal (quick reject)
    if type(e1) is not type(e2)
        return False

    if type(e1) is BoolExpr:
        return e1.value == e2.value

    if type(e1) is NotExpr:
        return same(e1.expr, e2.expr)

    if type(e1) is AndExpr:
        return same(e1.expr, e2.expr)
               same(e1.expr, e2.expr)

"""
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
"""

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

def step_not(e):
    if type(e) is NotExpr:
        # ----------------- Not-T
        # not true -> False
        #
        # ----------------- Not-F
        # not false -> true
        #
        # Alternative for above:
        #
        # -----------------
        # not v1 -> 'not [v1]'
        #
        #   e1 -> e1'
        # ----------------- Not-E
        # not e1 -> not e1'
        if is_value(e.expr):
            if e.expr.value == True: # not true
                return BoolExpr(False)
            else:
                return BoolExpr(True) # not false

        return Not(step(e.expr))

def step_and(e):
    # ---------------------- And-V
    # v1 and v2 -> '[v1] and [v2]'
    #       e1 -> e2
    # ---------------------- And-L
    #   e1 and e2 -> e1' and e2
    #       e2 -> e2'
    # ---------------------- And-L
    #   v1 and e2 -> v1 and e2'
    if is_value(e.lhs) and is_value(e.rhs):
        return BoolExpr(e.lhs.value and e.rhs.value)

    if is_reducible(e.lhs):
        return And(step(e.lhs), e.rhs)

    if is_reducible(e.rhs):
        return And(e.lhs, step(e.rhs))

    assert False

def step_or(e):
    # ---------------------- Or-V
    # v1 or v2 -> '[v1] or [v2]'
    #       e1 -> e2
    # ---------------------- Or-L
    #   e1 or e2 -> e1' or e2
    #       e2 -> e2'
    # ---------------------- Or-L
    #   v1 or e2 -> v1 or e2'
    if is_value(e.lhs) or is_value(e.rhs):
        return BoolExpr(e.lhs.value or e.rhs.value)

    if is_reducible(e.lhs):
        return Or(step(e.lhs), e.rhs)

    if is_reducible(e.rhs):
        return Or(e.lhs, step(e.rhs))

    assert False

# Compute the next step of the program
def step(e):
    """
    assert isinstance(e1, Expr)
    assert isinstance(op, Expr)
    assert isinstance(e2, Expr)
    exprResult = value(e1) and value(e2.expr)

    return exprResult and value(op)
    """
    # Not at bottom of tree
    assert is_reducible(e)

    if is_value(e.expr):
        if e.expr.value == True: # not true
            return BoolExpr(False)
        else:
            return BoolExpr(True) # not false

    return Not(step(e.expr))

def reduce(e1, e2):
    assert isinstance(e, Expr)

    while is_reducible(e)
        e = step(e)
    return e

return 0
