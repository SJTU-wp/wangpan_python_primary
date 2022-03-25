# 读取readme文件内容，复制到readme1中

file_read = open("readme", "r", encoding='utf8')
file_write = open("readme1", "w", encoding='utf8')

text = file_read.read()
file_write.write(text)

file_read.close()
file_write.close()
