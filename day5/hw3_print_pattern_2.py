# 打印菱形2

# 打印前五行
for i in range(1, 6):  # 用来记录行数
    j = 5 - i  # 用来记录空格数
    print(' ' * j, end='')  # 打印该行行首空格
    k = 1  # 用来记录星数
    while k < i:
        print('* ', end='')  # 星号空格整体打印
        k += 1
    print('*')  # 每行最后一个星不带空格，并换行
# 打印后四行
for i in range(6, 10):
    i = 10 - i
    j = 5 - i
    print(' ' * j, end='')
    k = 1  # 用来记录星数
    while k < i:
        print('* ', end='')
        k += 1
    print('*')
print()


# 打印空心菱形2

# 打印前五行
for n in range(1, 6):  # 用来记录行数
    m = 5 - n  # 用来记录空格数
    if n == 1:
        print(' ' * m, end='')
        print('*')
    else:
        print(' ' * m, end='')
        print('*', end='')
        print(' ' * (2 * n - 3), end='')
        print('*')
# 打印后四行
for n in range(6, 10):  # 用来记录行数
    n = 10 - n
    m = 5 - n  # 用来记录空格数
    if n == 1:
        print(' ' * m, end='')
        print('*')
    else:
        print(' ' * m, end='')
        print('*', end='')
        print(' ' * (2 * n - 3), end='')
        print('*')
print()


# 打印空心菱形3

# 打印前五行
for p in range(1, 6):
    q = 5 - p
    print(' ' * q, end='')  # 打印该行行首空格
    r = 1  # 记录星的个数
    while r <= 2:
        if p == 1 or r == 2:  # 打印第一行/打印第二个星并换行
            print('*')
            break
        else:  # 打印第一个星及空心部分
            print('*', end='')
            r += 1
            print(' ' * (2 * p - 3), end='')
# 打印后四行
for p in range(6, 10):
    p = 10 - p
    q = 5 - p
    print(' ' * q, end='')  # 打印该行行首空格
    r = 1  # 记录星的个数
    while r <= 2:
        if p == 1 or r == 2:  # 打印第一行/打印第二个星并换行
            print('*')
            break
        else:  # 打印第一个星及空心部分
            print('*', end='')
            r += 1
            print(' ' * (2 * p - 3), end='')
