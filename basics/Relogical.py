# Relational: > >= < <= == !=
# logical: and or ....

# cibil score:
cibil=int(input("Tell us cibil: "))
print("Status of PL of 1Lack:",(cibil>=700))
property=int(input("Tell us property value: "))
print("Status of BL of 8Lack:",(cibil>=850 and property>9))
print("Status of HL of 5Lack:",(property>=10 or cibil>=900))

# Campus recruitment
skill=input("Tell us your proficiency: ")
poc=int(input("Tell us how may POC you were done on "+skill))
print("Decision for Associate Engineer:",(skill=='java' or skill=='python' and poc>=2))
print("Decision for DevOps engineer:",(skill=='aws' or skill=='agile' or skill=='java'))
print("Decision for Web developer engineer:",(poc>=5 and (skill=='javascript' or skill=='python' or skill=='java')))
