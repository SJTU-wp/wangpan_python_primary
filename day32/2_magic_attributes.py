# author: wp
# 2022年03月22日 22:44
# 使用魔法属性
from test import Animal


class Person:
    """魔法属性演示"""
    country = 'China'

    def __init__(self, name):
        self.name = name
        self.age = 18

    # 当对象在内存中被释放时，自动触发执行
    def __del__(self):
        pass

    # 对象后面加括号，触发执行
    def __call__(self, *args, **kwargs):
        print('__call__')

    def func(self):
        """类方法描述"""
        self.age += 1
        return self.age

    def __str__(self):
        return 'zhang san'


if __name__ == '__main__':
    obj = Person('lao wang')  # 自动执行类中的init方法
    print(obj.name)

    print(Person.__doc__)  # 类的描述信息
    print(Person.func.__doc__)  # 类方法的描述信息
    # print(obj.func.__doc__)  # 可打印，但不能联想
    # print(obj.func().__doc__)  # 可联想，但打印结果并不是想要的

    obj_animal = Animal()
    print(obj_animal.__module__)  # 输出所在模块
    print(obj_animal.__class__)  # 输出所属类

    obj()  # __call__
    Person('wang')()  # __call__

    print(Person.__dict__)  # 获取类的属性,即：类属性、方法
    print(obj.__dict__)  # 获取对象的属性

    print(obj)  # 输出str方法的返回值
