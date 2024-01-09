##lambda表达式和匿名函数
### 1、生成一个函数对象
### 2、只能有一个表达式，计算结果是函数的返回值

f=lambda a,b,c:a+b+c
print(f)
print(f(1,2,3))

g=[lambda a:a*3,lambda b:b*4,lambda c:c*5]
print(g[0](20),g[1](20),g[2](20))