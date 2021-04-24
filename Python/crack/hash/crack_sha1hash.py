import hashlib
import time

def inp():
    pass_hash = input("Enter sha1 hash: ")
    pass_hash = pass_hash.lower()

    wordlist = input("File name (leave empty to use the default dictionary): ")
    if wordlist == "":
        wordlist = filepath
    
    return pass_hash, wordlist

def crack(pass_hash, wordlist):
    flag = 0
    try:
        pass_file = open(wordlist, "r")
    except:
        print("No file found, you donkey.")
        quit(0)

    start_time = time.time()

    for word in pass_file:
        enc_wrd = word.encode('utf-8')
        digest = hashlib.sha1(enc_wrd.strip()).hexdigest()
        
        if digest == pass_hash:
            print("Password found, you fucking piece of shit.")
            print("The password is " + word)
            print("--- Found in %s seconds ---" % (time.time() - start_time))
            flag = 1
            break

    if flag == 0:
        print("Password or passphrase is not in your stupid dictionary, get a better one!")
        print("Or you entered another type of hash, you donkey!")

def main():
    inphash, inplist = inp()
    crack(inphash, inplist)

if __name__ == "__main__":
    main()