class D:
    pass
class E:
    pass
class F:
    pass
class B(D,E):
    pass
class C(D,F):
    pass
class A(B,C):
    pass

print(D.mro())
print(E.mro())
print(F.mro())
print(B.mro())
print(A.mro())
