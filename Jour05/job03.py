def draw_diagonal_tapis(n):
    for i in range(n + 1):
        line = ''
        for j in range(n + 1):
          if i == j:
            line += 'X'
        else:
          line += '0'
    print(line)

draw_diagonal_tapis(5)