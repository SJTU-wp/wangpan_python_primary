# author: wp
# 2022年03月11日 19:48
import re

test_str = '<img data-original="https://rpic.douyucdn.cn/appCovers/2016/11/13/1213973_201611131917_samll.jpg" ' \
           'src="https://rpic.douyucdn.cn/appCovers/2016/11/13/1213973_201611131917_samll.jpg" style="display: ' \
           'inlines;"> '

str1 = re.search(r"https://.*?\.jpg", test_str)

str2 = str1.group()
print(str2)

str3 = re.search(r"https://.*\/", str2)
print(str3.group())

str4 = re.search(r"https://.*?/", str2)
print(str4.group())
