import os

# filepath should be changed to the path of the directory of all the files that need to be changed

def getNumber(filename):
    counter = 5
    number = ''
    while True:
        if filename[counter] in "0123456789":
            number += filename[counter]
        else:
            break
        counter += 1
    return number

def main():
    for filename in os.listdir(filepath):
        if filename[-3:] == '.py' and filename[:5] == "euler":
            #print(filename) 
            number = getNumber(filename)
            rest = 3 - len(number)
            newName = "euler"
            for i in range(rest):
                newName += "0"
            newName += number + ".py"
            src = filepath + filename 
            dst = filepath + newName

            os.rename(src, dst)

main()