# author: wp
# 2022年03月10日 21:53
# 匹配一行文字中的开头的数字内容

import re

text = '0523王攀的出生年份1999'
ret = re.match('[0-9]*', text)
print(ret.group())
