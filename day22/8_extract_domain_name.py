# author: wp
# 2022年03月10日 23:19
# 将给定网址提取出域名

import re

str1 = """http://www.interoem.com/messageinfo.asp?id=35`
http://3995503.com/class/class09/news_show.asp?id=14
http://lib.wzmc.edu.cn/news/onews.asp?id=769
http://www.zy-ls.com/alfx.asp?newsid=377&id=6
http://www.fincm.com/newslist.asp?id=415
"""
list1 = re.split('\n', str1)  # 先将行与行分割开，存到一个列表中

for line in list1:
    ret = re.search(r'(?<=//)([^/]+)', line)  # (?<=y)x 匹配x仅当x前面是y
    if ret:
        print(ret.group())
