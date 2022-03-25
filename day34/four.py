# author: wp
# 2022年03月24日 20:31
# 多个装饰器的执行顺序练习，掌握其原理
def decorator1(func):
    print('--开始装饰1--')

    def inner1():
        print('verify 1')
        func()

    return inner1


def decorator2(func):
    print('--开始装饰2--')

    def inner2():
        print('verify 2')
        func()

    return inner2


@decorator1  # func = decorator1(func)  等号右边的func是经过装饰2的func
@decorator2  # 先装饰  func = decorator2(func)
def func():
    print('I am func')


# func()
# print(func)  # <function decorator1.<locals>.inner1 at 0x00000288A68F13A0>
print(func())  # 比func()多一个None   完美！
