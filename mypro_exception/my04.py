#coding=utf-8
## try...except...else
try:
    a=input("输入被除数")
    b=input("输入除数")
    c=float(a)/float(b)
except BaseException as e:
    print(e)
else:
    print("结果是",c)