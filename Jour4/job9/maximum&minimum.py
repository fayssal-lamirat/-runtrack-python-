L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]

# Initialisation des variables max et min avec le premier élément de la liste
max = L[0]
min = L[0]

# Parcours de la liste pour trouver le maximum et le minimum
for x in L:
    if x > max:
        max = x
    if x < min:
        min = x

# Affichage du résultat
print("Le maximum de la liste est :", max)
print("Le minimum de la liste est :", min)
