import os

#os.rename(src, dst)

for count, filename in enumerate(os.listdir("C:\\Users\\matti\\Documents\\Python\\Projects\\Rename")):
    print(count, filename) 
    dst ="Hostel" + str(count) + ".jpg"
    src ='xyz'+ filename 
    dst ='xyz'+ dst