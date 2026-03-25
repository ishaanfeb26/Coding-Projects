cost=float(input('Enter the total cost of product'))

actual_sale= float(input("Enter the total sale of the day"))
if(cost>actual_sale):
    print('You lost money on this deal')
elif(actual_sale == cost):
    print("Break even")
else:
    print('You profited on this sale')