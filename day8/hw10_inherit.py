# 练习继承、使用super调用父类方法，多重继承

class Animal:

    @staticmethod
    def eat():
        print("吃---")

    @staticmethod
    def drink():
        print("喝---")

    @staticmethod
    def run():
        print("跑---")

    @staticmethod
    def sleep():
        print("睡---")


class Dog(Animal):
    @staticmethod
    def bark():
        print("汪汪叫")


class XiaoTianQuan(Dog):
    @staticmethod
    def fly():
        print('会飞')

    def bark(self):
        super().bark()  # 调用父类的方法bark
        print('像神一样的叫唤')


class Pet:
    @staticmethod
    def eat():
        print("吃---")


class Cat(Animal, Pet):
    @staticmethod
    def catch():
        print('爬树')


# 创建一个狗对象
xiaohei = Dog()

xiaohei.eat()
xiaohei.drink()
xiaohei.run()
xiaohei.sleep()
xiaohei.bark()
print('-' * 50)

xiaomei = Cat()
xiaomei.catch()
xiaomei.drink()
xiaomei.eat()
print(Cat.__mro__)
print('-' * 50)

god_dog = XiaoTianQuan()
god_dog.fly()
god_dog.eat()
god_dog.bark()  # 调用重写后的bark方法
