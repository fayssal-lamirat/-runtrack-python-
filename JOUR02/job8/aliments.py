def fruits_et_legumes(type, saison):
    if type == "fruits" and saison == "hiver":
        print("orange, mandarine et kiwi")
    elif type == "fruits" and saison == "ete":
        print("Poire, fraise, cassis")
    elif type == "legume" and saison == "hiver":
        print("carotte, topinambour, endive")
    elif type == "legume" and saison == "ete":
        print("artichaut, aubergine,navet")
    else:
        print("Type ou saison non reconnu")
fruits_et_legumes("fruits", "hiver") # affiche "orange, mandarine et kiwi"
fruits_et_legumes("legume", "ete") # affiche "artichaut, aubergine,navet"
fruits_et_legumes("fruits", "printemps") # affiche "Type ou saison non reconnu"
