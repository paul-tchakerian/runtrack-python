L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]

def productList(liste):

    product = 0

    for i in liste:
        
        if 25 < i < 90:
        
             if product == 0:
                product = i
             else:
                product *= i 
    return product

print(productList(L))
