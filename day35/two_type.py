# author: wp
# 2022年03月26日 20:26
# 使用元类type生成一个类

class A(object):
    num = 100


# 普通方法
def print_b(self):
    print(self.num)


# 静态方法
@staticmethod
def print_static():
    print('I am static')


# 类方法
@classmethod
def print_class(cls):
    print(cls.num)


# 使用元类type生成一个类，有继承，有各种方法，有属性
B = type("B", (A,), {"print_b": print_b, "print_static": print_static,
                     "print_class": print_class, "bar": True})

b = B()
b.print_b()
b.print_static()
b.print_class()
print(b.bar)
print(B.__dict__)
