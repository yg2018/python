#特殊属性
class A():
    pass
class B():
    pass
class C(A,B):
    def __init__(self,nn):
        self.nn=nn
    def cc(self):
        print("cc")

c=C("ss")
print(dir(c))
print(c.__class__)
print(C.__bases__)
print(C.mro())
print(A.__subclasses__())
print(dir(A))