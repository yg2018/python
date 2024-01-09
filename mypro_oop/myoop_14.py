#测试继承
class Person():

    def __init__(self,name,age):
        print(self)
        self.name=name
        self.__age=age

    def say_age(self):

        print("我的年龄是:{0}".format(self.__age))

class Student(Person):
    def __init__(self,name,age,score):
        self.score=score
        Person.__init__(self,name,age)

p=Person("李四",29)
s1=Student("张三",18,99)
s1.say_age()
print(dir(s1))