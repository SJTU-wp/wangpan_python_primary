# 可变参数练习，元组，字典的传参拆包练习

def demo1(*args, **kwargs):
    print(args)
    print(kwargs)
    print('-' * 50)
    # print(*args) 报错
    # print(**kwargs) 报错
# 可变参数 也叫 多值参数
# 在元组前加*就是解包(unpack),效果呢就是 (1,2,3,4) 就会变为1,2,3,4
# 在字典前加** 就是解包(unpack), 效果呢
# {'name': '小明', 'age': 18, 'gender': True}
# 变为 name="小明", age=18, gender=True


def demo(num, *args, **kwargs):
    print(num)
    print(args)
    print(kwargs)
    print('-' * 50)
    demo1(*args, **kwargs)


if __name__ == '__main__':
    demo(1, 2, 3, 4, 5, name="小明", age=18, gender=True)
