#-*- coding: UTF-8 -*-
# 导包
import pymysql
# 获取连接对象
conn = pymysql.connect(host='172.17.100.200',
                       port=3306,
                       user='root',
                       password='2020nji9VFR$',
                       db='smart-parking-operation')
# 获取游标对象
cursor = conn.cursor()

# 执行SQL语句
sql = "SELECT * FROM t_op_parking WHERE code='PR010072';"
result = cursor.execute(sql)

# 获取查询结果并断言

# 关闭游标对象
cursor.close()
# 关闭连接对象
conn.close()