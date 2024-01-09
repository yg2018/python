#测试object根类
class Person():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def say_age(self):
        print(self.name,"的年龄是",self.age)

obj=object()
print(dir(obj))
p=Person("张三",13)
print(dir(p))