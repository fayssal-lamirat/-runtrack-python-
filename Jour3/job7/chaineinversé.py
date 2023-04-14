chaine = "nikana"
inverse = ""

i = 1

for lettre in chaine:
    print("iteration n°"+str(i))
    print("valeur de la variable inverse: '"+inverse+"'")
    print("lettre actuelle: "+lettre)
    inverse = lettre + inverse
    print("valeur de inverse a la fin de l'iteration: "+inverse)
    i = i+1
    print()


print(inverse)