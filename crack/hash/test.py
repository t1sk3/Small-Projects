test = open("extend10mil.txt")
lst = []
for line in test:
    lst.append(line)
test.close()
print(len(lst))