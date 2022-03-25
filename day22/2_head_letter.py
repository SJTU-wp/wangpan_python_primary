# author: wp
# 2022年03月10日 21:42
# 匹配一行文字中的开头的字母内容

import re

text = 'qwer, df 2 lian, automobile2022.03.10'
ret = re.match("[a-zA-Z]+", text)
print(ret.group())
