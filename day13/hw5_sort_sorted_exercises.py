# author: wp
# 2022年03月02日 15:02
from operator import itemgetter, attrgetter


def sort_str():
    l5 = "This is a test string from wp Tan".split()
    print(l5)
    print(sorted(l5, key=str.lower))  # key等于一个函数；往往会写一个匿名函数


# 待排序的列表里是元组
def sort_list_tuple():
    students_tuples = [
        ('john', 'A', 15),
        ('jane', 'B', 12),
        ('dave', 'B', 10)
    ]

    # 理解
    # def my_func(i):
    #     return i[2]

    # lambda就是匿名函数
    print(sorted(students_tuples, key=lambda i: i[2]))


class Student:

    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age

    def __repr__(self):  # 相对于str更加灵活，可以返回你想返回的类型
        return repr((self.name, self.grade, self.age))


# 待排序的列表里是自定义的对象
def sort_list_object():
    students_objects = [
        Student('john', 'A', 15),
        Student('jane', 'B', 12),
        Student('dave', 'B', 10)
    ]  # __repr__保证可以排“对象”
    print(sorted(students_objects, key=lambda s: s.age))


def use_operator():
    students_tuples = [
        ('john', 'A', 15),
        ('jane', 'B', 12),
        ('dave', 'B', 10)
    ]
    print(sorted(students_tuples, key=itemgetter(2)))
    students_objects = [
        Student('john', 'A', 15),
        Student('jane', 'B', 12),
        Student('dave', 'B', 10)
    ]
    print(sorted(students_objects, key=attrgetter('grade')))
    print(sorted(students_tuples, key=itemgetter(1, 2)))  # 多层排序
    print(sorted(students_objects, key=attrgetter('grade', 'age')))


# 稳定性演示
def use_stability():
    l5_1 = [('red', 1), ('blue', 1), ('red', 2), ('blue', 2)]
    l5_1.sort(key=itemgetter(0))
    print(l5_1)


# 字典中有列表
def dict_list():
    my_dict = {'Li': ['M', 7],
               'Zhang': ['E', 2],
               'Wang': ['P', 3],
               'Du': ['C', 2],
               'Ma': ['C', 9],
               'Zhe': ['H', 7]}
    # my_dict.items()将字典中的键值对以元组的形式组合到一起
    print(sorted(my_dict.items(), key=lambda v: v[1][1]))  # 难点


# 列表中有字典；itemgetter的强大之处
def list_dict():
    game_result = [
        {"name": "Bob", "wins": 10, "losses": 3, "rating": 75.00},
        {"name": "David", "wins": 3, "losses": 5, "rating": 57.00},
        {"name": "Carol", "wins": 4, "losses": 5, "rating": 57.00},
        {"name": "Patty", "wins": 9, "losses": 3, "rating": 71.48}]
    print(sorted(game_result, key=itemgetter('rating', 'wins')))


if __name__ == '__main__':
    # sort_list_object()
    # use_operator()
    # use_stability()
    # dict_list()
    list_dict()
