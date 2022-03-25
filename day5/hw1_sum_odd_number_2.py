# 实现从1到100间的奇数求和

result = 0

for i in range(1, 101):
    if i % 2 != 0:
        result += i

print("1到100间的奇数和为：", result)
