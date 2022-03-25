# hw5 选择、插入、快速排序
import random


class MySort:
    def __init__(self, arr_length):
        self.arr = []
        self.arr_length = arr_length

    def randint_arr(self):
        for i in range(self.arr_length):
            self.arr.append(random.randint(0, 99))
        print(self.arr)

    # 选择排序 selection sort
    def selection_sort(self):
        # min_pos = 0  # 原bug处
        for i in range(self.arr_length - 1):
            min_pos = i
            for j in range(i + 1, self.arr_length):
                if self.arr[j] < self.arr[min_pos]:
                    min_pos = j
            self.arr[i], self.arr[min_pos] = self.arr[min_pos], self.arr[i]
        print(self.arr)

    # 插入排序 insertion sort
    def insertion_sort(self):
        for i in range(self.arr_length - 1):
            j = i
            while j >= 0:
                if self.arr[j + 1] < self.arr[j]:  # 这个判断条件相对难一点
                    self.arr[j + 1], self.arr[j] = self.arr[j], self.arr[j + 1]
                j -= 1
        print(self.arr)

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


if __name__ == '__main__':
    my_sort = MySort(10)

    my_sort.randint_arr()
    my_sort.selection_sort()

    # my_sort.arr.clear()
    # my_sort.randint_arr()
    # my_sort.insertion_sort()
    #
    # my_sort.arr.clear()
    # my_sort.randint_arr()
    # my_sort.quick_sort(0, my_sort.arr_length - 1)
    # print(my_sort.arr)
