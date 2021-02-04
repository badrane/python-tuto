# creer une class Retangle
# prend 2 parameters long , larg , par default  = 0
# a prend un nom = "rectangle"
# une methode surface
#une methode __str__ pour l 'affichage avec  ces caracteriques lon , larg ,surface
# creer une classe carre qui herite de rectangle
# et prend un nom = "carre"

class Rectangle:
    """classe des rectangles."""
    def __init__(self, longueur=0, largeur=0):
        "Initialisation avec valeurs par defaut"
        self.lon = longueur
        self.lar = largeur
        self.nom = "rectangle"
    def surface(self):
        "Retourne la surface d'un rectangle."
        return self.lon*self.lar
    def __str__(self):
        "Affichage des caracteristiques d'un rectangle."
        return ("\nLe {} de cotes {} et {} a une surface de {}".
                format(self.nom, self.lon, self.lar, self.surface()))

class Carre(Rectangle):
    """classe de carres"""
    def __init__(self, cote=0):
        super().__init__(cote,cote)
        self.nom = "carre"


if __name__ == "__main__":
    r = Rectangle(12,8)
    print(r)
    #r.__str__()
    print(r.surface())
    r.lon=78
    print(r.surface())
    print(r)
    a = Carre(456)
    print(a)
