# using arithmetic can swap numeric objects

# swap between non numerical objects such as str, list,tuple,dict can be done via third object
mohamed="savings"
razak="current"
print("Mohamed account type",mohamed,"Razak account type",razak)
temp=mohamed
mohamed=razak
razak=temp
print("Mohamed account type",mohamed,"Razak account type",razak)



kabilan=float(input("Tell us height of kabilan: "))
menon=float(input("Tell us height of menon: "))
print(kabilan,menon)
kabilan*=menon#kabilan=kabilan*menon#
menon=kabilan/menon#
kabilan/=menon#kabilan=kabilan/menon#
print(kabilan,menon)
kabilan=kabilan+menon#11.6
menon=kabilan-menon#5.4
kabilan=kabilan-menon#6.2
print(kabilan,menon)

