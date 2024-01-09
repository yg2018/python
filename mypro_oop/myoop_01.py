##函数的定义
class Student:
    def __init__(self,name,score):#构造方法
        self.name=name #实例属性
        self.score=score

    def say_score(self): #实例方法
        print("{0}的成绩是：{1}".format(self.name,self.score))

s=Student('yuange',100)
print("name=",s.name)
print("score=",s.score)
s.say_score()