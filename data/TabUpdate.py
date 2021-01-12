from pymysql import *

#reg=input("Tell us your registration numbe rof vehicle: ")
problem=input("Tell us problem which gonna cause extra amount: ")
amount=int(input("Tell us extra amount gonna put for "+problem))

con=connect(host='localhost',database='kabilan',user='root',passwd='')

con.autocommit(True)

#qry="update jobs set expected=expected+2 where issues like '%General service%'"
#qry="update jobs set exp_bill=exp_bill+500 where regnum='%s'"%(reg)
qry="update jobs set exp_bill=exp_bill+"+str(amount)+" where issues like '%"+problem+"%'"

cur=con.cursor()

ack=cur.execute(qry)

if ack!=0:print("Updated")
else:print("Not updated")

con.close()