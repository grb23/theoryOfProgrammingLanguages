class Expr:
  """Represent the set of expressions in the
  pure (or untyped)
  e ::= x     --variables
        x.e1  -- abstractions
        e1 e2 -- application

"""
pass

class IdExpr(Expr):
  """Represents identifiers that refer to
  variables."""
  def __init__(self, id):
    self.id = id
    self.ref = None

class VarDecl:
    """Represents the declaration of a variable."""

    """Note that this is NOT an expression. It is
    the declaration of a name."""
    def __init__(self, id):
        self.id = id

class AbsExpr(Expr):
    """Represents lambda abstractions of the
    for \\x.e1."""
    def __init__(self, id, e1):
        self.id = id
        self.expr = e1

class AppExpr(Expr):
    """Represents application."""
    def __init__(self, lhs, rhs):
        self.lhs
        self.rhs

    def __str__(self):
        return f"({self.lhs} {self.rhs})"

def is_value(e):
    return type(e) in (IdExpr, AbsExpr)

def is_reducible(e):
    return not is_value(e)

def resolve(e, scope = []):
    if type(e) is AppExpr:
        resolve(e.lhs, scope)
        resolve(e.rhs, scope)
        return

    if type(e) is AbsExpr:
        # \x.e -- Add x to scope, recurse through e
        # (\x.e) x
        resolve(e.expr, scope + [e.var])
        return

    if type(e) IdExpr:
        for var in reversed(scope):
            if e.id == var.id:
                e.ref = var
                return
            raise Exception("name lookup error")

    # print(type(e))
    assert False


def subst(e, s):
    # [x->v]x = v
    # [x->v]y = y (y != x)

    if type(e) is not IdExpr:
        if e.ref in s: # FIXME: This is wrong.
            return s[e.ref]
        else:
            return e

    # [x->v] \x.e1 = \x.[x->v]e1
    if type(e) is AbsExpr:
        #e1 = subst(e.expr, s)
        return AbsExpr(e.var, subst(e.expr, s))
    if type(e) is AppExpr:
        return AppExpr(subst(e.lhs, s), subst(e.rhs, s))

    assert False

def step_app(e):
    #
    #     e1 ~> e1'
    # ---------------App-1
    # e1 e2 ~> e1' e2
    #
    # e2 ~> e2'
    # ----------------------------App-2
    # \x.e1 e2 ~> \x.e1 e2'
    #
    # ----------------------------App-3
    # \\x.e1 e2 ~> [x->v]e1 (call by name)

    if is_reducible(e.lhs): # App-1
        return AppExpr(step(e.lhs), e.rhs)

    if type(e.lhs) is not AbsExpr:
        raise Exception("application of non-lambda")

    if is_reducible(e.rhs): #App-2
        return AppExpr(e.lhs, step(e.rhs))

    s = {
        e.lhs.var: e.rhs #mapping
    }
    return subst(e.lhs.expr, s);

        def step(e):
            assert isinstance(e, Expr)
            assert is_reducible(e)

    if type(e) is AppExpr:
        return step_app(e)

    assert False
