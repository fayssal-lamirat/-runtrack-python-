def distance_toilettes(marches, hauteur):
    distance_jour = 2 * marches * hauteur / 100  # en mètres
    distance_semaine = 7 * distance_jour
    return f"Pour {marches} marches de {hauteur} cm, le gardien parcours {distance_semaine:.2f} m par semaine."

marches = 50
hauteur = 20
distance = distance_toilettes(marches, hauteur)
print(distance)
