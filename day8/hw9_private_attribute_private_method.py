# 练习私有属性和私有方法

class Women:

    def __init__(self, name):

        self.name = name
        self.__age = 18

    def eat(self):
        self.__secret()  # 私有方法只能被自己的方法内部调用

    def __secret(self):
        print("我的年龄是 %d" % self.__age)  # 私有属性只能被自己的方法调用


if __name__ == '__main__':
    xiaomei = Women('小美')
    print(xiaomei.name)  # 外界无法调用__age属性
    xiaomei.eat()  # 外界无法调用__secret方法
