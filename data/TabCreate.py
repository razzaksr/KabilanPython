from pymysql import *

con=connect(host='localhost',database='kabilan',user='root',passwd='')

qry1 = "create table jobs(number int(4) not null, regnum varchar(50) not null,pick_date date not null, cust_name varchar(50) not null, cust_contact bigint(10) not null, issues text not null, expected int(4) not null, exp_bill double not null)"
qry2="ALTER TABLE jobs ADD PRIMARY KEY ( number )"
qry3="ALTER TABLE jobs CHANGE number number INT( 4 ) NOT NULL AUTO_INCREMENT"

cur=con.cursor()

cur.execute(qry1)
cur.execute(qry2)
cur.execute(qry3)

print("Table has created")

con.close()