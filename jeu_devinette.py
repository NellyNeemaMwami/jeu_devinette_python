import random
x = random.randint(1, 100)
a = int(input(' ' ))
while (a != x) : 
    print ('réessayer vous y êtes presque ')
    a = int (input ('saisissez un autre nombre :'))
    if (a > x ) :
        print (' vous allez loin du nombre ')
    elif (a < x ) :
        print (' ajoutez un tout petit peu')
    else :
        print (' c\'est parfait , vous l\'avez fait  ')
