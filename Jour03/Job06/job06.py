string = "abcdefghijklmnopqrstuvwxyz" * 10

for i in range(len(string)):
    print(' ' * (len(string)-i), string[i] * (i*2+1))
