#print("Welcome to Object Oriented Programming")

'''name=input("Enter your name:")
age=int(input("Enter age:"))
gender=input("Enter gender:")
origin=input("Hailing from:")'''

'''print("Welcome,",name)
print("Age:",age)
print("Gender:",gender)
print("City:",origin)'''
#print("Welcome, %s\nAge:%d\nGender:%s\nCity:%s"%(name,age,gender,origin))

'''carname=input("Enter the car name:\n")
carno=int(input("Enter the car no:\n"))
carprice=float(input("Enter the price:\n"))

print("Carname:%s\nCarno:%d\nPrice:%.2f"%(carname,carno,carprice))'''

'''print("Enter the digits:")
num1=int(input())
num2=int(input())
num3=int(input())
num4=int(input())


print("%d-%c"%(num1,chr(num1)))
print("%d-%c"%(num2,chr(num2)))
print("%d-%c"%(num3,chr(num3)))
print("%d-%c"%(num4,chr(num4)))'''

origin=int(input("Enter the first number\n"))
count=int(input("Enter the nth number\n"))
sum=0
if origin>0 and count>0:
    for num in range(1, count + 1):
        if num%2==0:
            print("+%d"%origin,end="")
            sum+=origin
        else:
            print("-%d"%origin,end="")
            sum+=(-origin)
        #sum += origin
        origin += 1

    print("=%d"%sum)
else:print("Invalid Input")