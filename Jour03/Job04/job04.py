def Fizzbuz():      # je créer une fonction qui va contenir les conditions ternaires 
    for j in range(1,101):
        fizz = "Fizz" if j % 3 == 0 else ""
        buzz = "Buzz" if j % 5 == 0 else ""
        print(fizz + buzz or j)


Fizzbuz()


# j'ai utilisé une méthode qui fait appel à des conditions ternaires pour déterminer si le nombre est divisible par 3 ou 5 ou les deux. J'ai voulu utilisé cette méthode pour que je puisses 
# rééecrire mon code différemment de la 1ère fois où j'ai fais ce job.
