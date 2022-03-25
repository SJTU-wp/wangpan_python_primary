# author: wp
# 2022年03月21日 20:38
# 实现工厂模式


class Animal:

    def eat(self):
        pass

    def voice(self):
        pass


class Dog(Animal):
    def eat(self):
        print('狗吃骨头')

    def voice(self):
        print('狗叫汪汪')


class Cat(Animal):
    def eat(self):
        print('猫吃鱼')

    def voice(self):
        print('猫叫喵喵')


class FactoryMode:
    def __init__(self):
        self.d = {'dog': Dog(), 'cat': Cat()}

    def create_ani(self, animal_name):
        return self.d[animal_name]


if __name__ == '__main__':
    f_test = FactoryMode()
    animal = f_test.create_ani('cat')  # 走哪一类
    animal.eat()
    animal.voice()
