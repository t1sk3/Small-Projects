import pygame as pg
from math import *
import time

class branch:
    def __init__(self, x1, y1, x2, y2, angle):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.angle = angle
        self.length = sqrt((y1-y2)**2 + (x1-x2)**2)
    
    def draw(self):
        pg.draw.line(screen, BLACK, (self.x1, self.y1), (self.x2, self.y2), 1)
        pg.display.flip()
    
    def create(self):
        xl = self.x2 + sin(radians(self.angle + (ANGLE)))*self.length/FRACTION
        yl = self.y2 + cos(radians(self.angle + (ANGLE)))*self.length/FRACTION
        xr = self.x2 + sin(radians(self.angle - (ANGLE)))*self.length/FRACTION
        yr = self.y2 + cos(radians(self.angle - (ANGLE)))*self.length/FRACTION
        return [branch(self.x2, self.y2, xl, yl, self.angle + (ANGLE)), branch(self.x2, self.y2, xr, yr, self.angle - (ANGLE))]

def main():
    global screen, BLACK, WHITE, ANGLE, FRACTION
    # Starting variables
    # Starting coordinate of the first branch
    x1 = 600
    y1 = 1200
    # Ending coordinate of the first branch
    x2 = 600
    y2 = 800
    # The angle towards the y axis (changing this without changing the coordinates will change the tree)
    angle = 180
    # Angle of the next branches, as well as the fraction of its length
    ANGLE = 30
    FRACTION = 1.85
    
    pg.init()

    xmax = 1200
    ymax = 1200

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    screen = pg.display.set_mode((xmax,ymax))
    pg.display.set_caption("Split Tree")
    screen.fill(WHITE)

    pg.display.flip()

    newBranch = branch(x1,y1,x2,y2,angle)
    newBranch.draw()
    lst = newBranch.create()
    used = []
        
    while True:
        new1 = []
        for br in lst:
            br.draw()
            used.append(br)
            new = br.create()
            new1.append(new[0])
            new1.append(new[1])
            #time.sleep(0.01)
        for br2 in new1:
            lst.append(br2)
        for u in used:
            lst.remove(u)
        used.clear()

if __name__ == "__main__":
    main()