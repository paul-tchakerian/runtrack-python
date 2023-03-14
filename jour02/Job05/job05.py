

def calcule( num1,operateur,num2):
    if operateur=="+":
        return num1+num2
    elif operateur=="-":
        return num1-num2
    elif operateur=="*":
        return num1*num2
    elif operateur=="/":
        return num1/num2
    elif operateur=="%":
        return num1%num2
print(calcule(43,"-",750))