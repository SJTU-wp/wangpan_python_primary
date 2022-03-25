# 完成名片管理系统（原理简单，就是繁琐）

import hw11_cards_tools

while True:

    # USER（小明）处显示功能菜单
    hw11_cards_tools.show_menu()

    action = input("请选择操作功能：")
    print("您选择的操作是【%s】" % action)

    # 1,2,3 针对名片的操作
    if action in ["1", "2", "3"]:

        # 新增名片
        if action == "1":
            hw11_cards_tools.new_card()
        # 显示全部
        elif action == "2":
            hw11_cards_tools.show_all()
        # 查询名片
        elif action == "3":
            hw11_cards_tools.search_card()

    # 0 退出系统
    elif action == "0":

        print("欢迎再次使用【名片管理系统】")

        break

    # 其他内容输入错误，需要提示用户
    else:
        print("您输入的不正确，请重新选择")


# 如果在开发程序时，不希望立刻编写分支内部的代码
# 可以使用 pass 关键字，表示一个占位符，能够保证程序的代码结构正确！
# 程序运行时，pass 关键字不会执行任何的操作！
# pass
