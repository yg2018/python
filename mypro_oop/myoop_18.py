#重写__str__()方法
class Person():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return "{0}的年龄是{1}".format(self.name,self.age)

p=Person("xiaoming",12)
print(p)
