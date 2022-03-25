# author: wp
# 2022年03月10日 21:31
# 匹配以“www”起始且以“.com”/".edu"/".net"结尾的简单Web域名

import re

web_list = ['www.yahoo.com', 'www.sjtu.edu.cn', 'www.sjtu.edu', 'https://www.abc.org']
for web in web_list:
    ret = re.match(r'^www\.[\w]+\.(com|net|edu|cn|org)$', web)
    if ret:
        print('{} 符合要求'.format(ret.group()))
    else:
        print('{} 不符合要求'.format(web))
