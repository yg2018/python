#练习4
# 定义一个 Employee 雇员类，要求如下：
# (1) 属性有：id、name、salary
# (2) 运算符重载+：实现两个对象相加时，默认返回他们的薪水和
# (3) 构造方法要求：输入 name、salary，不输入 id。id 采用自增的方式，从 1000 开 始自增，第一个新增对象是 1001，第二个新增对象是 1002。
# (4) 根据 salary 属性，使用@property 设置属性的 get 和 set 方法。set 方法要求输 入：1000-50000 范围的数字。
class Employee:
    id=1000

    def __init__(self,name,salary):
        self.name=name
        self.__salary=salary

    @property
    def salary(self):
        return self.__salary;

    @salary.setter
    def salary(self,salary):
        if 1000<=salary<=50000:
            self.__salary=salary
        else:
            print("薪水录入错误，只能在1000-50000的范围内")

e=Employee("zhangsan",10)
print(e.salary)
