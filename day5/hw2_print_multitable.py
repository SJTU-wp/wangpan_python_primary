# 打印九九乘法表

i = 1

while i <= 9:
    j = 1  # 刚开始放错位置了
    while j <= i:  # 刚开始手误打成j<=9
        print(i, "*", j, "=", i*j, end='\t')
        j += 1
    i += 1
    print()
