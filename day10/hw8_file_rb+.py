# 练习rb+模式，感受与r+模式的区别

# 二进制模式打开得到的是字节流，二进制模式下磁盘上存的是什么字符，直接拿出来
# 文本模式下，\r\n 拿出来是\n

file8 = open('file8.txt', mode='r+', encoding='utf8')
file8.write('hello\nworld')
file8.close()

file8 = open('file8.txt', mode='r+', encoding='utf8')
print(file8.read())
file8.close()

file8 = open('file8.txt', mode='rb+')
print(file8.read())
file8.close()
