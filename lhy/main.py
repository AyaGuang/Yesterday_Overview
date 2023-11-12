import socket
import sys
import struct
import time
import tcp
import threading
import _thread
import pymysql
import pymysql


#连接数据
def MySQLConnect():
    connection = pymysql.connect(
        host='123.57.208.119',  # IP，MySQL数据库服务器IP地址 后面换成局域网地址
        port=3307,  # 端口，默认3306，可以不输入
        user='Scrape',  # 数据库用户名
        password='5LAjfRFW3aecXn5h',  # 数据库登录密码
        database='scrape',  # 要连接的数据库
        charset='utf8'  # 字符集，注意不是'utf-8'
    )
    return connection

#插入数据到数据库
def AddData(grade):
    # 连接数据库
    conn = MySQLConnect()
    # 使用cursor()方法创建一个游标对象cursor
    cursor = conn.cursor()
    # 插入数据库
    sql = "INSERT INTO test(grade) VALUES (%s); "
    cursor.execute(sql, [grade])
    # 提交事务
    conn.commit()
    # 关闭游标
    cursor.close()
    # 关闭数据库连接
    conn.close()
def ReadData():
    # 连接数据库
    conn = MySQLConnect()
    # 使用cursor()方法创建一个游标对象cursor
    cursor = conn.cursor()
    # 读数据库
    cursor.execute('select * from scrape')

    aa = cursor.fetchall()
    print(aa)
    #cursor.execute(sql, [num, yb, wd, time])
    # 提交事务
    conn.commit()
    # 关闭游标
    cursor.close()
    # 关闭数据库连接
    conn.close()

if __name__ == '__main__':

    try:
        # MySQLConnect()
        ReadData()
        # AddData(50)
        # ReadData()
        print("连接成功")
    except:
        print("连接失败")
        sys.exit(1)