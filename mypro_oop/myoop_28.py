#测试设计模式--工厂模式+单例模式
##工厂模式实现了创建者和调用者的分离，使用专门的工厂类将选择实现类、创建对象进 行统一的管理和控制

class CarFactory:
    __obj=None
    __init_flag=True

    def __new__(cls, *args, **kwargs):
        if cls.__obj==None:
            cls.__obj=object.__new__(cls)
        return cls.__obj

    def __init__(self):
        if CarFactory.__init_flag:
            print("init...")
            CarFactory.__init_flag=False

    def createCar(self,brand):
        if brand=='奔驰':
            return Benz()
        elif brand=='宝马':
            return BMW()
        elif brand=='比亚迪':
            return BYD()
        else:
            return "未知品牌，无法创建"
class Benz:
    pass
class BMW:
    pass
class BYD:
    pass

factory=CarFactory()
factory2=CarFactory()
print(factory)
print(factory2)
c1=factory.createCar("奔驰")
c2=factory2.createCar("比亚迪")
print(c1)
print(c2)

