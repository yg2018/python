##测试局部变量和全局变量的效率
###局部变量效率较高

import math
import time

def globalFun():
    start=time.time()
    for i in range(100000):
        math.sqrt(30)

    end=time.time()
    print('全局变量耗时',end-start)

def localFun():
    start=time.time()
    b=math.sqrt
    for i in range(100000):
        b(30)
    end=time.time()
    print('局部变量耗时',end-start)

globalFun()
localFun()