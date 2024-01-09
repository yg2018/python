#类方法
## 从属于类对象，所有对象共同拥有
## @classmethod装饰器修饰
## 类名.类方法名（参数列表）
## 不能访问实例属性和实例方法
## 子类继承父类，cls传入的是子类对象

class Student():
    company='HaiYi'

    # @classmethod
    # def say_company(cls):
    #     print("我的公司是{0}".format(cls.company))
    @classmethod
    def say_company(cls):
        print("我的公司是{0}".format(cls.company))

print(Student.say_company())