#循环结构

##while循环
num=0
while num<=10:
    print(num,end='\t')
    num=num+1
print()
print("*************************************************")

##计算1~100的累加和
num=0
sum=0
while num<=100:
    sum+=num;
    num+=1;
print("累加和是{0}".format(sum))

#for循环
for x in (100,200,300):
    print(x)

for x in 'abcd':
    print(x)

d={"name":"zhangsan","age":17,"sex":"nan"}

for x in d:
    print(x)

for x in d.keys():
    print(x)

for x in d.values():
    print(x)

for x in d.items():
    print(x)

##range对象
for x in range(5):
    print(x)

##嵌套循环
for x in range(5):
    for y in range(5):
        print(x,end='\t')
    print()

##九九乘法表
for x in range(1,10):
    for y in range(1,x+1):
        print("{0}*{1}={2}".format(x,y,x*y),end='\t')
    print()

##输出字典表格
d1={"name":"zhangsan","age":18,"salary":30000,"city":"济南"}
d2={"name":"lisi","age":17,"salary":20000,"city":"青岛"}
d3={"name":"wangwu","age":19,"salary":10000,"city":"烟台"}
l=[d1,d2,d3]
for x in l:
    if x.get("salary")>15000:
        print(x)

#break语句
while True:
    a=input("请输入字符，Q或q结束")
    if a=='q' or a=='Q':
        print("程序结束，退出")
        break
    else:
        print(a)

#continue语句


#循环语句的else语句
##while

##for




