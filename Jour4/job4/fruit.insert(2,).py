def ajouter_mangue():
    fruits = ["pomme", "cerise", "orange", "Melon"]
    fruits.insert(2, "Mangue")
    return fruits
print(ajouter_mangue()) # affiche ['pomme', 'cerise', 'Mangue', 'orange', 'Melon']
