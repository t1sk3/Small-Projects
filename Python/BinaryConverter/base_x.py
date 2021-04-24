import eulerlib

def to_base(num, base):
    if base == 10:
        return num
    
    num = int(num)
    basebase = 1
    iteration = 0
    newlst = []
    while basebase <= num:
        basebase = basebase*base
        iteration += 1
    iteration += -1
    multiplier = base**iteration
    for i in range (0, iteration + 1):
        if int(num) >= multiplier:
            nieuw = (num - (num%multiplier))/multiplier
            newlst.append(nieuw)
            num = num - multiplier*nieuw

        else:
            newlst.append('0')
        if multiplier != 1:
            multiplier = multiplier/base
        elif multiplier == 1:
            multiplier = 0

    for i in range(0, len(newlst)):
        newlst[i] = int(newlst[i])

    for i in range(0, len(newlst)):
        if newlst[i] == 10:
            newlst[i] = 'A'
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
        elif newlst[i] == 16:
            newlst[i] = 'G' 
        elif newlst[i] == 17:
            newlst[i] = 'H' 
        elif newlst[i] == 18:
            newlst[i] = 'I' 
        elif newlst[i] == 19:
            newlst[i] = 'J' 
        elif newlst[i] == 20:
            newlst[i] = 'K' 
        elif newlst[i] == 21:
            newlst[i] = 'L' 
        elif newlst[i] == 22:
            newlst[i] = 'M' 
        elif newlst[i] == 23:
            newlst[i] = 'N' 
        elif newlst[i] == 24:
            newlst[i] = 'O'
        elif newlst[i] == 25:
            newlst[i] = 'P' 
        elif newlst[i] == 26:
            newlst[i] = 'Q' 
        elif newlst[i] == 27:
            newlst[i] = 'R' 
        elif newlst[i] == 28:
            newlst[i] = 'S' 
        elif newlst[i] == 29:
            newlst[i] = 'T' 
        elif newlst[i] == 30:
            newlst[i] = 'U' 
        elif newlst[i] == 31:
            newlst[i] = 'V' 
        elif newlst[i] == 32:
            newlst[i] = 'W' 
        elif newlst[i] == 33:
            newlst[i] = 'X' 
        elif newlst[i] == 34:
            newlst[i] = 'Y' 
        elif newlst[i] == 35:
            newlst[i] = 'Z' 

    res = ''.join(str(d) for d in newlst)
    return res

if __name__ == "__main__":
    for i in range(2,37):
        print(i, to_base(200, i), eulerlib.etc.decimal_to_base(200,i))

