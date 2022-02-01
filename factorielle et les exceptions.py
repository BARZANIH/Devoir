def calculfact(n):
    if n==0:
        return 1
    else:
        return n*calculfact(n-1)

def is_complex(n):
    if (type(n) == complex):
        n = n.real #### On prend la partie réelle du nombre et on réaffecte la valeur de a avec
    else:
        n = n.real
    return n


def negative(n):
    if (n < 0):
        print("vous avez saisie un nombre négative!on va le transformer en positive ")
        n = abs(n)
        return (n)
    else:
        return(n)


def digit(n,x,y):
    if (len(str(n)) > y ) :
        while((len(str(n)) > y)):
            print("Le nombre saisie comporte plus de {} digit, Veuillez le resaisir.".format(y))
            n = int(input())
    if (len(str(n)) < x ) :
        while((len(str(n)) < x)):
            print("Le nombre saisie comporte moins de {} digit, Veuillez le resaisir.".format(x))
            n = int(input())
    else:
        pass
    return (n)



def factorielle_v3(n):
    if (type(n)==str):
        while(type(n)==str):
            try:
                print("Veuillez saisir un valeur numérique:")
                n = int(input()) #### Saisie d'une nouvelle valeur de n
            except:
                print("on peut pas calculer le factorielle d'une chaine de caractère!!!")
    if (type(n)==float):
        while(type(n)==float):
            try:
                print("Veuillez saisir un valeur numérique entier:")
                n = int(input()) #### Saisie d'une nouvelle valeur de n
            except:
                print("on peut pas calculer le factorielle d'un nombre réel!!!")
    elif (type(n) == complex):
        is_complex(n)
        print(is_complex(n))
        n = is_complex(n)
    elif (n<0):
        n = negative(n)
    elif (len(str(n))<2 or len(str(n))>5):
        n=digit(n,2,5)
    return calculfact(n) 