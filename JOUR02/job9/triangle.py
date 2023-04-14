def type_triangle(a, b, c):
    # Vérifier si les longueurs permettent de construire un triangle
    if a + b > c and a + c > b and b + c > a:
        # Vérifier si le triangle est équilatéral
        if a == b == c:
            print("Triangle équilatéral")
        # Vérifier si le triangle est isocèle
        elif a == b or a == c or b == c:
            # Vérifier si le triangle est rectangle
            if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
                print("Triangle isocèle et rectangle")
            else:
                print("Triangle isocèle")
        # Si le triangle n'est pas équilatéral ou isocèle, il est quelconque
        else:
            # Vérifier si le triangle est rectangle
            if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
                print("Triangle quelconque et rectangle")
            else:
                print("Triangle quelconque")
    else:
        print("Impossible de construire un triangle avec ces longueurs")
type_triangle(3, 4, 5) # affiche "Triangle rectangle et isocèle"
type_triangle(5, 5, 5) # affiche "Triangle équilatéral"
type_triangle(3, 4, 6) # affiche "Triangle quelconque"
type_triangle(1, 2, 3) # affiche "Impossible de construire un triangle avec ces longueurs"

