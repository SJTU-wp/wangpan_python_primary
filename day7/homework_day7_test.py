# set1 = {1, 2, 3}
# list1 = list(set1)
# print(list1)
# list_join = list((1, 2, 3)) + list({4, 5, 6})
# print(list_join)
#
# list10 = [True, False, 0, 1, 2]
# for i in range(len(list10)):
#     print("%s的元素个数为：%d " % (list10[i], list10.count(list10[i])))

# 错误案例
# list13 = [x for x in range(10)]
# list13_del_index_odd = [list13[i] if i % 2 == 0 else '' for i in range(len(list13))]
# print(list13_del_index_odd)

# list3_1 = [i for i in range(10)]
# list3_2 = [j if j % 2 == 0 else j ** 2 for j in range(10)]
# print(list3_1)
# print(list3_2)
# for elem in list3_1:
#     if elem in list3_2:
#         print(elem, end=' ')

# import homework_day7
#
# homework_day7.hw_74()
# homework_day7.hw_75()
# a = [i if i % 2 == 0 for i in range(10)]
# print(a)
# a = [i for i in range(10) if i % 2 == 0]
# print(a)
for i in range(1, 77):
    print("print('第%d题：')" % i)
    print("hw_%d()" % i)
    print("print('-' * 50)")
