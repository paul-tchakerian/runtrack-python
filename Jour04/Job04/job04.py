FRUITS = ['apple', 'banana', 'orange']

def add_melon():
    FRUITS.insert(2, 'Mango')

print(FRUITS)
add_melon() # appeler la fonction pour que la mangue soit ajouté à la liste
print(FRUITS) 
add_melon() # appeler une deuxieme fois la fonction pour que la mangue soit ajouté à l'index 2