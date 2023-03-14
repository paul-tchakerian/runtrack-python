def replace(list):                    # La fonction replace() prend en paramètre une liste en argument qui pmodifie cette liste
    list[3] = list[2] + list[4]       # en remplaçant la valeur à l'index 3 par la somme des valeurs à l'index 2 et 4    
    return list[-1]

L = [48, 92, 53, 12, 63]
last_value = replace(L)   
print(L)
print(last_value)
