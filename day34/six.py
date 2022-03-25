# author: wp
# 2022年03月24日 21:01
# 有参数函数的装饰练习

from time import ctime, sleep


def decorator(func):
    def inner(a, b):
        print('{} called at {}'.format(func.__name__, ctime()))
        print(a, b)
        func(a, b)
    return inner


@decorator
def func(a, b):
    print(a+b)


func(2, 3)
sleep(2)
func(7, 8)
