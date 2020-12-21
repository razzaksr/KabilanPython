'''
Repeatation:
Series/patterns:
'''

'''for num in range(1,100+1,+2):
    #if num%2!=0:
    print(num)'''

'''for even in range(1,100+1):
    if even%2==0:
        print(even)'''

'''num1=0
num2=1

limit=int(input("Tell us how many fibonacci you want: "))
print(num1)
print(num2)

for fibo in range(3,limit+1):
    sum = num1 + num2
    print(sum)
    num1 = num2
    num2 = sum'''

'''data=int(input("Tell number wish to check for prime: "))
if data==2 or data==3 or data==5 or data==7 or data%2!=0 and data%3!=0 and data%5!=0 and data%7!=0:
    print(data,"is prime")
else:print(data,"not prime")'''

limit=int(input("Tell us limit to show prime numbers: "))
for data in range(2,limit+1):
    if data == 2 or data == 3 or data == 5 or data == 7 or data % 2 != 0 and data % 3 != 0 and data % 5 != 0 and data % 7 != 0:
        print(data,"is prime")