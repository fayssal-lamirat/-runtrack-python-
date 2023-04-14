import random
import string
import hashlib

def create_password():
    while True:
        password = input("Choisissez un mot de passe: ")
        if len(password) < 8:
            print("Le mot de passe doit contenir au moins 8 caractères.")
        
        elif not any(char.isdigit() for char in password):
#Cette ligne de code est utilisée pour vérifier si le mot de passe contient au moins un chiffre.
# J'utilise la méthode isdigit() pour vérifier chaque caractère du mot de passe.
           
            print("Le mot de passe doit contenir au moins un chiffre.")
        
        elif not any(char.isupper() for char in password):
# Cette ligne vérifie si le mot de passe contient au moins une lettre majuscule.
# J'ai utilisé isupper() qui est une méthode de chaîne (string)  qui renvoie True 
# si tous les caractères de la chaîne sont en majuscules et qu'il y a au moins un caractère, sinon elle renvoie False

            print("Le mot de passe doit contenir au moins une lettre majuscule.")

        elif not any(char.islower() for char in password):
# Cette ligne a son tour est une condition qui permet de vérifier si le mot de passe contient au moins une lettre minuscule.
# la boucle "for" ici  parcour chaque caractère de la chaîne de caractères "password".
#Pour chaque caractère de "password", la méthode islower() est utilisée pour vérifier si le caractère est une lettre minuscule. 
# Si au moins un caractère de la chaîne est une lettre minuscule, la condition renverra False. Sinon, la condition renverra True

            print("Le mot de passe doit contenir au moins une lettre minuscule.")

        elif not any(char in "!@#$%^&*" for char in password):
# Cette ligne est la condition qui permet de vérifier si le mot de passe contient au moins un caractère spécial.
#Pour chaque caractère de "password", la condition char in "!@#$%^&*" est utilisée pour vérifier si le caractère est un caractère spécial.
#  Si au moins un caractère de la chaîne est un caractère spécial, la condition renverra False. Sinon, la condition renverra True.

            print("Le mot de passe doit contenir au moins un caractère spécial (!, @, #, $, %, ^, &, *).")
        
        else:
            return password
  #  Lorsque cette condition est remplie, la fonction renvoie le mot de passe choisi par l'utilisateur. Cette ligne return password renvoie la valeur de la variable password comme résultat de la fonction create_password().
  #  lorsque l'utilisateur choisit un mot de passe qui répond aux critères de sécurité, cette ligne de code permet à la fonction de renvoyer ce mot de passe à l'endroit où elle a été appelée.

def hash_password(password):
    # Utiliser l'algorithme SHA-256 pour hasher le mot de passe
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password

# Demander à l'utilisateur de créer un mot de passe
password = create_password()
print("Mot de passe valide !")

# Hasher le mot de passe et afficher le résultat
hashed_password = hash_password(password)
print("Le mot de passe haché est:", hashed_password)
