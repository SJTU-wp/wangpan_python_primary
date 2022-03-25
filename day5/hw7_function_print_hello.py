# 定义函数打印多次hello

def say_hello():
    """该函数用于打印多次hello"""
    n = int(input("请输入打印次数："))
    print('hello\n' * n)


if __name__ == '__main__':
    say_hello()
