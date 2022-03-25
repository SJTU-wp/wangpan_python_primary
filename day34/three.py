# author: wp
# 2022年03月24日 20:14
# 使用装饰器为某个函数增加权限验证

def verify(func):
    print('--开始进行装饰--')

    def inner():
        print('权限验证')
        func()
    return inner


@verify  # 等价于func = verify(func)  其实就是inner了
def func():
    print('I am func')


func()  # 相当于运行inner(), 但内置函数中的func()还是原func()
print(func)  # <function verify.<locals>.inner at 0x00000279E8DC7310>
print(func())  # 权限验证  I am func  None
