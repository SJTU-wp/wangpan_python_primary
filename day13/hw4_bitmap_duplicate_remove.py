# author: wp
# 2022年03月01日 22:10
# 自行编写位图，实现1千个随机数（0-1万）之间的去重
import random


class Bitmap:
    def __init__(self, arr_len):
        self.bitmap = 0
        self.arr = []
        self.arr_len = arr_len
        # 可以新定义列表将去重结果放入其中(for)，也可以尝试在原列表中进行pop（索引）操作去重(while)
        self.arr_new = []

    def randint_arr(self):
        for i in range(0, self.arr_len):
            self.arr.append(random.randint(0, 10000))
        print(self.arr)

    def duplicate_remove(self):
        for i in self.arr:
            # 如果已经存在，不放入arr_new
            if self.bitmap & 1 << i:  # 按位与，有假则假
                pass
            # 如果不存在，放入arr_new，并更新bitmap值
            else:
                self.arr_new.append(i)
                # 更新bitmap值以表示i已放入arr_new
                self.bitmap = self.bitmap | 1 << i  # 按位或，有真则真
        return self.arr_new


if __name__ == '__main__':
    arr = Bitmap(1000)
    arr.randint_arr()
    print(arr.duplicate_remove())
