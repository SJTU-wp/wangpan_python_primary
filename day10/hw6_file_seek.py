# 通过seek从文件开头偏移5个字节，然后把文件剩余内容读取

file6 = open('file6.txt', mode='w+', encoding='utf8')
file6.write("hello, python!")
file6.seek(5)
text = file6.read()
print(text)
file6.close()
