##全局变量和局部变量

a=10

def test():
    global a
    a=20
    print(a)

test()
print(a)

##locals和globals
def test02(a,b,c):
    '''locals和globals'''
    print(a,b,c)
    print(locals())
    print('#'*10)
    print(globals())

test02(10,20,30)
#print(help(test02))