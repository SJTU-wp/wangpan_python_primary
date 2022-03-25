# author: wp
# 2022年03月24日 21:28
# 在装饰时带参数
def set_level(level_num):
    def decorator(func):
        def inner(*args, **kwargs):
            if level_num == 1:
                print('权限级别1，验证')
            elif level_num == 2:
                print('权限级别2，验证')
            return func(*args, **kwargs)
        return inner
    return decorator


@set_level(1)
def test1():
    print('---test1---')
    return 'ok'


@set_level(2)
def test2():
    print('---test2---')
    return 'ok'


test1()
test2()
