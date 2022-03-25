# 练习open的a+，w+模式，感受他们与r+的区别

# w+如果文件存在会被覆盖
# 如果文件不存在，创建新文件
file7 = open("file7.txt", mode='w+', encoding='utf8')
file7.write("Hello, python!")

# a+如果该文件已存在，文件指针将会放在文件的结尾
# 如果文件不存在，创建新文件进行写入
file7 = open("file7.txt", mode='a+', encoding='utf8')
file7.write("wo shi a+")

# r+文件的指针将会放在文件的开头
# 如果文件不存在，抛出异常
file7 = open("file7.txt", mode='r+', encoding='utf8')
file7.write("wo shi r+")

file7.close()
