#  Wzorowane na przykładzie Rona Zacharskiego
#

from math import sqrt
from numpy import corrcoef

users = {
        "Ania": 
            {"Blues Traveler": 1.,
            "Broken Bells": 1.5,
            "Norah Jones": 2,
            "Deadmau5": 2.5,
            "Phoenix": 3.0,
            "Slightly Stoopid": .5,
            "The Strokes": 0.0,
            "Vampire Weekend": 2.0},
         "Bonia":
            {"Blues Traveler": 4.0,
            "Broken Bells": 4.5, 
            "Norah Jones": 5.0,
            "Deadmau5": 5.5, 
            "Phoenix": 6.0, 
            "Slightly Stoopid": 3.5, 
            "The Strokes": 2.0,
            "Vampire Weekend": 5.0}
        }

        
def manhattan(rating1, rating2):
    
    """Oblicz odległość w metryce taksówkowej między dwoma  zbiorami ocen
       danymi w postaci: {'The Strokes': 3.0, 'Slightly Stoopid': 2.5}
       Zwróć -1, gdy zbiory nie mają… wspólnych elementów"""
       
    # TODO: wpisz kod
    klucze1 = rating1.keys()
    klucze2 = rating2.keys()
    odleglosc = 0
    udaloSiePorownac = False

    for klucz in klucze1:
        if klucz in rating2.keys():
            udaloSiePorownac = True
            odleglosc = odleglosc + abs(rating2[klucz] - rating1[klucz])

    if (udaloSiePorownac==True):
        return odleglosc
    else:
        return -1

def pearson(rating1, rating2):
    klucze1 = users[rating1].keys()    
    klucze2 = users[rating2].keys()
    korelacja=0
    x=0
    y=0
    suma_x=0
    suma_y=0
    iloczyn_sumy=0
    suma_iloczynow=0
    korelacja_licz=0
    korelacja_mian=0
    n=0
    for key in klucze1:
        for key1 in klucze2:
            if key ==key1:
                n=n+1
                x=users[rating1][key]
                y=users[rating2][key1]
                suma_x=suma_x+x
                suma_y=suma_y+y 
            iloczyn_sumy=suma_x*suma_y
            suma_iloczynow=suma_iloczynow+(x*y)
    korelacja_licz=korelacja_licz+suma_iloczynow-(iloczyn_sumy/n)
    korelacja_mian=(sqrt(suma_x**2-(suma_x**2/n)))*(sqrt(suma_y**2-(suma_y**2/n)))
    korelacja=korelacja_licz/korelacja_mian
    return korelacja

def pearsonNumpy(rating1, rating2):
    korelacja=0
    klucze1 = users[rating1].keys()    
    klucze2 = users[rating2].keys()
    x=[]
    y=[]
    for key in klucze1:
        for key1 in klucze2:
            if key==key1:
                x.append(users[rating1][key])
                y.append(users[rating2][key1])
    korelacja=corrcoef([x,y])[1,0]
    return korelacja
