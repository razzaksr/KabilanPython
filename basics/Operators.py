# finding distance can be travelled depend on the milage and fuel

fuel=int(input("Tell us liters you filled: "))
milage=int(input("Tell your avg milage: "))
tank=int(input("Tell us your tank capacity: "))#13
kms=fuel*milage
print("Kilometer you can travel is",kms)
res=tank/4#3.25
res*=milage
print("Kilometer can travel through main:",(kms-res))
print("Kilometer can travel through reserve is:",res)
