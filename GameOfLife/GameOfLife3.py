import numpy as np 
import pygame as pg
import time

#calculating the new board
def update(frameNum, board, N): 
    newboard = board.copy()
    for i in range(N):
        for j in range(N):
            total = int(board[i, (j-1)%N] + board[i, (j+1)%N] + 
                                board[(i-1)%N, j] + board[(i+1)%N, j] + 
                                board[(i-1)%N, (j-1)%N] + board[(i-1)%N, (j+1)%N] + 
                                board[(i+1)%N, (j-1)%N] + board[(i+1)%N, (j+1)%N]) 
            if board[i, j]  == ON: 
                if (total < 2) or (total > 3): 
                    newboard[i, j] = OFF 
            else: 
                if total == 3: 
                    newboard[i, j] = ON
    board[:] = newboard[:]
    return board

#def for pausing
def paused():

    smallText = pg.font.SysFont("comicsansms",20)
    TextSurf, TextRect = text_objects("Paused", smallText, bright_red)
    TextRect.center = ((xmax/2),10)
    screen.blit(TextSurf, TextRect)
    

    while pause:
        for event in pg.event.get():

            if event.type == pg.QUIT:
                pg.quit()
                quit()
        button("Continue",0,0,100,50,green,bright_green,unpause)
        button("Quit",1100,0,100,50,red,bright_red,quitgame)

        pg.display.update()

#def for unpausing
def unpause():
    global pause
    pause = False

#def to make render text in pyagame easier
def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

#def to make a button in pygame
def button(msg,a,b,c,d,ic,ac,action=None):
    mouse = pg.mouse.get_pos()
    click = pg.mouse.get_pressed()
    if a+c > mouse[0] > a and b+d > mouse[1] > b:
        pg.draw.rect(screen, ac, (a,b,c,d))
        if click[0] == 1 and action != None:
            action()
    else:
        pg.draw.rect(screen, ic, (a,b,c,d))
    smallText = pg.font.SysFont("comicsansms",20)
    textSurface, textRect = text_objects(msg, smallText, WHITE)
    textRect.center = ((a+(c/2)), (b+(d/2)))
    screen.blit(textSurface, textRect)

#def to quit the game
def quitgame():
    pg.quit
    quit(0)

#def to undo last edited thing
def undo():
    global lstcox
    global lstcoy
    if lstcox:
        if board[lstcox[-1],lstcoy[-1]] == 1:
            board[lstcox[-1],lstcoy[-1]] = 0
            del lstcox[-1]
            del lstcoy[-1]
        elif board[lstcox[-1],lstcoy[-1]] == 0:
            board[lstcox[-1],lstcoy[-1]] = 1
            del lstcox[-1]
            del lstcoy[-1]

#def to go out of editormode
def uned():
    global ed
    ed = 0

#constants and variables
N = 150
k = 0
ed = 0
lstx = []
lsty = []
lstcox = []
lstcoy = []
ON = 1
OFF = 0
running = True
pause = False
question = True

while question:
    #opening from file, a random board or a blank board
    print("How would you like your initial board to be?")
    print("1. I would like to start from a file.")
    print("2. I would like to start with a randomly generated board.")
    print("3. I would like to start with a blank board and draw something myself.")
    ask = int(input("Please answer 1, 2 or 3: "))

    if ask == 1:
        question = False
        #creating a board
        board = np.zeros((N,N))

        #reading the file and implementing in the board
        inp = open(input("What is the filename of your .lif file (please make sure it is in the same directory as this .py program)"))
        for line in inp:
            x = int(N/2)
            y = x
            if not line.startswith("#"):
                columns = line.split(" ")
                print(columns[0], columns[1])
                x = x + int(columns[0])
                y = y + int(columns[1])
                lstx.append(x)
                lsty.append(y)

        for i in range(len(lstx)):
            board[lstx[i], lsty[i]] = 1

        inp.close()

    #creating a random board
    elif ask == 2:
        board = np.random.choice([0, 1], size=(N,N))
        question = False
    
    #creating an empty board
    elif ask == 3:
        board = np.zeros((N,N))
        print("When the animation starts, please press e right away.")
        question = False

    else:
        print("I did not understand your answer.")
        time.sleep(2)

print("First, the initial board will be shown for 3 seconds, then the animation will start.")
time.sleep(2)

#the animation
pg.init()

xmax = 1200
ymax = 1200

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
red = (200,0,0)
bright_red = (255,0,0)
green = (0,200,0)
bright_green = (0,255,0)

screen = pg.display.set_mode((xmax,ymax))
pg.display.set_caption("My Game of Life")
screen.fill(BLACK)
while running:
    screen.fill(BLACK)
    w = 8
    x = 0
    y = 0
    for i in range(N):
        for j in range(N):
            if board[i,j] ==ON:
                box = pg.Rect(x, y, w-2, w-2)
                pg.draw.rect(screen, WHITE, box)
            y = y + w
        x = x + w
        y = 0
    pg.display.flip()
    if k == 0:
        k = k + 1
        time.sleep(3)
    if ed == 0:
        board = update(10, board, N)
    elif ed == 1:
        lstcox.clear
        lstcoy.clear
        while ed == 1:
            mouse1 = pg.mouse.get_pos()
            for event in pg.event.get():
                if event.type == pg.MOUSEBUTTONDOWN and mouse1[0] > 50 and 100 < mouse1[1] < 1100:
                    cox = int((mouse1[0] - (mouse1[0]%8))/8)
                    coy = int((mouse1[1] - (mouse1[1]%8))/8)
                    lstcox.append(cox)
                    lstcoy.append(coy)
                    if board[cox, coy] == 0:
                        board[cox, coy] = 1
                    elif board[cox, coy] == 1:
                        board[cox, coy] = 0
                        screen.fill(BLACK)
                w = 8
                x = 0
                y = 0
                for i in range(N):
                    for j in range(N):
                        if board[i,j] ==ON:
                            box = pg.Rect(x, y, w-2, w-2)
                            pg.draw.rect(screen, WHITE, box)
                        y = y + w
                    x = x + w
                    y = 0
                button("Continue",0,0,100,50,green,bright_green,uned)
                button("Undo",1100,0,100,50,red,bright_red,undo)

                smallText = pg.font.SysFont("comicsansms",20)
                TextSurf, TextRect = text_objects("Editmode", smallText, bright_red)
                TextRect.center = ((xmax/2),10)
                screen.blit(TextSurf, TextRect)  

                pg.display.flip()

    keys = pg.key.get_pressed()
    if keys[pg.K_SPACE]:
        pause = True
        paused() 
    if keys[pg.K_e]:
        ed = 1
    if keys[pg.K_ESCAPE]:
        running = False
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
pg.quit
