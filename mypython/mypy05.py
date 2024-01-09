#练习

##1、安装 Pycharm 开发环境，并使用图文描述整个过程。
##傻瓜式安装，可用破解补丁

##2. 输入一个学生的成绩，将其转化成简单描述：不及格(小于 60)、及格(60-79)、良好 (80-89)、优秀(90-100)
# score=int(input("请输入你的成绩"))
# grade=''
# if score<60:
#     grade="不及格"
# elif score<80:
#     grade="及格"
# elif score<90:
#     grade="良好"
# else:
#     grade="优秀"
# print("你的分数是{0}，等级为{1}".format(score,grade))

##3. 已知点的坐标(x,y)，判断其所在的象限
# x=int(input("请输入横坐标x"))
# y=int(input("请输入纵坐标y"))
# if x==0 and y==0:
#     print("坐标为原点")
# elif x==0:
#     print("坐标在x轴上")
# elif y==0:
#     print("坐标在y轴上")
# elif x>0 and y>0:
#     print("坐标在第一象限")
# elif x>0 and y<0:
#     print("坐标在第四象限")
# elif x<0 and y>0:
#     print("坐标在第二象限")
# elif x<0 and y<0:
#     print("坐标在第三象限")

##4.输入一个分数。分数在 0-100 之间。90 以上是 A,80 以上是 B，70 以上是 C，60 以上 是 D。60 以下是 E
# score=int(input("请输入你的分数"))
# degree='ABCDE'
# grade=''
# if score<0 or score>100:
#     print("请输入1~100的整数")
# else:
#     num=score//10
#     if num<5:
#         num=5
#     grade=degree[9-num]
# print("你的分数是{0}，等级为{1}".format(score,grade))

##5. 利用 while 循环，计算 1-100 之间数字的累加和；计算 1-100 之间偶数的累加和，计算 1-100 之间奇数的累加和
# sum=0
# odd_sum=0
# even_sum=0
# i=0
# while i<101:
#     sum += i
#     if i%2==0:
#         even_sum += i
#     else:
#         odd_sum += i
#     i+=1
# print("1~100的和是{0}".format(sum))
# print("1~100的奇数和是{0}".format(odd_sum))
# print("1~100的偶数和是{0}".format(even_sum))
##6. 利用 for 循环，计算 1-100 之间数字的累加和；计算 1-100 之间偶数的累加和，计算 1-100 之间奇数的累加和
# sum_all=0
# sum_odd=0
# sum_even=0
# for j in range(1,101):
#     sum_all+=j
#     if j%2==0:
#         sum_even+=j
#     else:
#         sum_odd+=j
# print("1~100的和是{0}".format(sum_all))
# print("1~100的奇数和是{0}".format(sum_odd))
# print("1~100的偶数和是{0}".format(sum_even))

##7. 打印如下图案0 0 0 0 0 1 1 1 1 1 2 2 2 2 2 3 3 3 3 3 4 4 4 4 4
# for i in range(5):
#     for j in range(5):
#         print(i,end="\t")
#     print()
##8. 利用嵌套循环打印九九乘法表
# for m in range(1,10):
#     for n in range(1,m):
#         print("{0}*{1}={2}".format(m,n,m*n),end="\t")
#     print()
##9. 用列表和字典存储下表信息，并打印出表中工资高于 15000 的数据
# d1={"name":"Jack","age":19,"salary":30000}
# d2={"name":"Tom","age":38,"salary":20000}
# d3={"name":"Jerry","age":55,"salary":10000}
# list=[d1,d2,d3]
# for i in list:
#     if i.get("salary")>15000:
#         print(i)
##10. 要求输入员工的薪资，若薪资小于 0 则重新输入。最后打印出录入员工的数量和薪资明细，以及平均薪资
# salarys=[]
# salary_sum=0;
# while True:
#     salary=input("请输入你的薪资(q或Q结束)")
#     if salary.upper()=='Q':
#         print("录入完成，程序退出")
#         break
#     salary=float(salary)
#     if salary<0:
#         continue
#     salarys.append(salary)
#     salary_sum+=salary
#
# print("员工数{0}".format(len(salarys)))
# print(salarys)
# print("平均薪资{0}".format(float(salary_sum/len(salarys))))
##11. 员工一共 4 人。录入这 4 位员工的薪资。全部录入后，打印提示“您已经全部录入 4 名员工的薪资”。最后，打印输出录入的薪资和平均薪资
# sala_sum=0
# sala_list=[]
# for i in range(4):
#     sala=input("请输入薪资，Q或q中途退出")
#     if sala.upper()=='Q':
#         break
#     sala=float(sala)
#     sala_sum+=sala
#     sala_list.append(sala)
# else:
#     print("四名员工薪资已全部录入完成")
# print(sala_list)
# print(sala_sum/len(sala_list))

##12. 使用海龟绘图，绘制同心圆
# import turtle
# t=turtle.Pen()
# colors=["yellow","red","blue","green"]
# t.width(3)
# t.speed(1)
# for x in range(1,10):
#     t.penup()
#     t.goto(0, (-10 * x))
#     t.pendown()
#     t.color(colors[x%len(colors)])
#     t.circle(15+x*10)
# turtle.done()

##13. 使用海龟绘图，绘制 18*18 的棋盘
import turtle
t=turtle.Pen();

width=30
num=18

point1=[(-400,400),(-400+width*num,400)]
point2=[(-400,400),(-400,400-width*num)]

t.speed(10)

for i in range(19):
    t.penup()
    t.goto(point1[0][0],point1[0][1]-30*i)
    t.pendown()
    t.goto(point1[1][0],point1[1][1]-30*i)

for i in range(19):
    t.penup()
    t.goto(point2[0][0]+30*i,point2[0][1])
    t.pendown()
    t.goto(point2[1][0]+30*i,point2[1][1])

turtle.done()