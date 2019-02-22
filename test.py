from ast import *


# \x.x
id = AbsExpr(VarDecl("x"), IdExpr("x"))

# id y

# true = \a.\b.a
t = AbsExpr("a", AbsExpr("b", "a"))

# false = \a.\b.b
f = AbsExpr("a", AbsExpr("b", "b"))

# and =
land = \
    AbsExpr("p",
        AbsExpr("q",
            AbsExpr(
                AppExpr(IdExpr("p"),
                IdExpr("q")),
                IdExpr("p"))))

e1 = AppExpr(land, t)
e1 = AppExpr(AppExpr(land, t), t)
resolve(e1)
print(t)
print(f)

print(land)
print(e1)
