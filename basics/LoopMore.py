# Another real time example

#for seats in range(1,16):
'''seats=1
while seats<=15:
    amt=int(input("Tell us amount to book ticket: "))
    if amt>= 190:
        print("Ticket Booked @",seats)
        seats+=1
    else:print("Insufficient amount")'''

'''seats=1
while seats<=30:
    if seats%5!=0 and seats%2!=0:
        amt = int(input("Tell us amount to book ticket: "))
        if amt >= 190:
            print("Ticket Booked @", seats)
            seats += 1
        else:
            print("Insufficient amount")
    else:
        seats += 1
        continue#break'''

hire=20

while hire>0:
    skill=input("Tell us skill set you knew: ")
    poc=int(input("Tell us how may POC done on "+skill+": "))
    if (skill=='java' or skill=='python') and poc>=4:
        print("You are recruited to our company")
        hire-=1
    else:
        print("Try to update skill/ work more POC")