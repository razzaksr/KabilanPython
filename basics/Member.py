# member operator: in, not in

# list
models=['Redmi9','Realme7','Nokia6.1Plus','Honor9lite']
print(models[2])
#tuple
price=('avenger220','apache200',98700,12,'vikrant',1.2)
print(price[3])
#dict
skills={'java':8000,'python':9000,'dot net':15000,'CCPP':5000,'java':23000,'PHP':8000}
print(skills)

print('Realme5S' in models)
print('Redmi9' in models)

print(12 in price)
print(1.2 not in price)

print('php' in skills)

print('dotNet' not in skills)
