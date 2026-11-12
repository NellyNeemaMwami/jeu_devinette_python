import random
x = random.randint(1, 100)
tentatives = 0
a = int(input('Saisissez un nombre entre 1 et 100 ' ))
while (a != x) : 
    tentatives += 1
    print ('réessayer vous y êtes presque ')
    a = int (input ('saisissez un autre nombre :'))
    if (a > x ) :
        print (' Votre nombre est supérieur au nombre attendu , essayez encore ')
    elif (a < x ) :
        print (' Votre nombre est inférieur au nombre attendu , essayez encore')
    else :
        print (' c\'est parfait , vous l\'avez fait  ')
print('Bravo ! Vous avez trouvé le nombre en ', tentatives, 'tentatives.')