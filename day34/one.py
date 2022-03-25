# author: wp
# 2022年03月24日 19:56
# 能够使用闭包解决一元一次表达式y=a*x+b的多种a，b值问题

def func(a, b):
    def create_y(x):
        y = a * x + b
        print(y)
    return create_y


# 求解y=3x+4
func1 = func(3, 4)
func1(0)
func1(1)
func1(2)
