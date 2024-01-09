#序列推导式
##列表推导式
y=[x for x in range(1,5)]
print(y)

y=[x for x in range(1,5) if x%2==0]
print(y)

y=[x*2 for x in range(1,5)]
print(y)

str="abcdefg"
chars=[a for a in str]
print(chars)

cells=[(row,col) for row in range(5) for col in range(10)]
print(cells)

##字典推导式
###统计字符出现的次数
str="i love you, i love sxt, i love gaoqi"
char_count={c:str.count(c) for c in str}
print(char_count)

##集合推导式
sets={x for x in range(1,100) if x%9==0}
print(sets)

##生成器推导式（元组）一个生成器只能使用一次
gnt=(x for x in range(1,10))
mytuple=tuple(gnt)
print(mytuple)
print(gnt)
mytuple2=tuple(gnt)
print(mytuple2)

