num_dec = int(input('请输入一个十进制整型数：'))

num_bin = bin(num_dec)
num_oct = oct(num_dec)
num_hex = hex(num_dec)

print('十进制数', num_dec, '转换为二进制数为', num_bin, '，转换为八进制数为', num_oct, '，转换为十六进制数为', num_hex)
