amount=int(input('Enter amount that u want to withdraw'))
note1=amount//100
note2=(amount%100)//50
note3=((amount%100)%50)//5
print('Your money is', amount)
print('Number if $100 bills is', note1)
print("Number of $50 dollar bills is", note2)
print('Number of 5 dollar bills is', note3)