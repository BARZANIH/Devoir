import numpy as np
from math import *

def formule():
    S=float(input("Entrer Le prix actual de l'action:"))
    X=float(input("Entrer Le prix d'exercice de l'option:"))
    T=float(input("Temps restant avant l’expiration de l’option, en pourcentage d’une année:"))
    r=float(input("Taux d’intérêt sans risque:"))
    v=float(input("volatilité implicite du prix de l’action, mesurée par un décimal:"))
    d1=(np.log(S/X)+((r+v**2)/2)*T)/(v*sqrt(T))
    d2=d1-v*sqrt(T)
    print("d1:",d1)
    print("d2:",d2)

formule()