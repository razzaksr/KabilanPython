# Nested Loop:

# tables

'''for tab in range(1,5):
    for num in range(1,11):
        print(num,"*",tab,"=",num*tab)'''

# Theatre Process
for show in range(1,5):
    seat = 10
    if show==1:
        stime=10.30
        etime=10.50
    elif show==2:
        stime=12.10
        etime=12.30
    elif show==3:
        stime=5.20
        etime=5.40
    elif show==4:
        stime=9.15
        etime=9.35
    sum = 0
    while seat > 0 and stime <= etime:
        print("Current time is:", stime)
        tic = int(input("Tell us how many tickets you want: "))
        if tic <= seat:
            req = tic * 120
            amt = int(input("Enter the amount: "))
            if amt >= req:
                print("You got your ticket(s)", tic,"for the show",show)
                seat -= tic
                sum += req
            else:
                print("Insufficient amount")
        else:
            print("Enter the ticket less than", seat)
        stime += 0.05
    else:
        print("Housefull/ Film is screening")
        print("Collected amount:", sum)