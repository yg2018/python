#测试多重继承
##避免将结构搞的混乱，少使用
class AA():
    def aa(self):
        print("aa")
class BB():
    def bb(self):
        print("bb")
class CC(BB,AA):
    def cc(self):
        print("cc")

c=CC()
c.cc()
c.bb()
c.aa()