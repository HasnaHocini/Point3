# import
import math
from Class_Point import *

# Procédures et fonctions
def fn_distance(pa , pb ):
    """
    Calcule la distance entre deux points
    :param pa: l'objet 1 instancié de la classe Point
    :param pb: l'objet 2 instancié de la classe Point
    :return:   La distance entre les deux points
    """
    return round(math.sqrt((pa.x-pb.x)**2+(pa.y-pb.y)**2), 1)

# Programme principal

p1 = Point(7, 9)
p2 = Point(0, 0)
p1.Afficher()
p2.Afficher()
print(round(fn_distance(p1,p2),2))
print("Parfait !")
