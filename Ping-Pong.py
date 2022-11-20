from pygame import *
from random import randint
from time import time as timer
win_width = 1820
win_height = 1080
w = display.set_mode((win_width, win_height))
display.set_caption('Пинг-Понг')
background = (200, 255, 255)
w.fill(background)

clock = time.Clock()
FPS = 60
game = True

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()
    clock.tick(FPS)