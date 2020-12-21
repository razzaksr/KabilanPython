# sale
stock=30
collection=0
days=5
while stock>0 and days>0:
    quan=int(input("Tell us how many pen drives you want: "))
    if quan<=stock:
        stock -= quan
        collection+=10000*quan
        print(quan," items ordered")
    else:print("stock not available with required items",quan)
    days-=1
else:print("Out of stock/ Days are over")

print("Collected amount throughout the sale:",collection)
