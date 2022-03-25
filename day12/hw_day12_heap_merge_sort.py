# author: wp
# 2022年02月26日 19:17

import random


class MySort2:
    def __init__(self, arr_len):
        self.arr = []
        self.arr_len = arr_len
        # self.arr_new = [] 初始bug处
        self.arr_new = [0] * arr_len

    def arr_randint(self):
        for i in range(self.arr_len):
            self.arr.append(random.randint(0, 99))
        print(self.arr)

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
        for i in range(self.arr_len // 2 - 1, -1, -1):
            self.adjust_max_heap(self.arr_len, i)
        # 将最大值放在列表最后
        arr[0], arr[self.arr_len - 1] = arr[self.arr_len - 1], arr[0]

        # 重要：现在只有顶部元素不满足大根堆，故针对其调整
        for i in range(self.arr_len - 1, 1, -1):
            self.adjust_max_heap(i, 0)
            arr[0], arr[i - 1] = arr[i - 1], arr[0]
        print(self.arr)

    # 合并两个有序数组
    def merge(self, low, mid, high):
        arr_new = self.arr_new
        arr = self.arr
        for i in range(low, high + 1):
            arr_new[i] = arr[i]  # 关键理解处

        # 初始化
        i = low
        j = mid + 1
        # k = 0 起初bug处
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

        # while j <= high:
        #     arr[k] = arr_new[j]
        #     k += 1
        #     j += 1
        # while i <= mid:
        #     arr[k] = arr_new[i]
        #     k += 1
        #     i += 1
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


if __name__ == '__main__':
    my_sort = MySort2(10)

    my_sort.arr_randint()
    my_sort.heap_sort()

    my_sort.arr.clear()
    my_sort.arr_randint()
    my_sort.merge_sort(0, 9)
    print(my_sort.arr)

# # 调整大根堆麻烦方法，中间无用的重复判断过多
#     def adjust_max_heap(self, arr_len):
#         # 首先定位最后一个父节点
#         self.arr_len = arr_len
#         arr = self.arr
#         i = arr_len // 2 - 1  # 起始位置
#         while i >= 0:
#             son = 2 * i + 1  # 还少个判断son不溢出的条件
#             if arr[son] >= arr[son + 1] and arr[son] > arr[i]:
#                 arr[son], arr[i] = arr[i], arr[son]
#                 i = son
#                 continue
#             elif arr[son + 1] > arr[i]:
#                 arr[son + 1], arr[i] = arr[i], arr[son + 1]
#                 i = son + 1
#                 continue
#             i -= 1

# 合并两个有序数组，原错误写法，依照这种写法，arr一直处在乱序状态而未变
# 而每次调用merge函数都将给arr_new中赋值无序数组，而非设想中的有序数组合并过程
# 这样做的后果应该就是相当于只进行了最后一次合并，试试看
#     def merge(self, low, mid, high):
#         arr_new = self.arr_new
#         arr = self.arr
#         for i in range(low, high + 1):
#             arr_new[i] = arr[i]
#
#         i = low
#         j = mid + 1
#         # k = 0 起初bug处
#         k = low
#
#         while i < mid + 1 and j < high + 1:
#             if arr[i] < arr[j]:
#                 arr_new[k] = arr[i]
#                 i += 1
#             else:
#                 arr_new[k] = arr[j]
#                 j += 1
#             k += 1
#
#         while j <= high:
#             arr_new[k] = arr[j]
#             k += 1
#             j += 1
#         while i <= mid:
#             arr_new[k] = arr[i]
#             k += 1
#             i += 1
