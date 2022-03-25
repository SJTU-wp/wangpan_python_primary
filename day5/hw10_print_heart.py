# 打印一个心形图案

# 打印前3行
for i in range(1, 4):  # 用来记录行数
    j = 4 - i  # 用来记录空格数
    print(' ' * j + '* ' * (i + 1) + ' ' * (2 * j) + '* ' * i, end='')
    print('*')

# 打印后10行
for i in range(4, 14):  # 用来记录行数
    i = 14 - i
    j = 10 - i  # 用来记录空格数
    print(' ' * j, end='')
    k = 1  # 用来记录星数
    while k < i:
        print('* ', end='')
        k += 1
    print('*')
