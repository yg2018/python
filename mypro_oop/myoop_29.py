#练习
##1.定义发动机类 Motor、底盘类 Chassis、座椅类 Seat，车辆外壳类 Shell，并使用组合 关系定义汽车类。
## 其他要求如下：
## 定义汽车的 run()方法，里面需要调用 Motor 类的 work()方法，
## 也需要调用座椅 类 Seat 的 work()方法，
## 也需要调用底盘类 Chassis 的 work()方法。
class Motor:
    def work(self):
        print("发动机正在工作。。。")

class Chassis:
    def work(self):
        print("车辆外壳正在工作。。。")

class Seat:
    def work(self):
        print("座椅正在工作。。。")

class Shell:
    pass

class Car:
    def __init__(self,motor,chassis,seat,shell):
        self.motor=motor
        self.chassis=chassis
        self.seat=seat
        self.shell=shell

    def run(self):
        self.motor.work()
        self.chassis.work()
        self.seat.work()

c=Car(Motor(),Chassis(),Seat(),Shell())
c.run()