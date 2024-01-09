##参数的类型

###位置参数
def fun1(a,b,c):
    print(a,b,c)
fun1(10,20,30)
####fun1(10,20)参数个数和位置和参数对象

###默认参数,传递则覆盖，不传递则使用默认值

def fun2(a,b,c=20,d=40):
    print(a,b,c,d)
fun2(10,20,40,60)
fun2(10,20)

###命名参数
def fun3(a,c,b):
    print(a,b,c)
fun3(c=10,b=20,a=30)

###可变参数
####一个星号，参数存于元组中
####多个星号，参数存于字典中
def fun4(a,b,*c):
    print(a,b,c)
    print(type(c))

fun4(10,20,30,40)

def fun5(a,b,**c):
    print(a,b,c)
    print(type(c))
fun5(10,20,c=30,d=40,e=50)




