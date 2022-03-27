# author: wp
# 2022年03月27日 22:30
# 实例理解：编写接口类，抽象类
from abc import abstractmethod, ABCMeta


# 接口类
class WalkAnimal(metaclass=ABCMeta):
    @abstractmethod
    def walk(self):
        pass


class SwimAnimal(metaclass=ABCMeta):
    @abstractmethod
    def swim(self):
        pass


class FlyAnimal(metaclass=ABCMeta):
    @abstractmethod
    def fly(self):
        pass


# 如果正常一个老虎有走和游的方法的话，我们会这么做
class Tiger(WalkAnimal, SwimAnimal):  # 多继承
    def walk(self):
        print('walk')

    def swim(self):
        print('swim')


t = Tiger()
t.walk()
t.swim()


# 抽象类
class AllFile(metaclass=ABCMeta):
    all_type = 'file'

    @abstractmethod
    def read(self):
        """子类必须定义读功能"""
        print('read')

    @abstractmethod
    def write(self):
        """子类必须定义写功能"""
        print('write')


class Txt1(AllFile):
    def read(self):
        print('文本数据的读取方法1')
        super().read()

    def write(self):
        print('文本数据的写入方法1')
        super().write()


class Txt2(AllFile):
    def read(self):
        print('文本数据的读取方法2')
        super().read()

    def write(self):
        print('文本数据的写入方法2')
        super().write()


t1 = Txt1()
t2 = Txt2()
print(t1.all_type)
print(t2.all_type)
t1.read()
t1.write()
t2.read()
t2.write()
