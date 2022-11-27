from pygame import *
from random import randint
from time import time as timer
win_width = 900
win_height = 700
w = display.set_mode((win_width, win_height))
display.set_caption('Пинг-Понг')
background = (200, 255, 255)
w.fill(background)

class GameSprite(sprite.Sprite):
    def __init__ (self,player_image,player_x,player_y,size_x,size_y,player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        w.blit(self.image, (self.rect.x,self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y>0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y<625:
            self.rect.y += self.speed
    def update_p(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y>0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y<625:
            self.rect.y += self.speed


player1 = Player("ракетка.png", 50, 0, 50, 200, 10)
player2 = Player("ракетка.png", 800, 0, 50, 200, 10)
ball = GameSprite('ball.png', 200, 200, 60, 60, 60)

speed_x = 3
speed_y = 3

font.init()
font = font.SysFont('Georgia',36)
text_won = font.render("Левый проиграл", True, (0,0,0))
text_win = font.render("Правый проиграл", True, (0,0,0))

clock = time.Clock()
FPS = 60
game = True
finish = False

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        w.fill(background)
        player1.reset()
        player1.update_l()
        player2.reset()
        player2.update_p()
        ball.reset()
        ball.update()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if ball.rect.y > win_height - 58 or ball.rect.y <0:
            speed_y *= -1
        if sprite.collide_rect(player1, ball) or sprite.collide_rect(player2, ball):
            speed_x *= -1
        if ball.rect.x <0:
            finish = True
            w.blit(text_won, (310,350))
        if ball.rect.x > win_width:
            finish = True
            w.blit(text_win, (310,350))
    display.update()
    clock.tick(FPS)
