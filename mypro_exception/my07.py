#coding=utf-8
## return 一般不放到try except else finally中，一般放到最后，避免发生意想不到的错误

def test01():
    print("step1")
    try:
        x=3/0
        return "a"
    except BaseException as e:
        print(e)
        return "b"
    finally:
        return "c"
        print("总要执行")
    return "d"

print(test01())
