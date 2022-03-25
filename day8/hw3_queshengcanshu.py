# 多个缺省参数的传递练习，练习多个缺省参数

# 缺省参数指：传参时可以不传对应参数
def print_info(name, gender=True):  # 默认gender为True

    gender_text = "男生"
    if not gender:
        gender_text = "女生"

    print("%s 是 %s" % (name, gender_text))


# 缺省参数放最后
def print_info1(name, title='', gender=True):

    gender_text = "男生"

    if not gender:
        gender_text = "女生"

    print("%s%s 是 %s" % (title, name, gender_text))


if __name__ == '__main__':
    print_info('xiaoming')
    print_info1('xiaoming', title="纪律委员")
    print_info1("小美", gender=False)
    print_info1("老王", title="班长")
