import subprocess
from tkinter import *
import hashlib

def getWifiPasswords():
    global wifis, passList
    data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')

    wifis = sorted([line.split(':')[1][1:-1] for line in data if "All User Profile" in line], key=str.lower)

    passList = []

    for wifi in wifis:
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', wifi, 'key=clear']).decode('utf-8').split('\n')
        results = [line.split(':')[1][1:-1] for line in results if "Key Content" in line]
        try:
            passList.append(results[0])
        except IndexError:
            passList.append('')

    printInProgram()

def printInProgram():
    global showPass

    clear()

    if showPass:
        rowNum = 1
        Label1 = Label(home, text=f'Here is a list of all your known wifi networks and their passwords:').place(x=425, y=rowNum*30)
        rowNum += 1
        for wifi in range(len(wifis)):
            if passList[wifi] != '':
                Label1 = Label(home, text=f'SSID: {wifis[wifi]}').place(x=450, y=rowNum*30)
                Label2 = Label(home, text=f'Password: {passList[wifi]}').place(x=600, y=rowNum*30)
            else:
                Label1 = Label(home, text=f'SSID: {wifis[wifi]}').place(x=450, y=rowNum*30)
                Label2 = Label(home, text=f'Password: None found!').place(x=600, y=rowNum*30)
            rowNum += 1
        
        searchForButton = Button(home, text='Search for a specific network', command=searchFor, height=2, width=30).place(x=800, y=0)
        showButton = Button(home, text='Hide passwords', command=hidePassWord, height=2, width=30).place(x=150, y=0)
    else:
        rowNum = 1
        Label1 = Label(home, text=f'Here is a list of all your known wifi networks').place(x=450, y=rowNum*30)
        rowNum += 1
        for wifi in range(len(wifis)):
            if passList[wifi] != '':
                Label1 = Label(home, text=f'SSID: {wifis[wifi]}').place(x=450, y=rowNum*30)
                Label2 = Label(home, text=f'Password: ********').place(x=600, y=rowNum*30)
            else:
                Label1 = Label(home, text=f'SSID: {wifis[wifi]}').place(x=450, y=rowNum*30)
                Label2 = Label(home, text=f'Password: ********').place(x=600, y=rowNum*30)
            rowNum += 1
        
        searchForButton = Button(home, text='Search for a specific network', command=searchFor, height=2, width=30).place(x=800, y=0)
        showButton = Button(home, text='Show passwords', command=passForPass, height=2, width=30).place(x=150, y=0)

def passForPass():
    global passForPassEntry, enteredPass

    if not enteredPass:
        clear()
        enteredPass = True
        passForPassLabel = Label(home, text="Please enter your password:").pack()
        passForPassEntry = Entry(home, width=40)
        passForPassEntry.pack()
        passForPassButton = Button(home, text='Submit', command=passForPass2).pack()
        home.bind('<Return>', passForPass2)
    else:
        showPassWord()

def passForPass2(event=None):
    global passForPassEntry
    if hashlib.sha1(passForPassEntry.get().encode('utf-8').strip()).hexdigest() == "3bed76eaf1f24ca8dd40308d7c6b2e47905ed885":      # password is 'your password'
        showPassWord()

def showPassWord():
    global showPass, counter, used
    if used:
        counter = -1
    showPass = True
    printInProgram()

def hidePassWord():
    global showPass, counter, used
    if used:
        counter = -1
    showPass = False
    printInProgram()

def searchFor():
    global searchEntry
    home.bind('<Return>', searchFor2)
    searchEntry = Entry(home, width=30)
    searchEntry.place(x=800, y=40)
    entryButton = Button(home, text='Search', command=searchFor2, height=1, width=15).place(x=800,y=60)

def searchFor2(event=None):
    global counter, showPassWord, used
    if showPass:
        if used:
            if counter >= 2:
                for i in range(counter):
                    home.winfo_children()[-1].destroy()
            elif counter == -1:
                counter = 0
            else:
                home.winfo_children()[-1].destroy()
        else:
            used = True
        counter = 0
        used = 0
        searchWifi = searchEntry.get().strip()
        for word in [x.lower() for x in wifis]:
            if searchWifi.lower() in word:
                Label9 = Label(home, text=f'SSID: {wifis[[x.lower() for x in wifis].index(word)]}').place(x=800, y=90+counter/2*45)
                Label10 = Label(home, text=f'Password: {passList[[x.lower() for x in wifis].index(word)]}').place(x=800, y=110+counter/2*45)
                counter += 2
        if counter == 0:
            Label9 = Label(home, text=f'No network with that name found').place(x=800, y=90+counter*40)
            counter += 1
    else:
        if used:
            if counter > 1:
                for i in range(counter):
                    home.winfo_children()[-1].destroy()
            else:
                home.winfo_children()[-1].destroy()
        else:
            used = True
        counter = 0
        searchWifi = searchEntry.get().strip()
        for word in [x.lower() for x in wifis]:
            if searchWifi.lower() in word:
                Label9 = Label(home, text=f'SSID: {wifis[[x.lower() for x in wifis].index(word)]}').place(x=800, y=90+counter/2*45)
                Label10 = Label(home, text=f'Password: ********').place(x=800, y=110+counter/2*45)
                counter += 2
        if counter == 0:
            Label9 = Label(home, text=f'No network with that name found').place(x=800, y=90+counter*40)
            counter += 1

def clear():
    for widget in home.winfo_children():
        widget.destroy()

def main():
    global home, showPass, enteredPass, used

    showPass = False
    enteredPass = False
    used = False

    home = Tk()
    home.title("Search for wifi passwords")
    home.geometry("1200x600")

    searchButton = Button(home, text='Search for known networks and their passwords', command=getWifiPasswords, height=5, width=56).place(x=400, y=200)


    home.mainloop()

if __name__ == '__main__':
    main()