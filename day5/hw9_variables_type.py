# 编写代码理解可变类型和不可变类型

# 整型int
a = 10
b = 10
print("整型示例改变前内存地址为：", id(a), id(b))
a = 20
b = 20
print("整型示例改变后内存地址为：", id(a), id(b))

# 布尔型
bool1 = True
bool2 = True
print("布尔型示例改变前内存地址为：", id(bool1), id(bool2))
bool1 = False
print("布尔型示例改变后内存地址为：", id(bool1))

# 浮点型
float1 = 1.345
float2 = 1.345
print("浮点型示例改变前内存地址为：", id(float1), id(float2))
float1 = 7.892
print("浮点型示例改变后内存地址为：", id(float1))

# 复数型
complex1 = 3 + 4j
complex2 = 3 + 4j
print("复数型示例改变前内存地址为：", id(complex1), id(complex2))
complex1 = 2 + 6j
print("复数型示例改变后内存地址为：", id(complex1))

# 字符串
str1 = 'pycharm'
str2 = 'pycharm'
print("字符串示例改变前内存地址为：", id(str1), id(str2))
str1 = 'pycharm...'
print("字符串示例改变后内存地址为：", id(str1))

# 元组
tuple1 = (2, 3, 4, 1)
tuple2 = (2, 3, 4, 1)
print("元组示例改变前内存地址为：", id(tuple1), id(tuple2))
tuple1 = (1, 5, 9)
print("元组示例改变后内存地址为：", id(tuple1))

# 列表
demo_list = ['a', 'exams', 3, 8, 'type']
print(demo_list)
print("列表示例改变前内存地址为：", id(demo_list))
demo_list[0] = 'b'
demo_list[2] = 'homework'
print(demo_list)
print("列表示例改变后内存地址为：", id(demo_list))

# 字典
demo_dict = {"name": "wang pan", "age": 23}
print(demo_dict)
print("字典示例改变前内存地址为：", id(demo_dict))
demo_dict["name"] = "wang qiang"
demo_dict.pop("age")
print(demo_dict)
print("字典示例改变后内存地址为：", id(demo_dict))
