import random
def jeu_devinette(a):
    nombre_magique = random.randint(1, 100)
    tentatives = 0
    while (a != nombre_magique) : 
        tentatives += 1
        if tentatives == 20:
            print ('Vous avez dépassé le nombre de tentatives autorisées')
            print ('Le nombre magique était : ', nombre_magique)
        if (a > nombre_magique ) :
            print (' Votre nombre est supérieur au nombre attendu , essayez encore ')
            a = int(input('Vous pouvez essayer à nouveau: ' ))
        elif (a < nombre_magique ) :
            print (' Votre nombre est inférieur au nombre attendu , essayez encore')
            a = int(input('Vous pouvez essayer à nouveau: ' ))
    if (a == nombre_magique) :
        print (' Félicitations , vous avez trouvé le nombre magique en ', tentatives, 'tentatives')
        print ('Le maximum de tentatives autorisées était de 20')
        print ('Au plaisir de vous revoir pour une nouvelle partie')
    return tentatives
b =int (input('C\'est parti pour une nouvelle aventure, essayez de deviner le nombre entre 1 et 100: '))
jeu_devinette(b)