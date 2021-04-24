def bintodec(number):
    numlst = [int(d) for d in str(number)]
    multiplier = 2**(len(numlst) - 1)
    dec = 0
    for i in range(0, len(numlst)):
        if numlst[i] != 1 and numlst[i] != 0:
            print("This number is not a valid binary number.")
            exit(0)
        dec += numlst[i]*multiplier
        multiplier = multiplier/2
    return dec

def hextodec(number):
    hexlst = ['1','2','3','4','5','6','7','8','9','0','A','B','C','D','D','F']
    numlst = [str(d) for d in str(number)]
    for i in range(0, len(numlst)):
        if numlst[i] == 'A':
            numlst[i] = 10
        elif numlst[i] == 'B':
            numlst[i] = 11
        elif numlst[i] == 'C':
            numlst[i] = 12
        elif numlst[i] == 'D':
            numlst[i] = 13
        elif numlst[i] == 'E':
            numlst[i] = 14
        elif numlst[i] == 'F':
            numlst[i] = 15
        elif not numlst[i] in hexlst:
            print("This is not a valid hexadecimal number.")
            exit(0)
    for i in range(0, len(numlst)):
        numlst[i] = int(numlst[i])

    multiplier = 16**(len(numlst) - 1)
    dec = 0
    for i in range(0, len(numlst)):
        dec += numlst[i]*multiplier
        multiplier = multiplier/16
    return dec

def dectobin(number):
    number = int(number)
    two = 1
    iteration = 0
    newlst = []
    while two <= int(number):
        two = two*2
        iteration += 1
    iteration += -1
    multiplier = 2**iteration
    for i in range (0, iteration + 1):
        if int(number) >= multiplier:
            newlst.append('1')
            number = number - multiplier
        else:
            newlst.append('0')
        if multiplier != 1:
            multiplier = multiplier/2
        elif multiplier == 1:
            multiplier = 0
    bina = ''.join(str(d) for d in newlst)
    try:
        bina = int(bina)
        return bina
    except:
        return bina

def dectohex(number):
    number = int(number)
    hexhex = 1
    iteration = 0
    newlst = []
    while hexhex <= number:
        hexhex = hexhex*16
        iteration += 1
    iteration += -1
    multiplier = 16**iteration
    for i in range (0, iteration + 1):
        if int(number) >= multiplier:
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
    hexa = ''.join(str(d) for d in newlst)
    return hexa

def dectobcd(onumber):
    nums = []
    newnum = ''
    onumber = str(onumber).strip(' ')
    for number in onumber:
        nums.append(number)
    for number in nums:
        adding = True
        addnum = str(dectobin(int(number)))
        while adding:
            if len(addnum.strip()) < 4:
                addnum = '0' + addnum
            else:
                adding = False
        newnum = newnum + ' ' + str(addnum)
    return newnum

def bcdtodec(onumber):
    nums = onumber.split(" ")
    newnums = []
    for number in nums:
        newnums.append(int(bintodec(number)))
    newiedew = ''.join(str(d) for d in newnums)
    return int(newiedew)

def main():
    #choosing the original number system
    print("From what number system would you like to be converting?")
    print("1. Binary")
    print("2. Decimal")
    print("3. Hexadecimal")
    print("4. Binary-Coded Decimal")

    choice1 = input()
    if choice1 == '1':
        system1 = 1
        name1 = "binary"
    elif choice1 == '2':
        system1 = 2
        name1 = "decimal"
    elif choice1 == '3':
        system1 = 3
        name1 = "hexadecimal"
    elif choice1 == '4':
        system1 = 4
        name1 = "BCD"

    #choosing the target number system
    print("To what number system would you like to be converting?")
    print("1. Binary")
    print("2. Decimal")
    print("3. Hexadecimal")
    print("4. Binary-Coded Decimal")

    choice2 = input()
    if choice2 == '1':
        system2 = 1
        name2 = "binary"
    elif choice2 == '2':
        system2 = 2
        name2 = "decimal"
    elif choice2 == '3':
        system2 = 3
        name2 = "hexadecimal"
    elif choice2 == '4':
        system2 = 4
        name2 = "BCD"

    if system1 == system2:
        print("You are not converting to a new number system, your solution will therefor be the same as your input.")
        exit(0)
    elif system1 != 3 and system1 != 4:
        ognumber = input(f'Please enter your number in {name1}: ')
    elif system1 == 4:
        ognumber = input(f'Please enter your number in BCD, make sure to add spaces to split up the different numbers.')
    else:
        ognumber = input(f'Please enter your number in {name1}: ').upper()

    if system1 == 1:
        decnum = int(bintodec(ognumber))
    elif system1 == 2:
        decnum = int(ognumber)
    elif system1 == 3:
        decnum = int(hextodec(ognumber))
    elif system1 == 4:
        decnum = int(bcdtodec(ognumber))

    if system2 == 1:
        newnum = int(dectobin(decnum))
    elif system2 == 2:
        newnum = int(decnum)
    elif system2 == 3:
        newnum = dectohex(decnum)
    elif system2 == 4:
        newnum = dectobcd(decnum)

    print(f'Your {name1} number ({ognumber}) is {newnum} in {name2}.')

if __name__ == "__main__":
    main()