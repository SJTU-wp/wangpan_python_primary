# 使用dir查看类里的内容，是否有对象方法，练习__init__，__str__还有__del__

class Cat:

    def __init__(self, new_name):

        self.name = new_name

        print("%s 来了" % self.name)

    def __del__(self):  # 对象销毁的时候调用
        print("%s 我去了" % self.name)  # 用于展示调用效果

    def __str__(self):  # 打印对象调用这个
        # 必须返回一个字符串
        return "我是小猫[%s]" % self.name


tom = Cat('Tom')  # 调用__init__
print(tom)  # 调用__str__
# 默认调用__del__
