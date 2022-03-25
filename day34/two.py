# author: wp
# 2022年03月24日 20:05
# 闭包变量nonlocal修饰的使用练习

x = 300


def func():
    x = 200
    print(x)

    def nonlocal_func():
        nonlocal x
        print(x)
        x = 100
        print(x)
    return nonlocal_func


func1 = func()  # 200
func1()  # 200 100
