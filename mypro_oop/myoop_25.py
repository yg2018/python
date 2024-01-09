#浅拷贝和深拷贝
##浅拷贝 拷贝时，对象包含的子对象内容不拷贝
##深拷贝 使用 copy 模块的 deepcopy 函数，递归拷贝对象中包含的子对象。源对象和拷贝对象 所有的子对象也不同

import copy

class MobilePhone:
    def __init__(self,cpu,screen):
        self.cpu=cpu
        self.screen=screen

class Cpu:
    def calulate(self):
        print("计算个12345")
        print("CPU对象：",self)
class Screen:
    def show(self):
        print("显示一个好看的画面")
        print("Screen对象：",self)

m=MobilePhone(Cpu(),Screen())
m.cpu.calulate()
m.screen.show()

n=m
print(m,n)

m2=copy.copy(m)
print(m,m2)

m3=copy.deepcopy(m)
print(m2,m3)
