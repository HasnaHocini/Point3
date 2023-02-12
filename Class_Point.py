class Point:
    """
    Classe point
    """
    def __init__(self, p_x, p_y):
        """
        Constructeur de la classe Point
        :param p_x: Coordonnée x de mon point
        :param p_y: Coordonnée y de mon point
        """
        self.x = p_x
        self.y = p_y

    def Afficher(self):
        """
        Afficher les coordonnées cartésiennes d'un point
        """
        print(self.x, self.y)

    def Avoir_Coordonnes_Paires(self):
        if self.x % 2 == 0 and self.y % 2 == 0:
            return True
        else:
            return False
