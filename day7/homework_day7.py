# 将day7作业汇总到该.py文件下


def hw_3():
    """求两个有序数字列表的公共元素"""
    list3_1 = [i for i in range(10)]
    list3_2 = [j if j % 2 == 0 else j ** 2 for j in range(10)]
    print(list3_1)
    print(list3_2)
    for elem in list3_1:
        if elem in list3_2:
            print(elem, end=' ')
    print()


def hw_4():
    """给定一个n个整型元素的列表a，其中有一个元素出现次数超过n/2，求这个元素"""
    a = [1, 2, 3, 1, 1, 1, 4, 1, 6, 1]
    n = len(a)
    j = 0  # 计数
    for i in a:
        while a.count(i) > (n / 2) and j < 1:
            print("列表a中出现次数超过一半的元素为：", i)
            j += 1


def hw_6():
    """将元组 (1,2,3) 和集合 {4,5,6} 合并成一个列表"""
    list_join = list((1, 2, 3)) + list({4, 5, 6})
    print(list_join)


def hw_7():
    """在列表[1,2,3,4,5,6]首尾分别添加整型元素7和0"""
    list7 = [1, 2, 3, 4, 5, 6]
    list7.insert(0, 7)
    list7.append(0)
    print(list7)


def hw_8():
    """反转列表 [0,1,2,3,4,5,6,7]"""
    list8 = [0, 1, 2, 3, 4, 5, 6, 7]
    list8.reverse()
    print(list8)


def hw_9():
    """反转列表 [0,1,2,3,4,5,6,7] 后给出中元素 5 的索引号"""
    list9 = [0, 1, 2, 3, 4, 5, 6, 7]
    list9.reverse()
    print(list9.index(5))


def hw_10():
    """分别统计列表 [True,False,0,1,2] 中 True,False,0,1,2的元素个数，发现了什么"""
    list10 = [True, False, 0, 1, 2]
    for i in range(len(list10)):
        print("%s的元素个数为：%d " % (list10[i], list10.count(list10[i])))


def hw_11():
    """从列表 [True,1,0,‘x’,None,‘x’,False,2,True] 中删除元素‘x’"""
    list11 = [True, 1, 0, 'x', None, 'x', False, 2, True]
    while list11.count('x') != 0:
        list11.remove('x')
    print(list11)


def hw_12():
    """从列表 [True,1,0,‘x’,None,‘x’,False,2,True] 中删除索引号为4的元素"""
    list12 = [True, 1, 0, 'x', None, 'x', False, 2, True]
    list12.pop(4)
    print(list12)


def hw_13():
    """删除列表中索引号为奇数（或偶数）的元素"""
    list13 = [x for x in range(10)]
    list13_del_index_odd = []
    for i in range(len(list13)):
        if i % 2 == 0:
            list13_del_index_odd.append(list13[i])
    print(list13_del_index_odd)


def hw_14():
    """清空列表中的所有元素"""
    list14 = [x for x in range(10)]
    print(list14.clear())


def hw_15():
    """对列表 [3,0,8,5,7] 分别做升序和降序排列"""
    list15 = [3, 0, 8, 5, 7]
    list15.sort()
    print(list15)
    list15.sort(reverse=True)
    print(list15)


def hw_16():
    """将列表 [3,0,8,5,7] 中大于 5 元素置为1，其余元素置为0"""
    list16 = [3, 0, 8, 5, 7]
    list16_rewrite = [1 if list16[i] > 5 else 0 for i in range(len(list16))]
    print(list16_rewrite)


def hw_17():
    """遍历列表 [‘x’,‘y’,‘z’]，打印每一个元素及其对应的索引号"""
    list17 = ['x', 'y', 'z']
    for elem in list17:
        print(elem, '对应的索引值为：', list17.index(elem))


def hw_18():
    """将列表 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 拆分为奇数组和偶数组两个列表"""
    list18 = [i for i in range(0, 10)]
    list18_odd = [elem for elem in list18 if elem % 2 != 0]
    list18_even = [elem for elem in list18 if elem % 2 == 0]
    print("原列表拆分为奇数组和偶数组分别为：", list18_odd, list18_even)


