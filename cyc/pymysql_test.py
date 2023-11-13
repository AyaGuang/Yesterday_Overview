import pymysql

# 创建连接
conn = pymysql.connect(host="127.0.0.1", port=3306, user='root', passwd='123456', db='bilibili', charset='utf8mb4')
# 检查连接是否成功
if conn.open:
    print("数据库连接成功")
else:
    print("数据库连接失败")
# 创建游标
cursor = conn.cursor()
# 执行SQL查询
cursor.execute("SELECT * FROM bili")
# 获取查询结果
result = cursor.fetchall()
cur=len(result)
resou = [(cur+1, '卢本伟复播'), (cur+2, '萝卜刀'),(cur+3, '原神启动'), (cur+4, 'FAKER退役'),(cur+5, 'UZI转会')]
# 执行SQL，返回受影响的行数，一次插入多行数据
cursor.executemany("insert into bili (id, name) values (%s, %s)", resou)
# 执行SQL查询
cursor.execute("SELECT * FROM bili")
# 获取查询结果
result = cursor.fetchall()
# 打印查询结果
for row in result:
    print(row)
# 提交保存
conn.commit()
# 关闭游标
cursor.close()
# 关闭连接
conn.close()