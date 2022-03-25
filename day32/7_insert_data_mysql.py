# author: wp
# 2022年03月24日 13:03
# 使用python程序向数据表中加入十万条数据

from pymysql import connect


def main():
    conn = connect(host='192.168.181.128', port=3306, database='day32_hw', user='root', password='151508',
                   charset='utf8')

    cursor = conn.cursor()

    for i in range(100000):
        cursor.execute("insert into test_index values('ha-%d')" % i)

    conn.commit()


if __name__ == '__main__':
    main()