def hw_19():
    """分别根据每一行的首元素和尾元素大小对二维列表 [[6, 5], [3, 7], [2, 8]] 排序"""
    list_19 = [[6, 5], [3, 7], [2, 8]]
    print("根据每一行的首元素排序得：", sorted(list_19, key=lambda x: x[0]))
    print("根据每一行的尾元素排序得：", sorted(list_19, key=lambda x: x[-1]))


def hw_20():
    """从列表 [1,4,7,2,5,8] 索引为3的位置开始，依次插入列表 [‘x’,‘y’,‘z’] 的所有元素"""
    list20 = [1, 4, 7, 2, 5, 8]
    list20_1 = ['x', 'y', 'z']
    list20_1.reverse()
    for elem in list20_1:
        list20.insert(3, elem)
    print(list20)


def hw_21():
    """快速生成由 [5,50) 区间内的整数组成的列表"""
    list21 = [i for i in range(5, 50)]
    print(list21)


def hw_23():
    """将列表 [‘x’,‘y’,‘z’] 和 [1,2,3] 转成 [(‘x’,1),(‘y’,2),(‘z’,3)] 的形式"""
    a = ['x', 'y', 'z']
    b = [1, 2, 3]
    list23 = [(a[i], b[i]) for i in range(3)]
    print(list23)


def hw_24():
    """以列表形式返回字典 {‘Alice’: 20, ‘Beth’: 18, ‘Cecil’: 21} 中所有的键"""
    dict24 = {'Alice': 20, 'Beth': 18, 'Cecil': 21}
    print(dict24.keys())


def hw_25():
    """以列表形式返回字典 {‘Alice’: 20, ‘Beth’: 18, ‘Cecil’: 21} 中所有的值"""
    dict25 = {'Alice': 20, 'Beth': 18, 'Cecil': 21}
    print(dict25.values())


def hw_26():
    """以列表形式返回字典 {‘Alice’: 20, ‘Beth’: 18, ‘Cecil’: 21} 中所有键值对组成的元组"""
    dict26 = {'Alice': 20, 'Beth': 18, 'Cecil': 21}
    print(dict26.items())


def hw_27():
    """向字典 {‘Alice’: 20, ‘Beth’: 18, ‘Cecil’: 21} 中追加 ‘David’:19 键值对，更新Cecil的值为17"""
    dict27 = {'Alice': 20, 'Beth': 18, 'Cecil': 21}
    dict27['David'] = 19
    dict27['Cecil'] = 17
    print(dict27)


def hw_28():
    """删除字典 {‘Alice’: 20, ‘Beth’: 18, ‘Cecil’: 21} 中的Beth键后，清空该字典"""
    dict28 = {'Alice': 20, 'Beth': 18, 'Cecil': 21}
    dict28.pop('Beth')
    print(dict28)
    dict28.clear()
    print(dict28)


def hw_29():
    """判断 David 和 Alice 是否在字典 {‘Alice’: 20, ‘Beth’: 18, ‘Cecil’: 21} 中"""
    dict29 = {'Alice': 20, 'Beth': 18, 'Cecil': 21}
    if 'David' in dict29:
        print("David在字典中")
    else:
        print("David不在字典中")
    if 'Alice' in dict29:
        print("Alice在字典中")
    else:
        print("Alice不在字典中")


def hw_30():
    """遍历字典 {‘Alice’: 20, ‘Beth’: 18, ‘Cecil’: 21}，打印键值对"""
    dict30 = {'Alice': 20, 'Beth': 18, 'Cecil': 21}
    for k in dict30:
        print("%s - %d" % (k, dict30[k]))


def hw_32():
    """以列表 [‘A’,‘B’,‘C’,‘D’,‘E’,‘F’,‘G’,‘H’] 中的每一个元素为键，默认值都是0，创建一个字典"""
    list32 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    dict32 = {}
    for i in list32:
        dict32[i] = 0
    print(dict32)


def hw_33():
    """将二维结构 [[‘a’,1],[‘b’,2]] 和 ((‘x’,3),(‘y’,4)) 转成字典"""
    list33 = [['a', 1], ['b', 2]]
    tuple33 = (('x', 3), ('y', 4))
    dict33 = {}
    for i in tuple33:
        list33.append(list(i))
    for j in list33:
        dict33[j[0]] = j[1]
    print(dict33)


