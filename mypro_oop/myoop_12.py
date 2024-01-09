#@property装饰器
##将方法的调用方式变为“属性调用”

class Employee():

    @property
    def salary(self):
        return 30000;

e=Employee()
print(e.salary)
print(type(e.salary))
# e.salary() 'int' object is not callable

#e.salary=2000 # @property 修饰的属性，如果没有 加 setter 方法，则为只读属性 报错can't set attribute

class Employee2():

    def __init__(self,name,salary):
        self.name=name
        self.__salary=salary

    @property
    def salary(self):
        print("月薪为：{0}，年薪为：{1}".format(self.__salary,self.__salary*12))
        return self.__salary

    @salary.setter
    def salary(self,salary):
        if(0<salary<1000000):
            self.__salary=salary
        else:
            print("薪水录入错误！只能在 0-1000000 之间")

emp=Employee2("yuange",50000)
print(emp.salary)
emp.salary=30000
print(emp.salary)
emp.salary=-200