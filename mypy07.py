#字符串相关

#ord()函数
a="A"
print(ord(a))

#chr()函数
b=87
print(chr(b))

#空字符串和len()函数
c=''
print(len(c))
d="ashdbfha"
print(len(d))

#字符串拼接
#注：两边的类型要一致，不同则抛异常
a='a'+'b'
print(a)
#a=1+"a"
#print(a)
b='aaa''bbb'
print(b)

#字符串复制
a='a'*3
print(a)

#print函数 默认加一个换行符，可使用参数指定结束的字符
print('aaa',end='##')

print('aaa',end='')
print('aaa',end='')

#从控制台读取字符串
#myinput= input("请输入名字\n")
#print(myinput)

#str()函数 数字转字符串
a=5.20
print(str(a))
b=3.14e2
print(str(b))

#使用[]提取字符
a='abcdefghijklmnopqrstuvwxyz'
print(a)
##正向搜索
print(a[1])
print(a[4])
print(a[26-1])

##反向搜索
print(a[-1])
print(a[-10])
print(a[-26])

##索引越界
#print(a[30])

#replace()
##字符串是不可改变的
#a[1]='远
print(id(a))
a = a.replace('b','远')
print(a)
print(id(a))

#silce()字符串切片
a='abcdefghijklmnopqrstuvwxyz'
print(a[:])
print(a[2:])
print(a[:8])
print(a[2:5])
print(a[0:26:2])
print(a[-3:])
print(a[-8:-3])
print(a[::-1])

print("to be or not to be"[::-1])
print("sxtsxtsxtsxtsxt"[0:20:3])


#split() 默认空白字符（换行、空格、制表符）
print("to be or not to be".split())
print("to be or not to be".split("be"))

a=["sxt","sxt100","sxt200"]
print("*".join(a))

#测试拼接速度join（）较高

#仅包含下划线（_）、字母 和数字可以驻留
a="abc_33"
b="abc_33"
print( a is b)

c="dd#￥"
d="dd#￥"
print(c is d)
print(c is d)

#字符串比较和同一性 is/is not

#成员操作符 in/not in

#len(a)
#a.startwith("I")
#a.endwith("you")
#a.find("I")
#a.rfind("you")
#a.count("I")
#a.isalnum 是否全是字符或数字

#去除字符串首尾指定信息
#strip()
#lstrip()
#rstrip()

#大小写转换
#a.capitalize() 首字母大写
#a.title() 每个单子首字母大写
#a.upper() 字母大写
#a.lower() 字母小写
#a.swapcase() 大小写转换

#格式排版
#center() 居中
#ljust() 居左
#rjust() 居右

#其他方法
#isalnum() 是否为字母或数字
#isalpha 是否全为字母或汉字
#isdigit 是否全为数字
#isspace 是否空白符
#isupper 是否全为大写字母
#islower 是否全为小写字母

#format() 字符串格式化
a="名字是：{0}，年龄是：{1}"
print(a.format("袁葛",18))
print(a.format("yg",20))

a="名字是：{name}，年龄是：{age}"
print(a.format(age=20,name="ycl"))


#作业1
print("(5+10*x)/5-13*(y-1)(a+b)/x+9*(5/x+(12+x)/y)")

#作业2
salary=input("请输入月薪\n")
salary=int(salary)
print(salary*12)

#作业3
print("爱你一万年"*100) 

#作业4
print("to be or not to be"[::-1])

#作业5
a="sxt"*5
print(a[0:20:3])

#作业6
a="abc_33"
b="abc_33"

c="dd#"
d="dd#"
print( a is b)
print( c is d)