def hw_34():
    """将元组 (1,2) 和 (3,4) 合并成一个元组"""
    tuple34 = (1, 2) + (3, 4)
    print(tuple34)


def hw_35():
    """将空间坐标元组 (1,2,3) 的三个元素解包对应到变量 x,y,z"""
    (x, y, z) = (1, 2, 3)
    # x, y, z = (1, 2, 3)
    print(x, y, z)


def hw_36():
    """返回元组 (‘Alice’,‘Beth’,‘Cecil’) 中 ‘Cecil’ 元素的索引号"""
    tuple36 = ('Alice', 'Beth', 'Cecil')
    print(tuple36.index('Cecil'))


def hw_37():
    """返回元组 (2,5,3,2,4) 中元素 2 的个数"""
    tuple37 = (2, 5, 3, 2, 4)
    print(tuple37.count(2))


def hw_38():
    """判断 ‘Cecil’ 是否在元组 (‘Alice’,‘Beth’,‘Cecil’) 中"""
    tuple38 = ('Alice', 'Beth', 'Cecil')
    if 'Cecil' in tuple38:
        print("Cecil在元组中")
    else:
        print("Cecil不在元组中")


def hw_39():
    """返回在元组 (2,5,3,7) 索引号为2的位置插入元素 9 之后的新元组"""
    tuple39 = (2, 5, 3, 7)
    list39 = list(tuple39)
    list39.insert(2, 9)
    print(tuple(list39))


def hw_40():
    """创建一个空集合，增加 {‘x’,‘y’,‘z’} 三个元素"""
    set40 = set()
    a = {'x', 'y', 'z'}
    set40.update(a)
    print(set40)


def hw_41():
    """删除集合 {‘x’,‘y’,‘z’} 中的 ‘z’ 元素，增加元素 ‘w’，然后清空整个集合"""
    set41 = {'x', 'y', 'z'}
    set41.discard('z')
    print(set41)
    set41.add('w')
    print(set41)
    set41.clear()
    print(set41)


def hw_42():
    """返回集合 {‘A’,‘D’,‘B’} 中未出现在集合 {‘D’,‘E’,‘C’} 中的元素（差集）"""
    set42_1 = {'A', 'D', 'B'}
    set42_2 = {'D', 'E', 'C'}
    set42 = set42_1.difference(set42_2)
    print(set42)


def hw_43():
    """返回两个集合 {‘A’,‘D’,‘B’} 和 {‘D’,‘E’,‘C’} 的并集"""
    set43_1 = {'A', 'D', 'B'}
    set43_2 = {'D', 'E', 'C'}
    set43 = set43_1.union(set43_2)
    print(set43)


def hw_44():
    """返回两个集合 {‘A’,‘D’,‘B’} 和 {‘D’,‘E’,‘C’} 的交集"""
    set44_1 = {'A', 'D', 'B'}
    set44_2 = {'D', 'E', 'C'}
    set44 = set44_1.intersection(set44_2)
    print(set44)


def hw_45():
    """返回两个集合 {‘A’,‘D’,‘B’} 和 {‘D’,‘E’,‘C’} 未重复的元素的集合"""
    set45_1 = {'A', 'D', 'B'}
    set45_2 = {'D', 'E', 'C'}
    set45 = set45_1.symmetric_difference(set45_2)
    print(set45)


def hw_46():
    """判断两个集合 {‘A’,‘D’,‘B’} 和 {‘D’,‘E’,‘C’} 是否有重复元素"""
    set46_1 = {'A', 'D', 'B'}
    set46_2 = {'D', 'E', 'C'}
    result = set46_1.isdisjoint(set46_2)  # 没有返回True，有则返回False
    print(result)


def hw_47():
    """判断集合 {‘A’,‘C’} 是否是集合 {‘D’,‘C’,‘E’,‘A’} 的子集"""
    set47_1 = {'A', 'C'}
    set47_2 = {'D', 'C', 'E', 'A'}
    result = set47_1.issubset(set47_2)
    print(result)


def hw_48():
    """去除数组 [1,2,5,2,3,4,5,‘x’,4,‘x’] 中的重复元素"""
    list48 = [1, 2, 5, 2, 3, 4, 5, 'x', 4, 'x']
    set48 = set(list48)
    print(list(set48))


