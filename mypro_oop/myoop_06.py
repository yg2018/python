#静态方法
##与类对象无关
##与普通函数没区别，但需要类名调用
##不能访问实例属性和实例方法

class Student():
    company="HaiYi"

    def __init__(self,name,score):
        self.name=name
        self.score=score

    @staticmethod
    def add(a,b):
        #print(company)
        return a+b

print(Student.add(10,20))