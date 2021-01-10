import zipfile

charlist = 'abcdefghijklmnopqrstuvwxyz' #ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890~`!@#$%^&*()_-+={[}]|\:;<,>.?/'
complete = []

for current in range(5):
    a = [i for i in charlist]
    for x in range(current):
        a = [y + i for i in charlist for y in a]
    complete = complete + a
complete = sorted(complete)

print('The list of possible passwords has been created')
print(f'It contains {len(complete)} words')

z = zipfile.ZipFile('secret.zip')

tries = 0

for password in complete:
    if tries % 10000 == 0:
        print(tries, password)
    if password == 'passw':
        print('Got it')
    try:
        tries += 1
        z.setpassword(password.encode('ascii'))
        z.extract('secret.txt')
        print(f'Password was found in {tries} tries! It was {password}')
        break
    except:
        pass