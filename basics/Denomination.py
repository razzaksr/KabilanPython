# Denomination

t2000count=6
f500count=10
t200count=20
o100count=50

#print(t2000count*2000 + f500count*500 + t200count*200 +o100count*100)
status=""
user=int(input("Tell us amount to withdraw: "))# 14500
res=user
if user>0:
    req=user//2000
    if req<=t2000count:
        user-=req*2000
        t2000count-=req
        status+="2000 X "+str(req)+"\n"
    else:
        user-=(t2000count*2000)
        status += "2000 X " + str(t2000count)+"\n"
        t2000count=0
if user>0:
    req=user//500
    if req<=f500count:
        user-=req*500
        f500count-=req
        status+="500 X "+str(req)+"\n"
    else:
        user-=(f500count*500)
        status += "500 X " + str(f500count)+"\n"
        f500count=0
if user>0:
    req=user//200
    if req<=t200count:
        user-=req*200
        t200count-=req
        status+="200 X "+str(req)+"\n"
    else:
        user-=(t200count*200)
        status += "200 X " + str(t200count)+"\n"
        t200count=0
if user>0:
    req=user//100
    if req<=o100count:
        user-=req*100
        o100count-=req
        status+="100 X "+str(req)+"\n"
    else:
        user-=(o100count*100)
        status += "100 X " + str(o100count)+"\n"
        o100count=0

if user>0:
    print("can't provide",res)
else:
    print(res,"can be provided by following denom's",status)