def isValidDate(date):
    if len(date) < 3:
        return False
    dd = date[0]
    mm = date[1]
    yy = date[2]
    if dd < 1 or dd > 31 or mm < 1 or mm > 12 or yy < 1 or yy > 3000:
        return False
    if mm == 2 and dd > 28:
        return False
    if (mm == 4 or mm == 6 or mm == 9 or mm == 11) and dd > 30:
        return False
    return True

def nextDate(date):     # date = (30, 4, 2020)
    if not isValidDate(date):
        return None
    dd = 1 + date[0]
    mm = date[1]
    yy = date[2]
    if mm == 2 and dd > 28:             # Febrero
        dd = 1
        mm = 3
    elif mm == 4 or mm == 6 or mm == 9 or mm == 11:  # Mes de 30 días
        if dd > 30:
            dd = 1
            mm += 1
    elif dd > 31:           # Mes de 31 días
        dd = 1
        mm += 1
        if mm > 12:
            mm = 1
            yy += 1
    return dd, mm, yy       # dd, mm, yy forman una tupla de manera implícita
