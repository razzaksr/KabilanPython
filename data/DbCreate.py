from pymysql import *

con=connect(host='localhost',user='root',passwd='')

qry="create database kabilan"

cur=con.cursor()

cur.execute(qry)

print("Database has created")

con.close()