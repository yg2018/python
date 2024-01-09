#查看继承结构mro()
class A():
    pass
class B(A):
    pass
class C(A):
    pass
class D(B,C):
    pass

d=D()
print(D.mro())