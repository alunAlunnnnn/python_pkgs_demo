from functools import singledispatch


class Test:
    def __init__(self):
        pass

    @singledispatch
    def age(self, para1):
        print("数据类型未注册")

    @age.register(int)
    def _(self, para1):
        print("整数")

    @age.register(str)
    def _(self, para1):
        print("字符串")

t = Test()
t.age(1)
