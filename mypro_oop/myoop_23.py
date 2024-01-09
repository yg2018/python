#特殊方法和运算符重载
##运算符实际上是通过调用对象的特殊方法实现的
a=20
b=30
c=a+b
d=a.__add__(b)
print(c)
print(d)

##重写特殊方法
class Person():
    def __init__(self,name):
        self.name=name

    def __add__(self, other):
        if isinstance(other,Person):
            return "{0}--{1}".format(self.name,other.name)
        else:
            return "不是同类对象，不能相加"

    def __mul__(self, other):
        if isinstance(other,int):
            return self.name*other
        else:
            return "不是同类，不能相乘"

p=Person("yuange")
p2=Person("yuanzhengzheng")
print(p+p2)
print(p*5)