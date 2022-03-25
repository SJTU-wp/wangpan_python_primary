# author: wp
# 2022年03月21日 20:47
# 多重继承，mro应用，调用__init__


class Parent(object):
    def __init__(self, gender, *args, **kwargs):  # 为避免多继承报错，使用不定长参数，接受参数
        print('parent的init开始被调用')
        self.gender = gender  # grandpa吃掉gender
        print('parent的init结束被调用')


class Son1(Parent):
    def __init__(self, name, age, *args, **kwargs):  # 为避免多继承报错，使用不定长参数，接受参数
        print('Son1的init开始被调用')
        self.name = name  # son1吃掉name
        super().__init__(age, *args, **kwargs)  # 为避免多继承报错，使用不定长参数，接受参数
        print('Son1的init结束被调用')


class Son2(Parent):
    def __init__(self, age, gender, *args, **kwargs):  # 为避免多继承报错，使用不定长参数，接受参数
        print('Son2的init开始被调用')
        self.age = age  # son2吃掉age
        super().__init__(gender, *args, **kwargs)  # 为避免多继承报错，使用不定长参数，接受参数
        print('Son2的init结束被调用')


class Grandson(Son1, Son2):  # 多重继承
    def __init__(self, name, age, gender):
        print('Grandson的init开始被调用')
        # 多继承时，相对于使用类名.__init__方法，要把每个父类全部写一遍
        # 而super只用一句话，执行了全部父类的方法，这也是为何多继承需要全部传参的一个原因
        # super(Grandson, self).__init__(name, age, gender)  python2中的写法，与下面等价
        super().__init__(name, age, gender)
        print('Grandson的init结束被调用')


print(Grandson.__mro__)  # 打印出来顺序是谁，将来调用的就是谁
gs = Grandson('grandson', 12, '男')
print('姓名：', gs.name)
print('年龄：', gs.age)
print('性别：', gs.gender)
