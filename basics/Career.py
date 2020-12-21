# Zealous Career Consultant

category=input("Tell us Programmer/ Support")
if category=='Programmer':
    tech=input("Tell us which programming technology wish to learn: ")
    print("U have chosen", tech)
    if tech == 'java' or tech=='JAVA':
        role=input("What kind of role you are expect in "+tech)
        if role == 'web developer':print("2 months duration with 3 POC")
        elif role == 'app developer':print("3 months duration with 2POC")
        elif role == 'windows developer':print("1 month duration with 1 POC")
        else:print(role,"can't play with",tech)
    elif tech=='python' or tech=='PYTHON':
        role = input("What kind of role you are expect in " + tech)
        if role == 'web developer':
            print("2 months duration with 3 POC")
        elif role == 'data scientist':
            print("6 months duration with 2POC")
        elif role == 'automation engineer':
            print("4 month duration with 1 POC")
        else:
            print(role, "can't play with", tech)
    elif tech=='javascript' or tech=='JAVASCRIPT':
        role = input("What kind of role you are expect in " + tech)
        if role == 'web developer':
            print("2 months duration with 3 POC")
        elif role == 'app developer':
            print("3 months duration with 2POC")
        else:
            print(role, "can't play with", tech)
else:
    print(category," has to do Global certification on online")