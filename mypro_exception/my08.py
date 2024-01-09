#coding=utf-8
## with代码块
with open("d:/idea/test.txt",encoding="utf-8") as f:
    for line in f:
        print(line)