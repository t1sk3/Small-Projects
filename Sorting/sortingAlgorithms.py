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

if __name__ == "__main__":
    print(sortLst([7,4,3,7,2,1,8,9,3,3,7,3,7,32,3,7645,6,78,3,24,7,7,34,75,875,68,4679,237,8,764,8,3586,86]))
    print(sortLstRecur([7,4,3,7,2,1,8,9,3,3,7,3,7,32,3,7645,6,78,3,24,7,7,34,75,875,68,4679,237,8,764,8,3586,86]))
    print(bubble_sort([7,4,3,7,2,1,8,9,3,3,7,3,7,32,3,7645,6,78,3,24,7,7,34,75,875,68,4679,237,8,764,8,3586,86]))
    print(sorted([7,4,3,7,2,1,8,9,3,3,7,3,7,32,3,7645,6,78,3,24,7,7,34,75,875,68,4679,237,8,764,8,3586,86]))