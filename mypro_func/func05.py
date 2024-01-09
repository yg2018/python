##传递参数

##可变对象（列表、字典、其他自定义的对象）
a=[10,20]
def fun1(n):
    print(id(n))
    n.append(30)
    print(n)
print(id(a))
print(a)
fun1(a)
print(a)


##不可变对象引用（int、float、字符串、元组、布尔值）
a=100
def func02(m):
    print("m:",id(m))
    m=200
    print("m:",id(m))
func02(a)
print("a:",id(a))