def hw_49():
    """返回字符串 ‘abCdEfg’ 的全部大写、全部小写和大小写互换形式"""
    string49 = "abCdEfg"
    print(string49.upper())
    print(string49.lower())
    print(string49.swapcase())


def hw_50():
    """判断字符串 ‘abCdEfg’ 是否首字母大写，字母是否全部小写，字母是否全部大写"""
    string50 = "abCdEfg"
    print(string50.istitle())
    print(string50.islower())
    print(string50.isupper())


def hw_51():
    """返回字符串 ‘this is python’ 首字母大写以及字符串内每个单词首字母大写形式"""
    string51 = 'this is python'
    print(string51.title())


def hw_52():
    """判断字符串 ‘this is python’ 是否以 ‘this’ 开头，又是否以 ‘python’ 结尾"""
    string52 = 'this is python'
    print(string52.startswith('this'))
    print(string52.endswith('python'))


def hw_53():
    """返回字符串 ‘this is python’ 中 ‘is’ 的出现次数"""
    string53 = 'this is python'
    print(string53.count('is'))


def hw_54():
    """返回字符串 ‘this is python’ 中 ‘is’ 首次出现和最后一次出现的位置"""
    string54 = 'this is python'
    print(string54.find('is'))
    print(string54.rfind('is'))


def hw_55():
    """将字符串 ‘this is python’ 切片成3个单词"""
    string55 = 'this is python'
    print(string55.split())


def hw_56():
    """返回字符串 ‘blog.csdn.net/xufive/article/details/102946961’ 按路径分隔符切片的结果"""
    string56 = 'blog.csdn.net/xufive/article/details/102946961'
    print(string56.split('/'))


def hw_57():
    """将字符串 ‘2.72, 5, 7, 3.14’ 以半角逗号切片后，再将各个元素转成浮点型或整型"""
    string57 = '2.72, 5, 7, 3.14'
    list57 = string57.split(',')
    print(list57)
    for i in list57:
        if '.' in i:  # 利用浮点数的小数点特性加以区分
            i = float(i)
            print(i, type(i))
        else:
            i = int(i)
            print(i, type(i))


def hw_58():
    """判断字符串 ‘adS12K56’ 是否完全为字母数字，是否全为数字，是否全为字母"""
    string58 = 'adS12K56'
    print(string58.isalnum())
    print(string58.isdecimal())
    print(string58.isalpha())


def hw_59():
    """将字符串 ‘there is python’ 中的 ‘is’ 替换为 ‘are’"""
    string59 = 'there is python'
    print(string59.replace('is', 'are'))


def hw_60():
    """清除字符串 ‘\t python \n’ 左侧、右侧，以及左右两侧的空白字符"""
    string60 = '\t python \n'
    print(string60.lstrip())
    print(string60.rstrip())
    print(string60.strip())


def hw_61():
    """将三个全英文字符串（比如，‘ok’, ‘hello’, ‘thank you’）分行打印，实现左对齐、右对齐和居中对齐效果"""
    a = 'ok'
    b = 'hello'
    c = 'thank you'
    print(a + '\n' + b + '\n' + c)
    print()
    print(a.rjust(9) + '\n' + b.rjust(9) + '\n' + c.rjust(9))
    print()
    print(a.center(9) + '\n' + b.center(9) + '\n' + c.center(9))


def hw_62():
    """将三个字符串（比如，‘Hello, 我是David’, ‘OK, 好’, ‘很高兴认识你’）分行打印，实现左对齐、右对齐和居中效果"""
    a = 'Hello, 我是David'
    b = 'OK, 好'
    c = '很高兴认识你'
    print(a + '\n' + b + '\n' + c)
    print()
    print(a.rjust(14) + '\n' + b.rjust(15) + '\n' + c.rjust(12))
    print()
    print(a.center(14) + '\n' + b.center(16) + '\n' + c.center(12))


def hw_63():
    """将三个字符串 ‘15’, ‘127’, ‘65535’ 左侧补0成同样长度"""
    a = '15'
    b = '127'
    c = '65535'
    a1 = a.rjust(5).replace(' ', '0')
    b1 = b.rjust(5).replace(' ', '0')
    c1 = c.rjust(5).replace(' ', '0')
    print(a1, b1, c1)


