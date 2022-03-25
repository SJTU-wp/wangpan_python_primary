# 通过readline依次读取文件每一行并打印

file4 = open("file4.txt", mode='r+', encoding='utf8')

# file4.write("人生苦短 我用Python\n仰天大笑出门去，我辈岂是蓬蒿人\n"
#             "纵有疾风起，人生不言弃")

while True:
    # 读取一行内容
    text = file4.readline()

    # 判断是否读到内容
    if not text:
        break

    # 打印
    print(text, end='')

file4.close()
