# author: wp
# 2022年03月24日 21:06
# 可变参数函数的装饰练习

def decorator(func):
    print('开始进行装饰')

    def inner(*args, **kwargs):
        print('权限验证')
        func(*args, **kwargs)
    return inner


@decorator
def func(a, *args, **kwargs):
    print('--test1-- %d' % a)
    print('--test1--', args)
    print('--test1--', kwargs)


func(2)
func(7, 8)
func(6, 8, 9, 10, zhangsan=18)  # 如果是zhang san呢？
