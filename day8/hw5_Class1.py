# 设计一个类，实例化两个对象
# 小明跑步跑完步，会去吃东西
# 小美不跑步，小美喜欢吃东西

# object是基类
# 实例化 ，初始化一个对象时，调用__init__
class Person(object):
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def run(self):
        print('%s runs in the morning' % self.name)

    def eat(self):
        print('%s eats' % self.name)


xiaoming = Person('xiaoming', 18, 1.75)
xiaoming.run()
xiaoming.eat()
xiaomei = Person('xiaomei', 17, 1.65)
xiaomei.eat()
print(xiaoming)
print(xiaomei)
print(dir(xiaoming))
print(dir(xiaomei))
print(dir(Person))
