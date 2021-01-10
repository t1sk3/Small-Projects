import pygame as pg
import time

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

def findZero(sudoku):
    for y in sudoku:
        for x in y:
            if x == 0:
                return x, y

def solveSudoku(sudoku):
    finished = True
    for y in sudoku:
        if 0 in y:
            finished = False
    
    if finished:
        return sudoku

    #x, y = findZero(sudoku)
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
            drawSudokuSolving(sudoku)
            pg.display.flip()
            raise ValueError
        elif checkValue(sudoku, i, xind, yind):
            sudoku[yind][xind] = i
            drawSudokuSolving(sudoku)
            pg.display.flip()
            try:
                return solveSudoku(sudoku)
            except ValueError:
                sudoku[yind][xind] = 0
                drawSudokuSolving(sudoku)
                pg.display.flip()
                continue

def button(msg,a,b,c,d,ic,ac,action=None):
    mouse = pg.mouse.get_pos()
    click = pg.mouse.get_pressed()
    if a+c > mouse[0] > a and b+d > mouse[1] > b:
        pg.draw.rect(screen, ac, (a,b,c,d))
        if click[0] == 1 and action != None:
            action()
    else:
        pg.draw.rect(screen, ic, (a,b,c,d))
    smallText = pg.font.SysFont("calibri",20)
    textSurface, textRect = text_objects(msg, smallText, WHITE)
    textRect.center = (round(a+(c/2)), round(b+(d/2)))
    screen.blit(textSurface, textRect)

def drawLines():
    x = 75
    y = 50

    for i in range(0,10):
        if i == 0 or i == 3 or i == 6 or i == 9:
            pg.draw.line(screen, BLACK, (x+50*i, y), (x+50*i, y*10), 5)
        else:
            pg.draw.line(screen, BLACK, (x+50*i, y), (x+50*i, y*10), 1)
    for i in range(0,10):
        if i == 0 or i == 3 or i == 6 or i == 9:
            pg.draw.line(screen, BLACK, (x, y+50*i), (x*7, y+50*i), 5)
        else:
            pg.draw.line(screen, BLACK, (x, y+50*i), (x*7, y+50*i), 1)

    pg.display.flip()

def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()


def renderText(text, x, y, color):
    smallText = pg.font.SysFont("calibri",22)
    TextSurf, TextRect = text_objects(text, smallText, color)
    TextRect.center = (x, y)
    screen.blit(TextSurf, TextRect)

def drawSudokuSolving(sudoku):
    for y in sudoku:
        for x in y:
            if x != 0:
                x1 = 100 + 50*y.index(x)
                y1 = 75 + 50*sudoku.index(y)
                renderText(str(x), x1, y1, red)
            else:
                x1 = 80 + 50*y.index(x)
                y1 = 55 + 50*sudoku.index(y)
                rectangle = pg.Rect(x1, y1, 40, 40)
                pg.draw.rect(screen, WHITE, rectangle) 

def drawSudoku(sudoku):
    for y in sudoku:
        for x in y:
            if x != 0:
                x1 = 100 + 50*y.index(x)
                y1 = 75 + 50*sudoku.index(y)
                renderText(str(x), x1, y1, BLACK)
            else:
                x1 = 80 + 50*y.index(x)
                y1 = 55 + 50*sudoku.index(y)
                pg.Rect(x1, y1, 40, 40)

def solveButton():
    solving = True

def main():
    global screen, BLACK, WHITE, solving, green, bright_green, red
    pg.init()

    xmax = 600
    ymax = 600

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    green = (0,200,0) 
    bright_green = (0,255,0)
    red = (200,0,0)

    screen = pg.display.set_mode((xmax,ymax))
    pg.display.set_caption("SudokuSolver")
    screen.fill(WHITE)

    pg.display.flip()

    drawLines()

    drawSudoku(SUDOKU)

    solving = False
    counter = 0

    while True:
        if not solving:
            #button("Solve",0,0,100,40,green,bright_green,solveButton)
            if counter == 1:
                solving = True
            elif counter < 1:
                counter += 1
                print(counter)
            pg.display.flip()
        if solving:
            solveSudoku(SUDOKU)
            pg.display.flip()
            solving = False

'''SUDOKU = [
    [5,3,4,6,7,8,9,1,2],
    [6,7,2,1,9,5,3,4,8],
    [1,9,8,3,4,2,5,6,7],
    [8,5,9,7,6,1,4,2,3],
    [4,2,6,8,5,3,7,9,1],
    [7,1,3,9,2,4,8,5,6],
    [9,6,1,5,3,7,2,8,0],
    [2,8,7,4,1,9,6,3,5],
    [3,4,5,2,8,6,1,0,0]
]'''

SUDOKU = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
]

'''SUDOKU = [
    [8,0,0,0,0,0,0,0,0],
    [0,0,3,6,0,0,0,0,0],
    [0,7,0,0,9,0,2,0,0],
    [0,5,0,0,0,7,0,0,0],
    [0,0,0,0,4,5,7,0,0],
    [0,0,0,1,0,0,0,3,0],
    [0,0,1,0,0,0,0,6,8],
    [0,0,8,5,0,0,0,1,0],
    [0,9,0,0,0,0,4,0,0]
]'''

'''SUDOKU = [
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0]
]'''

if __name__ == "__main__":
    main()
    #print(solveSudoku(SUDOKU))