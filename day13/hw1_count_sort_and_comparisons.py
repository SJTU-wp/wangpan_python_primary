# author: wp
# 2022年02月28日 19:15
# 完成计数排序，对比不同排序算法排10万数的时间

import random
import time
import sys
sys.setrecursionlimit(100000)  # 修改最大递归深度；利于快排


class MySort:
    def __init__(self, arr_length):
        self.arr = []
        self.arr_length = arr_length
        self.arr_new = [0] * arr_length
        self.boundary = 100  # 数据范围；利于计数排序的调整

    def randint_arr(self):
        for i in range(self.arr_length):
            self.arr.append(random.randint(0, self.boundary - 1))

    # 冒泡排序（尝试用for循环去写），注意循环退出，警惕死循环
    def bubble_sort(self):
        for i in range(self.arr_length - 1):
            j = 0
            while j < self.arr_length - i - 1:
                if self.arr[j] > self.arr[j + 1]:
                    self.arr[j], self.arr[j + 1] = self.arr[j + 1], self.arr[j]
                j += 1

    # 选择排序 selection sort
    def selection_sort(self):
        for i in range(self.arr_length - 1):
            min_pos = i  # 之前这里出bug了
            for j in range(i + 1, self.arr_length):
                if self.arr[j] < self.arr[min_pos]:
                    min_pos = j
            self.arr[i], self.arr[min_pos] = self.arr[min_pos], self.arr[i]

    # 插入排序 insertion sort
    def insertion_sort(self):
        for i in range(self.arr_length - 1):
            j = i
            while j >= 0:
                if self.arr[j + 1] < self.arr[j]:  # 这个判断条件相对难一点
                    self.arr[j + 1], self.arr[j] = self.arr[j], self.arr[j + 1]
                j -= 1

    # 快速排序 quick sort
    # 首先定义分割函数（核心）
    def partition(self, left, right):
        arr = self.arr
        k = left
        # 添加代码降低快排最坏情况发生的概率
        tmp = random.randint(left, right)
        arr[right], arr[tmp] = arr[tmp], arr[right]

        for i in range(left, right):
            if arr[i] < arr[right]:
                arr[i], arr[k] = arr[k], arr[i]
                k += 1
        arr[k], arr[right] = arr[right], arr[k]
        return k

    # 快排递归
    def quick_sort(self, left, right):
        while left < right:  # 原先写了left != right，错误，left有可能比right小
            # 还单写过while没break，也不对，while会一直循环，而下面本就有递归，你只想让该程序执行一次，一个if就够了
            pivot = self.partition(left, right)
            self.quick_sort(left, pivot - 1)
            self.quick_sort(pivot + 1, right)
            break

    # 堆排：首先写如何将某一棵子树调整为大根堆，心中有树
    def adjust_max_heap(self, arr_len, start_pos):
        # 首先定位最后一个父节点
        arr = self.arr
        dad = start_pos  # 起始位置
        son = 2 * dad + 1
        while son < arr_len:
            if son + 1 < arr_len and arr[son] < arr[son + 1]:  # 保证son是左右子树中的最大值
                # arr[son], arr[son + 1] = arr[son + 1], arr[son] 原先写法，很隐晦的bug，最后不符合从小到大排序的要求
                son += 1
            if arr[son] > arr[dad]:
                arr[son], arr[dad] = arr[dad], arr[son]
                dad = son
                son = 2 * dad + 1
            else:
                break

    def heap_sort(self):
        arr = self.arr
        # 调整为大根堆
        for i in range(self.arr_length // 2 - 1, -1, -1):
            self.adjust_max_heap(self.arr_length, i)
        # 将最大值放在列表最后
        arr[0], arr[self.arr_length - 1] = arr[self.arr_length - 1], arr[0]

        # 重要：现在只有顶部元素不满足大根堆，故针对其调整
        for i in range(self.arr_length - 1, 1, -1):
            self.adjust_max_heap(i, 0)
            arr[0], arr[i - 1] = arr[i - 1], arr[0]

    # 合并两个有序数组
    def merge(self, low, mid, high):
        arr_new = self.arr_new
        arr = self.arr
        for i in range(low, high + 1):
            arr_new[i] = arr[i]  # 关键理解处

        # 初始化
        i = low
        j = mid + 1
        k = low

        # 合并两个有序数组
        while i < mid + 1 and j < high + 1:
            if arr_new[i] < arr_new[j]:
                arr[k] = arr_new[i]
                i += 1
            else:
                arr[k] = arr_new[j]
                j += 1
            k += 1

        for i in range(j, high + 1):
            arr[k] = arr_new[i]
            k += 1
        for i in range(i, mid + 1):
            arr[k] = arr_new[i]
            k += 1

    def merge_sort(self, low, high):
        # 递归分割，分治思想
        if low < high:
            mid = (low + high) // 2
            self.merge_sort(low, mid)
            self.merge_sort(mid + 1, high)
            self.merge(low, mid, high)  # 算法核心

    def count_sort(self):
        # 计数
        count = [0] * self.boundary
        for i in self.arr:
            count[i] += 1

        # 回填
        k = 0
        for i in range(0, self.boundary):
            j = 1
            while j <= count[i]:
                self.arr[k] = i
                j += 1
                k += 1

    # 提供调用所有排序算法的接口
    def test_sort(self, sort_method, *args, **kwargs):
        print(self.arr)
        sort_method(*args, **kwargs)
        print(self.arr)

    def test_sort_time(self, sort_method, *args, **kwargs):
        self.arr = temp  # 保证不同排序算法是对同一数组进行排序
        start = time.time()
        sort_method(*args, **kwargs)
        end = time.time()
        print('{} use time: {}'.format(sort_method, end-start))


if __name__ == '__main__':
    my_sort = MySort(100000)
    my_sort.randint_arr()
    temp = my_sort.arr  # temp在运行过程中为常量
    # my_sort.test_sort(my_sort.bubble_sort)
    # my_sort.test_sort(my_sort.selection_sort)
    # my_sort.test_sort(my_sort.insertion_sort)
    # my_sort.test_sort(my_sort.quick_sort, 0, my_sort.arr_length - 1)
    # my_sort.test_sort(my_sort.heap_sort)
    # my_sort.test_sort(my_sort.merge_sort, 0, my_sort.arr_length - 1)
    # my_sort.test_sort(my_sort.count_sort)
    my_sort.test_sort_time(my_sort.bubble_sort)
    my_sort.test_sort_time(my_sort.selection_sort)
    my_sort.test_sort_time(my_sort.insertion_sort)
    my_sort.test_sort_time(my_sort.quick_sort, 0, my_sort.arr_length - 1)
    my_sort.test_sort_time(my_sort.heap_sort)
    my_sort.test_sort_time(my_sort.merge_sort, 0, my_sort.arr_length - 1)
    my_sort.test_sort_time(my_sort.count_sort)
