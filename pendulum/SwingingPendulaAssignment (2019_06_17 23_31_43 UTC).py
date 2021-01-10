import pygame as pg
from math import *

pg.init()

screen_width = 800
screen_height = 500
origin = [screen_width/2,0]
blue = (50,200,255)
grey = (100,100,100)

screen = pg.display.set_mode([screen_width,screen_height])
sphere = pg.image.load('C:\\Users\\matti\\Documents\\Python\\Projects\\pendulum\\sphere.png')
sphere = pg.transform.scale(sphere,(40,40))
sphererect = sphere.get_rect()
centroidsphere = []

#calculations for Length pendulum with n swings per minute
def length(n):  
    g = 9.81
    T = (n/60)**(-1)
    L = g*(T/2/pi)**2
    return L

scalingfactor = 1200

#calculations for sphere coordinates
def coordinates(theta0,L,t):
    g = 9.81
    theta = theta0*cos(sqrt(g/L)*t)
    x = screen_width/2+L*sin(theta)*scalingfactor
    y = L*cos(theta)*scalingfactor
    return [x,y]

lst = []
for n in range(51,66):
    lst.append(length(n))
    print("n = ",n,"-- L:",round(length(n),10))

#definition start time
t0 = 0.001*pg.time.get_ticks()

running = True

while running:
    #time
    t = (0.001*pg.time.get_ticks() - t0)

    screen.fill(blue)
    for n in range(51,66):#display
        pg.draw.line(screen, grey, origin,coordinates(pi/4,length(n),t),3)
        screen.blit(sphere,(coordinates(pi/4,length(n),t)[0]-sphererect.right /2,coordinates(pi/4,length(n),t)[1]-sphererect.bottom/2))
    pg.display.flip()
    
    #End sequences
    keys = pg.key.get_pressed()
    if t > 4000:
        running = False
    if keys[pg.K_ESCAPE]:
        running = False
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    
pg.quit()


