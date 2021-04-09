import pygame as pg

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 255, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165 ,0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)

class Spot:
    def __init__(self, x, y):
        self.checked = False
        self.is_start = False
        self.is_end = False
        self.is_path = False
        self.is_barrier = False
        self.length = -1
        self.color = WHITE
        self.x = x
        self.y = y
        self.is_last = False
        self.path = []
    
    def make_start(self):
        self.is_start = True
        self.color = GREEN
    
    def make_end(self):
        self.is_end = True
        self.color = RED
    
    def make_checked(self):
        self.checked = True
    
    def make_path(self):
        self.is_path = True
        self.color = TURQUOISE
    
    def make_barrier(self):
        self.is_barrier = True
        self.color = BLACK
    
    def reset(self):
        self.is_start = False
        self.is_end = False
        self.is_path = False
        self.is_barrier = False
        self.color = WHITE
    
    def draw(self):
        pg.draw.rect(screen, self.color, (self.x*15 + 1, self.y*15 + 1, 15-2, 15-2))
        pg.display.flip()
    
    def check(self, l):
        self.length = l
        self.checked = True
        self.is_last = True
        self.color = ORANGE
    
    def make_path(self, path):
        self.path = path
        self.path.append(self)

    def get_path(self):
        return self.path

XPIX = 50
YPIX = 50

pg.init()

xmax = XPIX*15
ymax = YPIX*15

screen = pg.display.set_mode((xmax,ymax))
pg.display.set_caption("Pathfinding")
screen.fill(BLACK)
clock = pg.time.Clock()

board = []
for i in range(50):
    line = []
    for j in range(50):
        next_spot = Spot(j,i)
        next_spot.draw()
        line.append(next_spot)
    board.append(line)

searching = True
setting_up = True
start = False
end = False
barriers = False
breaking = False
while searching:
    for event in pg.event.get():
        if breaking:
            break
        if event.type == pg.QUIT:
            pg.quit
        
    if setting_up:
        if pg.mouse.get_pressed()[0]:
            pos = pg.mouse.get_pos()
            x = pos[0]//15
            y = pos[1]//15
        
            if not start:
                board[y][x].make_start()
                board[y][x].draw()
                board[y][x].is_last = True
                start = True
            elif not end and not board[y][x].is_start:
                board[y][x].make_end()
                board[y][x].draw()
                end = True
            elif not barriers and not board[y][x].is_start and not board[y][x].is_end:
                board[y][x].make_barrier()
                board[y][x].draw()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RETURN:
                barriers = True
                if start and end and barriers:
                    setting_up = False
    else:
        for line in board:
            if breaking:
                break
            for s in line:
                if breaking:
                    break
                if s.is_last:
                    x = line.index(s)
                    y = board.index(line)
                    s.is_last = False
                    s.color = GREY
                    s.draw()
                    if not x+1 > 49:
                        new = board[y][x+1]
                        if not new.checked and not new.is_barrier:
                            new.check(s.length+1)
                            new.draw()
                            new.make_path(list(s.get_path()))
                        if new.is_end:
                            searching = False
                            breaking = True
                            break
                    if not x-1 < 0:
                        new = board[y][x-1]
                        if not new.checked and not new.is_barrier:
                            new.check(s.length+1)
                            new.draw()
                            new.make_path(list(s.get_path()))
                        if new.is_end:
                            searching = False
                            breaking = True
                            break
                    if not y+1 > 49:
                        new = board[y+1][x]
                        if not new.checked and not new.is_barrier:
                            new.check(s.length+1)
                            new.draw()
                            new.make_path(list(s.get_path()))
                        if new.is_end:
                            searching = False
                            breaking = True
                            break
                    if not y-1 < 0:
                        new = board[y-1][x]
                        if not new.checked and not new.is_barrier:
                            new.check(s.length+1)
                            new.draw()
                            new.make_path(list(s.get_path()))
                        if new.is_end:
                            searching = False
                            breaking = True
                            break

    clock.tick(150)
            
making_path = True
while making_path:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit

    for line in board:
        for s in line:
            if s.is_end:
                making_path = False
                path = s.get_path()
                for sp in path:
                    sp.color = PURPLE
                    sp.draw()
                break
    clock.tick(150)

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit
    clock.tick(150)


                    

