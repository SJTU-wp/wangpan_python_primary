# author: wp
# 2022年03月24日 21:23
# 装饰器中如果不使用return func(),那么最终的返回值是多少
from time import ctime, sleep


def decorator(func):
    def inner(a, b):
        print('{} called at {}'.format(func.__name__, ctime()))
        print(a, b)
        return func(a, b)
    return inner


@decorator
def func(a, b):
    print(a+b)
    return a+b


func(2, 3)
sleep(2)
print(func)  # <function decorator.<locals>.inner at 0x0000011F66777310>
print(func(7, 8))  # ... 15
