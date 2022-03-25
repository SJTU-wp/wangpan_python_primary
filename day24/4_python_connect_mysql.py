# author: wp
# 2022年03月13日 23:07
# python连接mysql

from pymysql import *

# 创建Connection连接
con = connect(host='192.168.181.128', port=3306, database='day24_hw',
                   user='root', password='151508', charset='utf8')
# 获得Cursor对象
cs1 = con.cursor()

# 执行insert语句，并返回受影响的行数：添加一条数据
count = cs1.execute('insert into goods_cates(name) values("硬盘")')
# 打印受影响的行数
print(count)

count = cs1.execute('insert into goods_cates(name) values("光盘")')
print(count)

con.commit()

# 关闭Cursor对象
cs1.close()
# 关闭Connection对象
con.close()
