# def drawRectangle(hauteur, largeur):
#     for x in range(hauteur):
#         for y in range(largeur):
#             if (y == 0 or y == largeur-1):
#                 print("|", end="")
#             elif (x == 0 or x == hauteur-1) and (y != 0 and y != largeur-1):
#                 print("-", end="")
#             else:
#                 print(" ", end="")
#         print("")

# drawRectangle(5,10)

# def draw_rectangle(width, height):

#   print('|' + '-' * (width-2) + '|')

#   for i in range(height-2):

#     print('|' + ' ' * (width-2) + '|')


#   print('|' + '-' * (width-2) + '|')

# draw_rectangle(10, 3)


# def draw_rectangle(width, height):
#     for i in range(1, height + 1):
#         for j in range(1, width + 1):
#                 if j == 1 or j == width:
#                  print('|' + ' ' * (width-2) + '|')
#                 else:
#                   if i == 1 or i == height:
#                     print('|' + '-' * (1, height + 1) + '|') 
                



# draw_rectangle(10, 4)


def draw_rectangle(width, height):
  print('-' * width)
  for i in range(height - 3):
    print('|' + ' ' * (width - 3) + '|')
  print('-' * width)

draw_rectangle(10, 4) 
    
    

