#coding=utf-8
## 读取资源，finally关闭资源
try:
    f=open("d:/idea/test.txt","r",encoding="utf-8")
    content=f.readline()
    print(content)
except BaseException as e:
    print(e)
finally:
    f.close()

print("the end!")