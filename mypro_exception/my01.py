#coding=utf-8
##若被监控的语句有异常，则执行捕获异常的语句
try:
    print("step1")
    num=3/0
    print("step2")
except BaseException as e:
    print("step3")
    print(e)
print("step4")

print("*"*10)

##若被监控的语句无异常，则跳过捕获异常的语句
try:
    print("step1")
    #num=3/0
    print("step2")
except BaseException as e:
    print("step3")
    print(e)
print("step4")