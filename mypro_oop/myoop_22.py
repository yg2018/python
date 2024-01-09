#测试多态
## 1. 多态是方法的多态，属性没有多态。
## 2. 多态的存在有 2 个必要条件：继承、方法重写。
class Animal():
    def shout(self):
        print("动物叫唤")

class Dog(Animal):
    def shout(self):
        print("小狗汪汪叫")

class Cat(Animal):
    def shout(self):
        print("小猫喵喵叫")

def AnimalShout(a):
    if isinstance(a,Animal):
        a.shout()

AnimalShout(Dog())
AnimalShout(Cat())