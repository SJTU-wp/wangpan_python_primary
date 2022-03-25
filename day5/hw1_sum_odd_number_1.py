# 实现从1到100间的奇数求和

i = 1
result = 0

while i <= 100:
    if i % 2 != 0:
        result += i
    i += 1

print("1到100之间的奇数和为：", result)
