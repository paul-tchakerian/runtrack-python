# def is_prime(num):
#     if num == 1:
#         return False
#     for i in range(2, int(num/2)+1):
#         if num%i == 0:
#             return False
#     return True
# 
# for num in range(2, 1001):
#     if is_prime(num):
        # print(num, end='\t')


primes = [int]

def prime_numbers():
    for num in range(3, 1001, 2):   # La boucle commence à partir du nombre 3 --> 1000 avec des incréméntations de 2. En sachant que tous les nombres premiers supérieurs à 2 ne peuvent être que des nombres à ignorer puisque tous les nombres pairs supérieurs à 2 ne peuvent pas être premiers
        is_prime = True
        for i in range(2, int(num/2)+1): # la deuxieme boucle itère à travers tous les nombres stockés dans la liste primes et vérifie si le nombre est divisible par un nombre de le dictionnaire "primes"
            if num%i == 0:
                is_prime = False
                break
        if is_prime:
            if is_prime:
                print(num, end='\t')

print(primes)
prime_numbers()
