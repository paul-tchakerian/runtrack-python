def trouver_mot_plus_proche(mot_original):
    
    mot = input("Veuillez entrer un mot sans espace ni accent ni majuscule : ")

    # La fonction commence par transformer le mot en une liste de caractères (caracteres)
    caracteres = list(mot_original) # séparer les caractères du mot original
    index_pivot = -1 # index du pivot
    n = len(caracteres) # longueur du mot
    
    # Parcourir les lettres de la fin au début du mot (depuis l'index n-2 jusqu'à l'index 0). Dès que cette dernière trouve la première paire de lettres où la lettre d'indice i est + petite que la suivante (i+1), elle arrête la boucle et garde l'index de la lettre i dans la variable index_pivot
    for i in range(n-2, -1, -1): 
        if caracteres[i] < caracteres[i+1]: # si la lettre  est inférieure à la lettre suivante
            index_pivot = i     # alors trouver l'index du pivot qui est la plus petite  mais qui est plus grande que la lettre i+1 
            break
        
    if index_pivot == -1: # Si aucun pivot n'a été trouvé, cela signifie que le mot rentrée dans la console est déjà le plus grand possible
        print("Le mot entré est déjà le plus grand possible !")   # Donc la fonction affiche un message d'erreur 
        return mot_original  # et retourne le mot original
    
    else:
    # Sinon, la fonction continue la recherche du caractère suivant D (celui qui suit le pivot « index_pivot »)
        index_suivant = index_pivot + 1  #  Pour réaliser une recherche de celui-ci, il faut que la fonction boucle sur les lettres situées à droite de l'index pivot et en comparant chacune d'entre elles avec la lettre de caracteres[index_pivot] 
        for j in range(index_pivot+1, n):    # Seul le caractère le plus proche  mais qui reste supérieur à caracteres[index_pivot] sera retenu.
            if caracteres[j] > caracteres[index_pivot] and caracteres[j] <= caracteres[index_suivant]: 
                index_suivant = j   # Son index est stocké dans la variable  « index_suivant »
            
    # La fonction échange sa position avec celle de la lettre de pivot obtenue précédemment en utilisant la commande d'éléments en Python
    caracteres[index_pivot], caracteres[index_suivant] = caracteres[index_suivant], caracteres[index_pivot] # Une fois que le caractère est trouvé, la fonction échange sa position avec celle  de la lettre de pivot obtenue précédemment en utilisant la commande d'éléments en Python

            # Puis, la fonction « sorted » trie les lettres situées à droite de l'index pivot. D'ailleurs, le prochain caractère ne sera pas forcément juste à droite de mon pivot...
    caracteres[index_pivot+1:] = sorted(caracteres[index_pivot+1:])
    
    # Finallement, la fonction reconstitue en utilisant la commande « join » le mot à partir de la liste de caractères obtenue et l'affiche
    nouveau_mot = "".join(caracteres)
    print("Le mot le plus proche dans l'ordre alphabétique est :", nouveau_mot)
    return nouveau_mot

mot_original = input("Veuillez entrer un mot sans espace ni accent ni majuscule : ")
trouver_mot_plus_proche(mot_original)
