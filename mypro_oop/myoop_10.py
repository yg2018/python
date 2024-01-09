#方法的动态性
##动态的添加方法
##动态的修改已有的方法

class Person():
    def work(self):
        print("努力工作！")

def play_game(self):
    print("{0}喜欢玩游戏".format(self))

def work2(self):
    print("好好努力，勇攀高峰!")

p=Person()
p.work()

Person.work=work2
Person.play=play_game
p.work()
p2=Person()
p2.work()
p2.play()