#类对象
class Student():
    pass

Stu2=Student
print(id(Student))
print(type(Student))
s=Stu2()
print(type(s))