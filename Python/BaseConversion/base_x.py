import string

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
        for j in range(10, 36):
            if newlst[i] == j:
                newlst[i] = string.ascii_lowercase[i-9]

    res = ''.join(str(d) for d in newlst)
    return res

if __name__ == "__main__":
    for i in range(2,37):
        print(i, to_base(36, i))

