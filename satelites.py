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
    global score
    for i in range(satelite_number):
        satelite = Actor("satelite")
        satelite.pos = (random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50))
        satelites.append(satelite)
    start_time = time()

def draw():
    global total_time
    screen.blit("space", (0,0))
    number = 1
    for satelite in satelites:
        screen.draw.text(str(number),(satelite.pos[0], satelite.pos[1] + 20))
        satelite.draw()
        number += 1

        

