import pymysql

user = input("username:")
pwd = input("password:")

conn = pymysql.connect(host='localhost', user = 'root', password = '', database = 'day2')
cursor = conn.cursor(cursor = pymysql.cursors.DictCursor)
sql = "select yonghu.name,quanxian.depart from yonghu left join guanxi on yonghu.id = guanxi.id left join quanxian on guanxi.q_id = quanxian.q_id where name ='%s' and password ='%s' " %(user,pwd)
cursor.execute(sql)
result = cursor.fetchall()
cursor.close()
conn.close()

if result:
    print(result)
else:
    print("密码错误或查无此人！")
