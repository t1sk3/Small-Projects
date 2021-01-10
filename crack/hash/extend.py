def extend():
    counter = 0
    wrdlst = []
    print("If you have a dictionary with additional passwords,\nyou can extend the main dictionary with this program. \nPlease make sure the extending file is in the same directory as this program. \n \n")
    passfile = open("pass_list.txt", "r+")
    extendfile = open(input("Please enter the filename of the extending file: "), "r")
    for word in extendfile:
        if word not in passfile and word.strip("\n") not in passfile:
            counter += 1
            wrdlst.append(word.strip("\n"))
            passfile.writelines(word.strip("\n")+"\n")
    extendfile.close()
    passfile.close()
    print(f"{counter} word(s) added to dictionary. {wrdlst}")

def main():
    extend()

if __name__ == "__main__":
    main()