import re
import hashlib

while True:
    password = input("Choisissez un mot de passe : ")
    if len(password) < 8:
        print("Le mot de passe doit contenir au moins 8 caractères.")
        continue
    elif not re.search("[a-z]", password):
        print("Le mot de passe doit contenir au moins une lettre minuscule.")
        continue
    elif not re.search("[A-Z]", password):
        print("Le mot de passe doit contenir au moins une lettre majuscule.")
        continue
    elif not re.search("[0-9]", password):
        print("Le mot de passe doit contenir au moins un chiffre.")
        continue
    elif not re.search("[!@#$%^&*]", password):
        print("Le mot de passe doit contenir au moins un caractère spécial.")
        continue
    else:
        hash_object = hashlib.sha256(password.encode('utf-8'))
        hashed_password = hash_object.hexdigest()
        print("Mot de passe valide. Le mot de passe hashé est :", hashed_password)
        break
