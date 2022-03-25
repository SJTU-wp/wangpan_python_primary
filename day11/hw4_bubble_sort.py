# 冒泡排序
import random


def bubble_sort(ls_length):
    # 生成需排序数据
    list4 = []
    for i in range(ls_length):
        list4.append(random.randint(0, 99))
    print(list4)

    # 冒泡排序（尝试用for循环去写），注意循环退出，警惕死循环
    for i in range(ls_length - 1):
        j = 0
        while j < ls_length - i - 1:
            if list4[j] > list4[j+1]:
                list4[j], list4[j+1] = list4[j+1], list4[j]
            j += 1

    print(list4)


if __name__ == '__main__':
    bubble_sort(10)
