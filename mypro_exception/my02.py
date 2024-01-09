#coding=utf-8
##循环输入数字，如果不是数字则处理异常；直到输入 88，则结束循环。
while True:
    try:
        num=int(input("请输入一个数字"))
        print("输入的数字是：",num)
        if num==88:
            print("程序结束")
            break
    except BaseException as e:
        print(e)
        print("输入的不是数字！")
