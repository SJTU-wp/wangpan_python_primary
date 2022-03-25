# author: wp
# 2022年03月22日 23:32
# 理解sql注入原理，如何防止这种危险
# 用字符串直接拼接的方式写sql是非常危险的
# execute传参，可以防止sql注入

from pymysql import *


def main():
    find_name = input("请输入物品名称：")

    # 创建Connection连接
    conn = connect(host='192.168.181.128', port=3306,
                   user='root', password='151508', database='day24_hw', charset='utf8')
    # 获得Cursor对象
    cs1 = conn.cursor()

    # 非安全的方式
    # 输入 " 3 or 1=1"   (双引号也要输入)
    # sql = "select * from goods where price = %s" % find_name
    # print("""sql===>%s<====""" % sql)
    # 执行select语句，并返回受影响的行数：查询所有数据
    # count = cs1.execute(sql)

    # 安全的方式
    # 构造参数列表
    params = [find_name]
    # 执行select语句，并返回受影响的行数：查询所有数据
    count = cs1.execute('select * from goods where price=%s', params)
    # 注意：
    # 如果要是有多个参数，需要进行参数化
    # 那么params = [数值1, 数值2....]，此时sql语句中有多个%s即可

    # 打印受影响的行数
    print(count)
    # 获取查询的结果
    # result = cs1.fetchone()
    result = cs1.fetchall()
    # 打印查询的结果
    print(result)
    # 关闭Cursor对象
    cs1.close()
    # 关闭Connection对象
    conn.close()


if __name__ == '__main__':
    main()
