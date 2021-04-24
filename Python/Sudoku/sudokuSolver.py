def checkValue(sudoku, value, x, y):
    lstx = []
    lsty = []
    lstr = []
    if x > 5:
        xlimU = 5
        xlimA = 9
    elif x > 2:
        xlimU = 2
        xlimA = 6
    else:
        xlimU = -1
        xlimA = 3
    
    if y > 5:
        ylimU = 5
        ylimA = 9
    elif y > 2:
        ylimU = 2
        ylimA = 6
    else:
        ylimU = -1
        ylimA = 3

    for y1 in sudoku:
        for x1 in y1:
            if y1.index(x1) == x:
                lsty.append(x1)
            if sudoku.index(y1) == y:
                lstx.append(x1)
            if xlimU < y1.index(x1) < xlimA and ylimU < sudoku.index(y1) < ylimA:
                lstr.append(x1)
    if value not in lstr and value not in lstx and value not in lsty:
        return True
    else:
        return False

def solveSudoku(sudoku):
    finished = True
    for y in sudoku:
        if 0 in y:
            finished = False
    
    if finished:
        return sudoku

    found = False
    for y1 in sudoku:
        for x1 in y1:
            if x1 == 0:
                x = x1
                y = y1
                found = True
                break
        if found:
            break
                
    i = 0
    xind = y.index(x)
    yind = sudoku.index(y)
    while True:
        i += 1
        if i == 10:
            sudoku[yind][xind] = 0
            raise ValueError
        elif checkValue(sudoku, i, xind, yind):
            sudoku[yind][xind] = i
            try:
                return solveSudoku(sudoku)
            except ValueError:
                sudoku[yind][xind] = 0
                continue

'''SUDOKU = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
]'''

SUDOKU = [
    [8,0,0,0,0,0,0,0,0],
    [0,0,3,6,0,0,0,0,0],
    [0,7,0,0,9,0,2,0,0],
    [0,5,0,0,0,7,0,0,0],
    [0,0,0,0,4,5,7,0,0],
    [0,0,0,1,0,0,0,3,0],
    [0,0,1,0,0,0,0,6,8],
    [0,0,8,5,0,0,0,1,0],
    [0,9,0,0,0,0,4,0,0]
]

solved = solveSudoku(SUDOKU)
for line in solved:
    print(line)