# author: wp
# 2022年03月24日 20:49
# 使用装饰器实现函数执行时间统计
import time


def time_cal(func):
    print('开始统计时间')

    def inner():
        start_time = time.time()
        func()
        end_time = time.time()
        print('函数{}执行时间为：{}'.format(func.__name__, (end_time - start_time)))
    return inner


@time_cal
def func():
    print('I am func')
    for i in range(100000):
        pass


func()
