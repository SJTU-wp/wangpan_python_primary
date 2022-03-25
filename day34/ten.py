# author: wp
# 2022年03月24日 21:35
# 类装饰器
class Test:
    def __init__(self, func):
        print('--初始化--')
        print('func name is %s' % func.__name__)
        self.__func = func  # 私有属性，保存原函数体的引用

    def __call__(self, *args, **kwargs):
        print('--callable--')
        self.__func()


@Test
def test():
    print('--test--')


test()  # test = Test(test), 是个实例对象，能直接加括号是因为call的存在
