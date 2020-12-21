# Looping statement

hai=[12,78,98,56,3.4,'hello',33,8.9,12.4]

#for point in hai:print(point,end=" ")

'''for pos in range(len(hai)):
    print(hai[pos],end=" ")'''

'''for pos in range(3,len(hai)-2):
    print(hai[pos],end=" ")'''

'''for pos in range(0,len(hai),+2):
    print(hai[pos],end=" ")'''

'''for pos in range(len(hai)-1,-1,-1):
    print(hai[pos],end=" ")'''

pos=0
while pos<len(hai):
    print(hai[pos],end=" ")
    pos+=1