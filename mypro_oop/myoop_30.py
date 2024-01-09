#练习2
#使用工厂模式、单例模式实现如下需求：
# (1) 电脑工厂类 ComputerFactory 用于生产电脑 Computer。工厂类使用单例模式， 也就是说只能有一个工厂对象。
# (2) 工厂类中可以生产各种品牌的电脑：联想、华硕、神舟
# (3) 各种品牌的电脑使用继承实现：
# (4) 父类是 Computer 类，定义了 calculate 方法
# (5) 各品牌电脑类需要重写父类的 calculate 方法

class Computer:
    def calculate(self):
        pass
class LxComputer(Computer):
    def calculate(self):
        print("联想电脑正在计算。。。")

class HsComputer(Computer):
    def calculate(self):
        print("华硕电脑正在计算。。。")

class SzComputer(Computer):
    def calculate(self):
        print("神州电脑正在计算。。。")

class ComputerFactory:
    __obj=None
    __init_flag=True

    def __new__(cls, *args, **kwargs):
        if cls.__obj==None:
            cls.__obj=object.__new__(cls)
        return cls.__obj

    def __init__(self):
        if self.__init_flag:
            print("init...")
            self.__init_flag=False

    def createComputer(self,brand):
        if brand=='联想':
            return LxComputer()
        elif brand=='华硕':
            return HsComputer()
        elif brand=='神州':
            return SzComputer();
        else:
            print("无品牌，无法创建")
def computerWork(c):
    c.calculate();

factory=ComputerFactory()
factory2=ComputerFactory()
c1=factory.createComputer("联想")
c2=factory2.createComputer("华硕")
c3=factory.createComputer("神州")

computerWork(c1)
computerWork(c2)
computerWork(c3)

