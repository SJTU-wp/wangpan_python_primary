# 个人名片
name = input("请输入姓名：")
company = input("请输入所在公司：")
title = input("请输入所任职位：")
phone = input("请输入电话：")
email = input("请输入邮箱：")

print("*" * 50)
print(company)
print()
print(name, '(', title, ')')
print()
print("电话：%s" % phone)
print("邮箱：%s" % email)
print("*" * 50)
