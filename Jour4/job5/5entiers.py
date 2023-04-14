# Créer la liste L
L = [1, 3, 5, 7, 9]

# Afficher la valeur de L[1]
print("La valeur de L[1] est :", L[1])

# Écrire une fonction pour mettre à jour L[3]
def mettre_a_jour_L():
    L[3] = L[2] + L[4]

# Appeler la fonction pour mettre à jour L[3]
mettre_a_jour_L()

# Afficher la valeur de l'avant dernier terme de la liste
print("La valeur du dernier terme de la liste est :", L[-1])
