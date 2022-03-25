import random


# 1、seek偏移文字
def use_seek():
    file = open('file', mode='r+', encoding='utf8')
    pass


# 冒泡排序 bubble sort
def bubble_sort(arr_length):
    # 生成随机数
    arr = []
    for i in range(arr_length):
        arr.append(random.randint(0, 99))
    print(arr)

    i = arr_length - 1
    while i > 0:
        j = 0
        while j < i:
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            j += 1
        i -= 1

    print(arr)


# 选择排序 selection sort
def selection_sort(arr_length):
    # 生成随机数
    arr = []
    for i in range(arr_length):
        arr.append(random.randint(0, 99))
    print(arr)

    i = 0
    min_pos = i
    while i < arr_length - 1:
        j = i + 1
        while j < arr_length:
            if arr[j] < arr[min_pos]:
                min_pos = j
            j += 1
        arr[i], arr[min_pos] = arr[min_pos], arr[i]
        i += 1

    print(arr)


if __name__ == '__main__':
    bubble_sort(10)
    selection_sort(10)
