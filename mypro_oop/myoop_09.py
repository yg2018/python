#方法没有重载
##不要使用重名的方法
##如果重名，后面的方法会覆盖前面的方法，只有最后一个才是有效的

class Person():

    def say_hi(self,a,b):
        print("hello...",a,b)

    def say_hi(self):
        print("say_hi...")

p=Person()
#p.say_hi("aaa","bbb")
p.say_hi()

