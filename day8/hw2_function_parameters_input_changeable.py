# 函数可变类型列表、字典入参练习，在函数内改变列表，字典内容后，函数外打印显示发生改变

def change(num_list):
    # num_list.extend([1, 2, 3])
    # num_list = num_list + [1, 2, 3]
    num_list += [1, 2, 3]

    print(num_list)
    print('-' * 50)


def change2(dict1):
    dict1["name"] = 'xiongda'
    dict1["weight"] = 65

    print(dict1)
    print('-' * 20)


if __name__ == '__main__':
    demo_list = [6, 7, 8]
    change(demo_list)
    print(demo_list)
    print()

    demo_dict = {"name": "xiaoming", "age": 17, "height": 175}
    change2(demo_dict)
    print(demo_dict)
