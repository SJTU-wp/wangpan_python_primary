# 设计一个类，实例化1个对象

class Dog:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def bark(self):
        print("%s 具有汪汪叫行为" % self.name)

    def shake(self):
        print("%s 具有摇尾巴行为" % self.name)


if __name__ == '__main__':
    dahuang = Dog('dahuang', 'yellow')
    dahuang.bark()
    dahuang.shake()

    print(dir(dahuang))
    print(dir(Dog))
