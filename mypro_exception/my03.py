#coding=utf-8
## try...多个except

try:
    a=input("输入被除数")
    b=input("输入除数")
    c=float(a)/float(b)
except ZeroDivisionError:
    print("除数不能为0")
except ValueError:
     print("异常：除数和被除数都应该为数值类型")
except BaseException as e:
    print(e)
    print(type(e))
