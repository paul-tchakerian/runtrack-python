def cesar(message, decalage):

    key = "abcdefghijklmnopqrstuvwxyz"
    result = ''
    for i in range(len(message)):
        if message[i] in key:
          for x in range(len(key)):
                if  message[i] == key[x]:

                    if x+decalage > (len(key)-1):
                        result += key[(x+decalage)-len(key)-1]

                    else:
                        result += key[x+decalage]

                    break
        else:
            result += message[i]

    return result
        
print(cesar('Avanguard',10))
print(cesar('Ubuntu',3))