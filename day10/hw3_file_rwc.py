# 以可读可写打开一个文件，然后写入“人生苦短 我用Python”，关闭文件

file3 = open("file3.txt", mode='w+', encoding='utf8')

file3.write("人生苦短 我用Python")

file3.close()
