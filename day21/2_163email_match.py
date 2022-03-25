# author: wp
# 2022年03月11日 23:27
# 163邮箱匹配

import re

email_list = ["xiaoWang@163.com", "xiaoWang@163.comheihei", ".com.xiaowang@qq.com"]

for email in email_list:
    ret = re.match(r'[a-zA-Z\d_]+@163\.com$', email)
    if ret:
        print("%s 是符合规定的邮件地址,匹配后的结果是:%s" % (email, ret.group()))
    else:
        print("%s 不符合要求" % email)
