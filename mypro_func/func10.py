##递归函数（内存消耗比较大，时间消耗比较小）
###1、中止条件
###2、递归步骤
def fa(n):
    if n==1:return 1
    return n*fa(n-1)

for i in range(1,6):
    print(i,'!=',fa(i))