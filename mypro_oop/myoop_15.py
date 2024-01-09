#测试重写方法
class Person():
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def say_name(self):
        print("我是"+self.name)

    def say_age(self):
        print("我的年龄是"+self.age)

class Student(Person):
    def __init__(self,name,age,score):
        self.score=score
        Person.__init__(self,name,age)
    def say_name(self):
        print("报告老师，我是{0}".format(self.name))

s=Student("小明",5,99)
s.say_name()