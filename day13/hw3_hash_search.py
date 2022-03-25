# author: wp
# 2022年02月28日 23:17
# 通过自己写的hash函数，实现圣经前10的词频统计

MAX_KEY = 100000


def elf_hash(hash_str):
    h = 0
    for i in hash_str:
        h = (h << 4) + ord(i)
        g = h & 0xf0000000
        if g:
            h ^= g >> 24
        h &= ~g
    return h % MAX_KEY


# 格式化字符串；易错：字符串作为不可变数据类型，在函数内部修改局部变量的引用，不会影响到外部变量的引用
def clear_str(str_out):
    string = str_out
    clear_list = [',', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '[', ']', "'", '.', ':', ';', '?', '(', ')']
    for i in clear_list:
        string = string.replace(i, ' ')
    return string


def use_hash():
    file = open('The_Holy_Bible.txt', 'r')
    str_bible = file.read().lower()
    str_list = clear_str(str_bible).split()
    hash_table = [[None]] * MAX_KEY
    count_dict = {}  # 若存在哈希冲突的话，哈希表中无法再添加一列计数

    for i in str_list:
        if hash_table[elf_hash(i)][0] and i not in hash_table[elf_hash(i)]:  # 拉链法解决哈希冲突
            hash_table[elf_hash(i)].append(i)
        elif i in hash_table[elf_hash(i)]:
            pass
        else:
            hash_table[elf_hash(i)][0] = i

    for i in str_list:  # 初始化
        count_dict[i] = 0
    for i in str_list:
        if hash(i):
            count_dict[i] += 1

    result = sorted(count_dict.items(), key=lambda x: x[1], reverse=True)
    print("圣经中词频前十的单词及其出现次数分别为：{}".format(result[0:10]))


if __name__ == '__main__':
    use_hash()
