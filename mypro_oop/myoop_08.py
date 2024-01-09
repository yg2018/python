#__call__()函数，该对象像函数一样调用
class SalaryAccount():
    '''工资计算类'''

    def __call__(self, salary):
        yearSalary=salary*12
        daySalary=salary//30
        hourSalary=daySalary//8
        return dict(hourSalary=hourSalary,daySalary=daySalary,monSalary=salary,yearSalary=yearSalary)


s=SalaryAccount()
print(s(5000))
