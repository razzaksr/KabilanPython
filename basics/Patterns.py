# Patterns
'''
1 2 3 4 5
6 7 8 9 10
11 12 13 14 15
16 17 18 19 20
21 22 23 24 25
'''
'''num=1
for row in range(1,6):
    for col in range(1,6):
        print(num,end=" ")
        num+=1
    print()'''

'''
#####
$$$$$
#####
$$$$$
#####
1 3 5 7 9
2 4 6 8 10
11 13 15 17 19
12 14 16 18 20
21 23 25 27 29
'''
'''
odd=1
even=2
for row in range(1,6):
    for col in range(1,6):
        if row%2==0:
            print(even,end=" ")#print("$",end=" ")
            even+=2
        else:#print("#",end=" ")
            print(odd,end=" ")
            odd+=2
    print()'''

# Floyds
'''
Left Upper Floyd
1
12
123
1234
12345
'''
'''
for row in range(1,6):
    for col in range(1,row+1):
        print(col,end="")
    print()'''

'''
12345
1234
123
12
1
'''
'''
for row in range(5,0,-1):
    for col in range(1,row+1):
        print(col,end="")
    print()
'''

'''
    A
   AB
  ABC
 ABCD
ABCDE
'''
'''
for row in range(1,6):
    alpha=65
    for space in range(4,row-1,-1):print(" ",end="")
    for data in range(1,row+1):
        print(chr(alpha),end="")
        alpha+=1
    print()'''

'''
ABCDE
 ABCD
  ABC
   AB
    A
'''
for row in range(5,0,-1):
    alpha=65
    for space in range(4,row-1,-1):print(" ",end="")
    for data in range(1,row+1):
        print(chr(alpha),end="")
        alpha+=1
    print()