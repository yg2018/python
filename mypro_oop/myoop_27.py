#测试设计模式--单例模式
class MySingleton:
    __obj=None
    __init_flag=True

    def __new__(cls, *args, **kwargs):
        if cls.__obj==None:
            cls.__obj=object.__new__(cls)
        return cls.__obj

    def __init__(self,name):
        if MySingleton.__init_flag:
            print("init...")
            self.__obj.name=name
            MySingleton.__init_flag=False

s=MySingleton("ming")
s2=MySingleton("liang")
s3=MySingleton("ge")
print(s)
print(s2)
print(s3)
