#__del__析构方法和垃圾回收机制
##对象被销毁时所需的操作
##对象引用为0时，垃圾回收机制调用
##del 语句删除对象，也可以调用__del__方法
##一般不需要自定义

class Student():
    def __del__(self):
        print("销毁对象：{0}".format(self))

s1=Student()
s2=Student()
del s1
print("程序结束")



