#控制语句学习

##单分支结构

##多分支结构

##三元运算符
a=9
print(a if a<10 else '数值太大')

##多分支结构
score=int(input('请输入成绩'))
grade=''
if score<60:
    grade='不及格'
elif score<80:
    grade="及格"
elif score<90:
    grade="良好"
else:
    grade="优秀"
print("分数是{0}，成绩{1}".format(score,grade))

##练习1：输入一个分数。分数在 0-100 之间。90 以上是 A,80 以上是 B，70 以上是 C，60 以上是 D。60 以下是 E。
score=int(input('请输入您的分数'))
grade=''
if score<0 or score>100:
    print("请输入0~100的整数！")
else:
    if score>90:grade='A'
    elif score>80:grade='B'
    elif score>70:grade='C'
    elif score>60:grade="D"
    else:grade="E"
    print("分数是{0}，等级是{1}".format(score,grade))
print("************************************************")
degree="ABCDE"
if score<0 or score>100:
    print("请输入0~100的整数！")
else:
    num=score//10
    if num<6:
        num=5
    print("分数是{0}，等级是{1}".format(score, grade))