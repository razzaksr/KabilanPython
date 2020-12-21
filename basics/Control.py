'''
Control/ Decision making statements:
if condition:
	True statements
else:
	False statements
'''

prepaid = int(input("Tell us Tariff: "))

if prepaid >= 300:
    prepaid -= 50
    print("You can pay only", prepaid, "instead of", (prepaid + 50))
else:
    print("Can't redeem any coupen has to pay", prepaid)

balance=int(input("Account balance: "))
if prepaid<=balance:
    print(prepaid,"successfully purchased")
else:
    print("Insufficient balance in account")