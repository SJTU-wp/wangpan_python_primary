# 完成类属性，类方法的使用

class Tool:
    count = 0

    def __init__(self, name):
        self.name = name

        # 针对类属性做一个计数？
        Tool.count += 1  # 每调用一次初始化计数+1

    # 给一个方法加上classmethod进行装饰，就是类方法
    @classmethod
    def show_tool_count(cls):
        """显示工具对象的总数"""
        print("类方法工具对象的总数为 %d" % cls.count)


# 创建工具对象
tool1 = Tool("斧头")
tool2 = Tool("榔头")
tool3 = Tool("铁锹")

# 到这里调用了三次__init__，所以计数应为3
# 使用 Tool 类到底创建了多少个对象？
print("现在创建了 %d 个工具" % Tool.count)

print("现在创建了 %d 个工具" % tool3.count)  # 不规范的写法，因为count是类属性，虽然tool3作为类的对象也能调用，但是不规范
tool3.count = 99  # 创建了一个count对象属性
print("工具对象总数 %d" % tool3.count)  # 99
print("===> %d" % Tool.count)  # 类属性不会变
Tool.show_tool_count()
