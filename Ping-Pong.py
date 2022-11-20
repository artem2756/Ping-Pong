from pygame import *
from random import randint
from time import time as timer
win_width = 1820
win_height = 1080
w = display.set_mode((win_width, win_height))
display.set_caption('Пинг-Понг')
background = (200, 255, 255)
w.fill(background)

class GameSprite(sprite.Sprite):
    def __init__ (self,player_image,player_x,player_y,size_x,size_y,player_speed,):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        w.blit(self.image, (self.rect.x,self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x>0:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x<625:
            self.rect.x += self.speed
        
clock = time.Clock()
FPS = 60
game = True

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()
    clock.tick(FPS)
