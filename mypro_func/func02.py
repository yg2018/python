#函数也是对象

def printStar(n):
    print('*'*n);

print(id(printStar))
print(type(printStar))

printStar(10)
c=printStar
c(10)