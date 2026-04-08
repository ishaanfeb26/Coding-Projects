height=int(input('Give me ur hieght'))
weight=int(input('Give me ur wieght'))
BMI=weight/(height/100)**2
print(BMI)

if(BMI<18.4):
    print('Ur underweight')

elif(BMI<24.9):
    print('Ur healthy')

elif(BMI<29.9):
    print('Ur overweight')

else:
    print('Ur obese')