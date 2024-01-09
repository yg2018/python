#测试super()
## 代表父类的定义，不是父类对象
class AA():
    def say(self):
        print("A:",self)
        print("say AAA")

class BB(AA):
    def say(self):
        #AA.say(self)
        super().say()
        print("say BBB")

b=BB()
b.say()