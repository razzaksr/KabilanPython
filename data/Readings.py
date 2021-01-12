from pymysql import *

con=connect(host='localhost',user='root',passwd='',database='kabilan')

# SELECT COLUMN(S) FROM TABLE WHERE SPECIFIC ROWS

# Read All Rows All Column Query
#qry="select * from jobs"

'''
# Read All rows Specific Column query
what=input("Tell us what category you want(number,regnum,pick_date,cust_name,cust_contact,issues,expected,exp_bill): ")
qry="select %s from jobs"%(what)
'''

'''
# Read Specific row(s) with all columns query
job=int(input("Tell us job numer: "))
qry="select * from jobs where number=%d"%(job)
'''

'''
# Read Specific row(s) with all columns query
problem=input("Tell us issue: ")
qry="select * from jobs where issues like '%"+problem+"%'"
'''


# Read specific row(s) with specific column query
what=input("Tell us which detail you want: ")
basis=input("Tell us on what basis you need: ")
value=input("Tell us value for: "+basis)

if basis == 'issues':
    qry="select "+what+" from jobs where "+basis+" like '%"+value+"%'"
elif basis == 'pick_date':
    qry="select %s from jobs where %s > '%s'"%(what,basis,value)
else:
    qry = "select %s from jobs where %s='%s'" % (what, basis, value)

cur=con.cursor()

cur.execute(qry)

# Read specific row(s) with specific column execution
result=cur.fetchall()
for x in result:
    print(x[0])

'''
# Read Specific row(s) with all columns Execution
result=cur.fetchall()
for x in result:
    print(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7])
'''

'''
# Read Specific row(s) with all columns Execution
result=cur.fetchone()

print(result[0],result[1],result[2],result[3],result[4],result[5],result[6],result[7])
'''

'''
# Read All rows Specific Column Execution
result=cur.fetchall()
for x in result:
    print(x[0])
'''

'''
# Read all rows all column execution
result=cur.fetchall()

for x in result:
    print(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7])
'''

con.close()