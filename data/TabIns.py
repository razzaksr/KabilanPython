from pymysql import *

con=connect(host='localhost',database='kabilan',user='root',passwd='')

print("---------------Welcome to TVS Service------------------")
reg=input('Tell us Registration number of the vehicle: ')
pick=input('Tell us date of pick for service(YYYY-MM-DD): ')
name=input('Tell us customer name: ')
mob=int(input('Tell us contact number: '))
probs=input("Tell us issues you have in this vehicle(seperate issues by ,): ")
expDay=int(input("Tell us expected delivery duration: "))
expBill=float(input("Approximatly expected bill: "))
#issue=probs.split(",")

qry="""insert into jobs(regnum,pick_date,cust_name,cust_contact,issues,expected,exp_bill) values('%s','%s','%s',%d,'%s',%d,%f)"""%\
    (reg,pick,name,mob,probs,expDay,expBill)
cur=con.cursor()
ack=cur.execute(qry)
con.autocommit(True)
if ack!=0:print(ack,"vehicle added into records")
else:print("can't add the vehicle")

con.close()