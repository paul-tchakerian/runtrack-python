
def show_number():
    input_var = input("Salut cher correcteur, je suis un programme qui affiche les nombres de 0 à 100 sauf 26, 37, 88."
                        "voici les nombres affichés les uns à la suite des autres... ")
    for x in range(101):
        if x not in (26, 37, 88):
            print( "Donc\n" + input_var + "cela est sensé ressembler à cela " + str(x)) 
            print(x)


show_number()
