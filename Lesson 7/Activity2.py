math=int(input('Give me math grades'))

science=int(input('Give me science grades'))

SS=int(input('Give me SS grades'))

history=int(input('Give me History grades'))

LA=int(input('Give me LA grades'))

average=((math+science+SS+history+LA))/5

print(average)

if(average>92):
    print('U have  A grade')
elif(average<92 and average>82):
    print('U have B grade')
elif(average<82 and average>72):
    print('U have a C average')
else:
    print("Stay At Home ig")

