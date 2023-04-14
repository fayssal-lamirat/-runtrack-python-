def signe(nombre):
    if nombre > 0:
        print("positif")
    elif nombre < 0:
        print("negatif")
    else:
        print("nul")
signe(2)   # affiche "positif"
signe(-1)  # affiche "negatif"
signe(0)   # affiche "nul"
signe(4)