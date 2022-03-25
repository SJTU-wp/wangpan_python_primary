# 有101个整数，其中有50个数出现了两次,1个数出现了一次，找出出现了一次的那个数

import random

# 随机生成符合题意的101个整数
number_list1 = []

# 先在列表1中添加51个互不相同的随机数（默认在0~1000之间）
while len(number_list1) < 51:
    rand_number = random.randint(0, 1000)
    if rand_number not in number_list1:
        number_list1.append(rand_number)

# 构造符合题意、包含101个整数的列表
number_list = number_list1 + number_list1[0:50]
random.shuffle(number_list)  # 打乱
print(number_list)

# 找出出现了一次的那个数，利用“按位异或”运算及其交换律
num = 0
for i in range(0, 101):
    num = num ^ number_list[i]

print("这101个整数中，只出现了一次的数为：", num)

# 麻烦判断方法
# for i in range(0, 101):
#     while number_list.count(number_list[i]) == 1:
#         print...

# # 用7个整数测试代码正确性
#
# import random
#
# # 随机生成符合题意的7个整数
# number_list1 = []
#
# # 先在列表1中添加4个互不相同的随机数（默认在0~1000之间）
# while len(number_list1) < 4:
#     rand_number = random.randint(0, 1000)
#     if rand_number not in number_list1:
#         number_list1.append(rand_number)
#
# # 构造符合题意、包含7个整数的列表
# number_list = number_list1 + number_list1[0:3]
# random.shuffle(number_list)  # 打乱
# print(number_list)
#
# # 找出出现了一次的那个数，利用“按位异或”运算及其交换律
# num = 0
# for i in range(0, 7):
#     num = num ^ number_list[i]
#
# print("这7个整数中，只出现了一次的数为：", num)
