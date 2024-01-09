import time

print("当前秒数：")
b = int(time.time())//60
print(b)


print("当前分钟数：")
b = int(b//60)
print(b)

print("当前小时数：")
b = int(b//24)
print(b)

print("当前天数：")
b = int(b//365)
print(b)
