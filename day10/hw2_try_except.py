# 通过try进行异常捕捉，确保输入的内容一定是一个整型数
# 然后判断该整型数是否是对称数，12321就是对称数，123321也是对称数，否则就不是
# 非整型抛异常，非对称数抛不抛异常自行选择（也抛异常）

def is_symmetry_number(number):

    if number < 0:
        return print("负数不是对称数")
    else:
        str_num = str(number)
        str_num_reverse = str_num[::-1]  # 字符串逆序
        if str_num == str_num_reverse:  # 是对称数则返回
            return print("该整型数是对称数")
        print("主动抛出异常")
        raise Exception("该整型数不是对称数")


try:
    num = int(input("请输入一个整数："))
    print(num)
    is_symmetry_number(num)
except ValueError as result:
    print("%s 请输入正确的整数" % result)
except Exception as result:  # 用于接收抛出来的异常
    print(result)
finally:
    print("执行完成")
