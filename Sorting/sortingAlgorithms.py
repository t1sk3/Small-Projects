import time
import random

def sortLst(lst):
    res = []
    while True:
        minimum = None
        for num in lst:
            if minimum is None or num < minimum:
                minimum = num
        res.append(minimum)
        lst.remove(minimum)
        if len(lst) == 0:
            return res
        
def sortLstRecur(lst):
    def splitLst(lst):
        lst1 = []
        lst2 = []
        i = 0
        length = len(lst)
        if length == 2:
            if lst[0] > lst[1]:
                lst2.append(lst[0])
                lst1.append(lst[1])
                return lst1, lst2
            else:
                lst1.append(lst[0])
                lst2.append(lst[1])
                return lst1, lst2
        while True:
            minimum = None
            for num in lst:
                if minimum is None or num < minimum:
                    minimum = num
            i += 1
            lst.remove(minimum)
            lst1.append(minimum)
            if i == int(length/2) + 1:
                break
        for num in lst:
            lst2.append(num)
        return lst1, lst2

    lst1, lst2 = splitLst(lst)
    if len(lst1) == 1 and len(lst2) == 0:
        return lst1
    lst3 = sortLstRecur(lst1)
    lst4 = sortLstRecur(lst2)
    for num in lst4:
        lst3.append(num)
    return lst3

def bubble_sort(lst):
    for i in range(len(lst)):
        for j in range(len(lst) - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst

def quickSort(lst):
    if len(lst) == 0:
        return lst
    spil = lst[len(lst)//2]
    count = lst.count(spil)
    l = []
    r = []
    for i in lst:
        if i > spil:
            r.append(i)
        elif i < spil:
            l.append(i)
    return quickSort(l) + [spil] * count + quickSort(r)

def shotgun_sort(lst):
    res = []
    for num in lst:
        res.append(num)
    while res != sorted(lst):
        random.shuffle(res)
    return res

if __name__ == "__main__":
    LIMIT = 400
    base = []
    lst = []

    for i in range(LIMIT):
        base.append(i+1)
    for i in range(LIMIT):
        num = random.choice(base)
        base.remove(num)
        lst.append(num)

    backup = list(lst)

    sorting_funcs = [sortLst, sortLstRecur, bubble_sort, quickSort, sorted]

    for sorting_func in sorting_funcs:
        now = time.time()
        print(sorting_func(lst), sorting_func.__name__, ":", time.time() - now)
        lst = list(backup)