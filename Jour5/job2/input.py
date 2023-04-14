def draw_rectangle(width, height):
    # dessiner la première ligne du rectangle avec '-'
    print('-' * width)

    # dessiner les lignes suivantes avec '|' sur les côtés et des espaces à l'intérieur
    for i in range(height-2):
        print('|' + ' '*(width-2) + '|')

    # dessiner la dernière ligne du rectangle avec '-'
    if height > 1:
        print('-' * width)

# exemple d'utilisation
draw_rectangle(10, 3)



