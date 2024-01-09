#类属性 从属于类对象，所有对象共享
class Student():
    company='SXT' #类变量
    count=0 #类变量

    def __init__(self,name,score):
        self.name=name #实例属性
        self.score=score #实例属性
        Student.count+=1
        print(Student.count)

    def say_score(self):
        print("我的公司是{0}".format(Student.company))
        print("{0}的分数是{1}".format(self.name,self.score))

stu=Student('萧峰',300)
stu.say_score()
print(dir(stu))
stu2=Student('段誉',3000)
print(dir(stu2))
stu3=Student('虚竹',200)
print(dir(stu3))
