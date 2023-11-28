import pandas as pd
import mysql.connector

# 读取CSV文件
df = pd.read_csv('/Users/linhongyu/Downloads/zhihu.csv')

# 连接到MySQL数据库
conn = mysql.connector.connect(
    host='123.57.208.119',
    user='YesDB',
    password='RpXaFEnHMwnZSbSN',
    database='yesdb'
)

# 创建游标对象
cursor = conn.cursor()

# 插入数据到MySQL数据库
for index, row in df.iterrows():
    # 提取CSV文件中的数据
    title = row['title']
    pageview = row['PageView']
    appType = row['appType']
    date = row['date']
    src = row['src']
    rank = row['rank']
    cover = row['cover']
    up = row['up']

    # 构建插入数据的SQL语句
    sql = "INSERT INTO zhihu (title, pageview, appType, date, src, rank, cover, up) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    val = (title, pageview, appType, date, src, rank, cover, up)

    # 执行插入操作
    cursor.execute(sql, val)

# 提交更改并关闭游标和连接
conn.commit()
cursor.close()
conn.close()

print("数据上传完成")
