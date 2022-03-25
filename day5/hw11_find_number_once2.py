# 有102个整数，其中有50个数出现了两次，2个数出现了一次，找出出现了一次的那2个数（大家使用8个数即可）

import random

# 随机生成符合题意的8个整数
number_list1 = []

# 先在列表1中添加5个互不相同的随机数（默认在0~1000之间）
while len(number_list1) < 5:
    rand_number = random.randint(0, 1000)
    if rand_number not in number_list1:
        number_list1.append(rand_number)

# 构造符合题意、包含8个整数的列表
number_list = number_list1 + number_list1[0:3]
random.shuffle(number_list)  # 打乱
print(number_list)

# 找出出现了一次的那两个数，调用list.count（待改进）
print("这8个整数中，只出现了一次的两个数分别为：")
for i in range(0, 8):
    while number_list.count(number_list[i]) == 1:
        print(number_list[i])
        break

# 失败做法
# for i in range(0, 8):
#     num = num ^ number_list[i]
# for i in range(0, 8):
#     number_list2[i] = num ^ number_list[i]
# for i in range(0, 8):
#     if number_list[i] in number_list2:
#         print(number_list[i])
