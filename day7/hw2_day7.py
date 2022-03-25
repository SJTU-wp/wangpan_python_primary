# 编写代码理解 局部变量与全局变量

# 定义一个全局变量
number = 10


def demo1():
    num = 10
    print(num)
    num = 20
    print("修改后 %d" % num)


def demo2():
    num = 100
    print(num)
    # for或者while内定义的变量在函数内均有效
    for i in range(1):
        num1 = 200
    print(num1)  # 在for循环里定义虽然能用，但还是会有报错啊


def demo3():
    # number = 20  # 并没有修改到全局变量，只是定义了一个局部变量,内部使用是就近原则
    global number
    number = 35
    print(number)


def demo4():
    print(number)


# 局部变量修改相互之间不影响,局部变量在函数结束后释放
# 针对全局变量，读的时候可以不加，要修改时候，要加上global
demo1()
demo2()
demo3()
demo4()
