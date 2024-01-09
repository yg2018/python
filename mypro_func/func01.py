#1. 定义一个函数实现反响输出一个整数。比如：输入 3245，输出 5432.
# def func1(s):
#     return s[::-1]
#
# a='3245'
# print(func1(a))
#2. 编写一个函数.m(n)=1/2+2/3+...+n/n+1
# def m(n):
#     if n==1:
#         return n/(n+1)
#     else:
#         return (n/(n+1))+m(n-1)
# print(m(5))
#3. 输入三角形三个顶点的坐标，若有效则计算三角形的面积；如坐标无效，则给出提示。
import math

a=(10,10)
b=(20,20)
c=(10,20)

def isSjx(a,b,c):
    ab=math.sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)
    ac=math.sqrt((a[0]-c[0])**2+(a[1]-b[1])**2)
    bc=math.sqrt((b[0]-c[0])**2+(b[1]-c[1])**2)
    if (ab+ac)>bc and (ab+bc)>ac and (ac+bc)>ab:
        return True
    else:
        return False
print(isSjx(a,b,c))
#4. 输入一个毫秒数，将该数字换算成小时数，分钟数、秒数。
time=2533624226
print(type(time))

def convert_time(t):
    second=time//1000
    print("毫秒数",second)
    minute=second//60
    print("分钟数",minute)
    hour=minute//60
    print("小时数",hour)

convert_time(time)

#5. 使用海龟绘图。输入多个点，将这些点都两两相连。