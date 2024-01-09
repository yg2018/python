#coding=utf-8
##自定义异常
class AgeError(Exception):
    def __init__(self,errorInfo):
        Exception.__init__(self)
        self.errorInfo=errorInfo
    def __str__(self):
        return str(self.errorInfo)+",年龄错误，应该在1-150之间"
age=int(input("输入年龄"))
if age<0 or age>150:
    raise AgeError(age)
else:
    print(age)