##浅拷贝和深拷贝（参数的传递是浅拷贝）

###浅拷贝不拷贝子对象
###深拷贝拷贝设计的所有对象

import copy

def testCopy():
    '''测试浅拷贝'''
    a=[10,20,[5,6]]
    b=copy.copy(a)
    print("a:",a)
    print("b:",b)
    b.append(30)
    b[2].append(8)
    print("浅拷贝....")
    print("a:",a)
    print("b:",b)

def testDeepCopy():
    '''测试深拷贝'''
    a = [10, 20, [5, 6]]
    b = copy.deepcopy(a)
    print("a:", a)
    print("b:", b)
    b.append(30)
    b[2].append(8)
    print("深拷贝....")
    print("a:", a)
    print("b:", b)

testCopy()
testDeepCopy()