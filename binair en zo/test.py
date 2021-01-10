def dectohex(number):
    number = float(number)
    hexhex = 1
    iteration = 0
    newlst = []
    while hexhex <= number:
        hexhex = hexhex*16
        iteration += 1
    iteration += -1
    multiplier = 16**iteration
    for i in range (0, iteration + 1):
        if float(number) >= multiplier:
            nieuw = (number - (number%multiplier))/multiplier
            newlst.append(nieuw)
            number = number - multiplier*nieuw
        else:
            newlst.append('0')
        if multiplier != 1:
            multiplier = multiplier/16
        elif multiplier == 1:
            multiplier = 0
    
    for i in range(0, len(newlst)):
        newlst[i] = int(newlst[i])

    for i in range(0, len(newlst)):
        if newlst[i] == 10:
            newlst[i] = 'D'
        elif newlst[i] == 11:
            newlst[i] = 'B'
        elif newlst[i] == 12:
            newlst[i] = 'C'
        elif newlst[i] == 13:
            newlst[i] = 'D'
        elif newlst[i] == 14:
            newlst[i] = 'E'
        elif newlst[i] == 15:
            newlst[i] = 'F'
        print(newlst)
        
    hexa = ''.join(str(d) for d in newlst)
    return hexa

print(dectohex(45))
