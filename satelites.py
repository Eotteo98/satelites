import pgzrun
import random
import time



WIDTH = 800
HEIGHT = 600

start_time = 0 
end_time = 0
total_time = 0
next_satelite = 0
satelite_number = 8
satelites = []
lines = []

def create_satelites():
    global start_time
    for i in range(satelite_number):
        satelite = Actor("satelite")
        satelite.pos = (random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50))
        satelites.append(satelite)
    start_time = time.time()

def draw():
    global total_time
    screen.blit("space", (0,0))
    number = 1
    for satelite in satelites:
        screen.draw.text(str(number),(satelite.pos[0], satelite.pos[1] + 20))
        satelite.draw()
        number += 1
    
    for line in lines:
        screen.draw.line(line[0], line[1], "white")
    
    if next_satelite < satelite_number:
        total_time = time.time()- start_time
        screen.draw.text(str(round(total_time, 1)), (10,10), fontsize = 30)
    
    else:
        screen.draw.text(str(round(total_time, 1)), (10,10), fontsize = 30)

def update():
    pass


def on_mouse_down(pos):
    global lines, next_satelite
    if next_satelite < satelite_number:
        if satelites[next_satelite].collidepoint(pos):
            if next_satelite:
                lines.append((satelites[next_satelite - 1].pos, satelites[next_satelite].pos))
            next_satelite += 1
        else:
            lines = []
            next_satelite = 0

create_satelites()
pgzrun.go()


