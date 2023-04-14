def chiffrer_message(message, decalage):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    message_chiffre = ""
    for lettre in message:
        if lettre in alphabet:
            index_lettre = alphabet.index(lettre)
            nouvelle_index = (index_lettre + decalage) % 26
            lettre_chiffree = alphabet[nouvelle_index]
            message_chiffre += lettre_chiffree
        else:
            message_chiffre += lettre
    return message_chiffre

message = "vive les vacances"
decalage = 3
message_chiffre = chiffrer_message(message, decalage)
print(message_chiffre)
