from main import *
from Class_Point import *
import pytest

@pytest.fixture
def Creer_Points():
    pa = Point(0, 0)
    pb = Point(5, 5)
    return pa, pb

def test_fn_distance(Creer_Points):
    #pa = Point(0, 0)
    #pb = Point(5, 5)
    pa, pb =Creer_Points
    assert fn_distance(pa, pb) == 7.1


def test_coordonnes_paires(Creer_Points):
    #pa = Point(0, 0)
    #pb = Point(5, 5)
    pa, pb=Creer_Points
    assert pa.Avoir_Coordonnes_Paires() == True
    assert pb.Avoir_Coordonnes_Paires() == False

