# author: wp
# 2022年03月10日 22:19
# 只匹配包含字母和数字的行

import re

str1 = """<div>
<p>岗位职责：</p>
<p>完成推荐算法、数据统计、接口、后台等服务器端相关工作</p>
<p><br></p>
<p>必备要求：</p>
<p>良好的自我驱动力和职业素养，工作积极主动、结果导向</p>
<p> <br></p>
<p>技术要求：</p>
<p>1、一年以上 Python 开发经验，掌握面向对象分析和设计，了解设计模式</p>
<p>2、掌握HTTP协议，熟悉MVC、MVVM等概念以及相关WEB开发框架</p>
<p>3、掌握关系数据库开发设计，掌握 SQL，熟练使用 MySQL/PostgreSQL 中的一种<br></p>
<p>4、掌握NoSQL、MQ，熟练使用对应技术解决方案</p>
<p>5、熟悉 Javascript/CSS/HTML5，JQuery、React、Vue.js</p>
<p> <br></p>
<p>加分项：</p>
<p>大数据，数理统计，机器学习，sklearn，高性能，大并发345。</p>
</div> 
"""
list1 = re.split('\n', str1)  # 先将行与行分割开，存到一个列表中
# print(list1)
for line in list1:
    ret = re.search(r'.*\d+.*[a-zA-Z]+.*|.*[a-zA-Z]+.*\d+.*', line)
    if ret:
        print(ret.group())
