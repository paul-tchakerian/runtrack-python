
def show_number():
    input_var = input("Salut cher correcteur, je suis un programme qui affiche les nombres de 0 à 20."
                        "voici les nombres affichés les uns à la suite des autres... ")
    for x in range(21):
        print( "Donc\n" + input_var + "voici le nombre " + str(x)) 
        print(x)


show_number()
