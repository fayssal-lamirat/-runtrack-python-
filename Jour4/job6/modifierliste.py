#Écrire un programme qui échange les valeurs de la première et de la dernière case d’une
#liste quelconque non vide.

liste = ["a", "b", "c", "d", "e"]
variable = liste[0]
liste[0] = liste[-1]
liste[-1]=variable
print(liste)