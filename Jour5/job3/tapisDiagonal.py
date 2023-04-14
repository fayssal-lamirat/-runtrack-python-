def afficher_tapis(n):
    for i in range(n+1):
        for fayssal in range(n+1):
            if i == fayssal or i+fayssal == n:
                print("/", end="")
            else:
                print("X", end="")
        print()
afficher_tapis(10)
