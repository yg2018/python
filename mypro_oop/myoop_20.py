#测试MRO方法解析顺序
##如果父类中有相同名字的方法，在子类没有指定父类名时，解释器将 “从左向右”按顺序搜索
class A():
    def aa(self):
        print("aa")
    def say(self):
        print("say AA")
class B():
    def bb(self):
        print("bb")
    def say(self):
        print("say BB")
class C(A,B):
    pass

c=C()
c.say()