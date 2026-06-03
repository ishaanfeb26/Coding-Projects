cyclist1=int(input("Give me ur speed"))
cyclist2=int(input("Give me ur speed"))
cyclist3=int(input("Give me ur speed"))
average=(cyclist1+cyclist2+cyclist3)//3

print("The average is:", average)


if (cyclist1>average):
    print('Cyclist 1 is above average')
elif (cyclist2>average):
    print('Cyclist 2 is above average')
elif (cyclist3>average):
    print('Cyclist 3 is above average')
else:    print('All cyclists are average')


