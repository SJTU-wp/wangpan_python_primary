# author: wp
# 2022年03月22日 22:42
# 使用property属性装饰方法，实现通过对象.属性实现某个方法的调用
class Foo:
    @staticmethod
    def func():
        print('I am func')

    @property
    def prop(self):
        print('I am prop')
        return

    def prop2(self):
        return 'I am prop2'

    result = property(prop2)  # 类属性里边使用property


if __name__ == '__main__':
    foo_object = Foo()
    foo_object.func()  # 调用实例方法
    s = foo_object.prop  # 调用property属性
    ret = foo_object.result  # 自动调用prop2方法，并获取方法的返回值
    print(ret)
