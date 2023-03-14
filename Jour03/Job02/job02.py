
def show_number():
    input_var = input("Salut cher correcteur, je suis un programme qui parcours les nombres de 0 à 20 mais en affiche seulement 1/2n"
                        "voici les nombres affichés les uns à la suite des autres... ")
    for x in range(0, 21, 2):
        print( "Donc\n" + input_var + "voici le nombre " + str(x)) 
        print(x)


show_number()
