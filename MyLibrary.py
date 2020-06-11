
def Min(a, b):
    if(a < b):
        return a
    else:
        return b

def Max(a, b):
    if(a > b):
        return a
    else:
        return b

def inputData(min, max, label):
    x = eval(input("Escriba su " + label + " [" + str(min) + " - " + str(max) + "]: "))
    while(x < min or x > max):
        x = eval(input("Escriba su " + label + " [" + str(min) + " - " + str(max) + "]: "))
    return x


def seasonName(day, month):
    if day < 1 or day > 31 or month < 1 or month > 12:
        return "Día no válido"

    if month ==  1 or month ==  2  or month == 12 and day >= 21  or month == 3 and day <= 20:
        return "Invierno"
    if month ==  4 or month ==  5  or month ==  3                or month == 6 and day <= 20:
        return "Primavera"
    if month ==  7 or month ==  8  or month ==  6                or month == 9 and day <= 21:
        return "Verano"

    return "Otoño"
