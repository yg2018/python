#私有属性和私有方法
##1、约定，两个下划线定义的属性或方法是私有的，其他的为公有的。
##2、类的内部可以访问私有属性（方法）
##3、类的外部不能访问私有属性（方法）
##4、类的外部可以通过_类名__属性（方法）访问私有属性或方法

class Employee():
    __company="HaiYi" #私有类属性

    def __init__(self,name,age):
        self.name=name
        self.__age=age #私有实例属性

    def say_hi(self):
        print("我的公司是",Employee.__company)
        print(self.name,"的年龄是{0}".format(self.__age))
        self.__work()

    def __work(self): #私有方法
        print("好好工作，天天向上，努力挣钱，摆脱贫困!")

e=Employee('yuange',18)
print(e.name)
##print(e.__age) 不能直接访问私有的实例属性
print(e._Employee__age) #通过这种方式可以直接访问到私有属 性 。通过 dir 可以查到属性：_Employee__age
print(dir(e))
e.say_hi()
e._Employee__work()

