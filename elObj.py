# Gwendolyn Brunot
# grb23@zips.uakron.edu
# The University of Akron - Theory of Programming Languages
# Project 2 - Expression Language

class Expr:
    """Defines the following language
      e ::= true | false | not e1 | e1 and e2 | e1 or e2"""
      pass

class BoolExpr(Expr):
    """Represents the strings true and false"""
    def __init__(self, val):
        assert val == True or val == False
        self.value = val

class NotExpr(Expr):
    """Represents strings of the form 'not e'"""
    def __init__(self, e):
        assert isinstance(e, Expr)
        self.expr = e

class BinaryExpr(Expr):
    """Represents string of the form 'e1 @ e2'"""
    def __init__(self, e1, e2)
        assert isinstance(e1, Expr)
        assert isinstance(e2, Expr)
        self.lhs = e1
        self.rhs = e2

class AndExpr(BinaryExpr):
    """Represents string of the form 'e1 and e2'"""
        assert isinstance(e1, Expr)
        assert isinstance(e2, Expr)
        self.lhs = e1
        self.rhs = e2

class OrExpr(BinaryExpr):
    """Represents string of the form 'e1 or e2'"""
        assert isinstance(e1, Expr)
        assert isinstance(e2, Expr)
        self.lhs = e1
        self.rhs = e2