def hw_64():
    """将列表 [‘a’,‘b’,‘c’] 中各个元素用’|'连接成一个字符串"""
    list64 = ['a', 'b', 'c']
    print('|'.join(list64))


def hw_65():
    """将字符串 ‘abc’ 相邻的两个字母之间加上半角逗号，生成新的字符串"""
    string65 = 'abc'
    print(','.join(string65))


def hw_66():
    """从键盘输入手机号码，输出形如 ‘Mobile: 186 6677 7788’ 的字符串"""
    a = str(input("请输入手机号码："))
    print('Mobile:', a[0: 3], a[3: 7], a[7:])


def hw_67():
    """从键盘输入年月日时分秒，输出形如 ‘2019-05-01 12:00:00’ 的字符串"""
    def format_67(a, n):
        return a.rjust(n).replace(' ', '0')

    year = input("请输入年份：")
    month = input("请输入月份：")
    day = input("请输入哪天：")
    hour = input("请输入时：")
    minute = input("请输入分：")
    second = input("请输入秒：")
    print('%s-%s-%s %s:%s:%s' % (format_67(year, 4), format_67(month, 2),
                                 format_67(day, 2), format_67(hour, 2),
                                 format_67(minute, 2), format_67(second, 2)))


def hw_68():
    """给定两个浮点数 3.1415926 和 2.7182818，格式化输出字符串 ‘pi = 3.1416, e = 2.7183’"""
    print('pi = %.4f, e = %.4f' % (3.1415926, 2.7182818))


def hw_69():
    """将 0.00774592 和 356800000 格式化输出为科学计数法字符串"""
    print('%e %e' % (0.00774592, 356800000))


def hw_70():
    """将列表 [0,1,2,3.14,‘x’,None,’’,list(),{5}] 中各个元素转为布尔型"""
    list70 = [0, 1, 2, 3.14, 'x', None, '', list(), {5}]
    list70_1 = [bool(a) for a in list70]
    print(list70_1)


def hw_71():
    """返回字符 ‘a’ 和 ‘A’ 的ASCII编码值"""
    print("字符'a'和'A'的ASCII编码值分别为：", ord('a'), ord('A'))


def hw_72():
    """返回ASCII编码值为 57 和 122 的字符"""
    print('ASCII编码值为57和122的字符分别为：', chr(57), chr(122))


def hw_73():
    """将列表 [3,‘a’,5.2,4,{},9,[]] 中大于3的整数或浮点数置为1，其余置为0"""
    list73 = [3, 'a', 5.2, 4, {}, 9, []]
    list73_1 = []
    for i in list73:
        if (type(i) is int or type(i) is float) and i > 3:
            list73_1.append(1)
        else:
            list73_1.append(0)
    print(list73_1)


def hw_74():
    """将二维列表 [[1], [‘a’,‘b’], [2.3, 4.5, 6.7]] 转为 一维列表"""
    list74 = [[1], ['a', 'b'], [2.3, 4.5, 6.7]]
    list74_1 = [j for i in list74 for j in i]
    print(list74_1)


def hw_75():
    """将等长的键列表和值列表转为字典"""
    list_keys = ["name", "age", "height", "gender"]
    list_values = ["xiaoming", 17, 1.78, "man"]
    dict75 = {}
    for i in range(len(list_keys)):
        dict75[list_keys[i]] = list_values[i]
    print(dict75)


def hw_76():
    """数字列表求和"""
    list76 = [i for i in range(20)]
    print(sum(list76))


if __name__ == '__main__':
    print('第3题：')
    hw_3()
    print('-' * 50)
    print('第4题：')
    hw_4()
    print('-' * 50)
    print('第6题：')
    hw_6()
    print('-' * 50)
    print('第7题：')
    hw_7()
    print('-' * 50)
    print('第8题：')
    hw_8()
    print('-' * 50)
    print('第9题：')
    hw_9()
    print('-' * 50)
    print('第10题：')
    hw_10()
    print('-' * 50)
    print('第11题：')
    hw_11()
    print('-' * 50)
    print('第12题：')
    hw_12()
    print('-' * 50)
    print('第13题：')
    hw_13()
    print('-' * 50)
    print('第14题：')
    hw_14()
    print('-' * 50)
    print('第15题：')
    hw_15()
    print('-' * 50)
    print('第16题：')
    hw_16()
    print('-' * 50)
    print('第17题：')
    hw_17()
    print('-' * 50)
    print('第18题：')
    hw_18()
    print('-' * 50)
    print('第19题：')
    hw_19()
    print('-' * 50)
    print('第20题：')
    hw_20()
    print('-' * 50)
    print('第21题：')
    hw_21()
    print('-' * 50)
    print('第23题：')
    hw_23()
    print('-' * 50)
    print('第24题：')
    hw_24()
    print('-' * 50)
    print('第25题：')
    hw_25()
    print('-' * 50)
    print('第26题：')
    hw_26()
    print('-' * 50)
    print('第27题：')
    hw_27()
    print('-' * 50)
    print('第28题：')
    hw_28()
    print('-' * 50)
    print('第29题：')
    hw_29()
    print('-' * 50)
    print('第30题：')
    hw_30()
    print('-' * 50)
    print('第32题：')
    hw_32()
    print('-' * 50)
    print('第33题：')
    hw_33()
    print('-' * 50)
    print('第34题：')
    hw_34()
    print('-' * 50)
    print('第35题：')
    hw_35()
    print('-' * 50)
    print('第36题：')
    hw_36()
    print('-' * 50)
    print('第37题：')
    hw_37()
    print('-' * 50)
    print('第38题：')
    hw_38()
    print('-' * 50)
    print('第39题：')
    hw_39()
    print('-' * 50)
    print('第40题：')
    hw_40()
    print('-' * 50)
    print('第41题：')
    hw_41()
    print('-' * 50)
    print('第42题：')
    hw_42()
    print('-' * 50)
    print('第43题：')
    hw_43()
    print('-' * 50)
    print('第44题：')
    hw_44()
    print('-' * 50)
    print('第45题：')
    hw_45()
    print('-' * 50)
    print('第46题：')
    hw_46()
    print('-' * 50)
    print('第47题：')
    hw_47()
    print('-' * 50)
    print('第48题：')
    hw_48()
    print('-' * 50)
    print('第49题：')
    hw_49()
    print('-' * 50)
    print('第50题：')
    hw_50()
    print('-' * 50)
    print('第51题：')
    hw_51()
    print('-' * 50)
    print('第52题：')
    hw_52()
    print('-' * 50)
    print('第53题：')
    hw_53()
    print('-' * 50)
    print('第54题：')
    hw_54()
    print('-' * 50)
    print('第55题：')
    hw_55()
    print('-' * 50)
    print('第56题：')
    hw_56()
    print('-' * 50)
    print('第57题：')
    hw_57()
    print('-' * 50)
    print('第58题：')
    hw_58()
    print('-' * 50)
    print('第59题：')
    hw_59()
    print('-' * 50)
    print('第60题：')
    hw_60()
    print('-' * 50)
    print('第61题：')
    hw_61()
    print('-' * 50)
    print('第62题：')
    hw_62()
    print('-' * 50)
    print('第63题：')
    hw_63()
    print('-' * 50)
    print('第64题：')
    hw_64()
    print('-' * 50)
    print('第65题：')
    hw_65()
    print('-' * 50)
    print('第66题：')
    hw_66()
    print('-' * 50)
    print('第67题：')
    hw_67()
    print('-' * 50)
    print('第68题：')
    hw_68()
    print('-' * 50)
    print('第69题：')
    hw_69()
    print('-' * 50)
    print('第70题：')
    hw_70()
    print('-' * 50)
    print('第71题：')
    hw_71()
    print('-' * 50)
    print('第72题：')
    hw_72()
    print('-' * 50)
    print('第73题：')
    hw_73()
    print('-' * 50)
    print('第74题：')
    hw_74()
    print('-' * 50)
    print('第75题：')
    hw_75()
    print('-' * 50)
    print('第76题：')
    hw_76()
    print('-' * 50)


# for i in range(1, 77):
#     print("hw_%d()" % i)
#     print("print('-' * 50)")

# for i in range(11, 77):
#     print("def hw_%d():" % i)
#     print('\t""""""')
#     print()
#     print()
