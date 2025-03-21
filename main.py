from pygame import *
import random

from pygame.constants import KEYDOWN, K_SPACE
tym = 0
window = display.set_mode((700, 500))
display.set_caption(" Догонялки ")
background = transform.scale(image.load("galaxy.jpg"), (700, 500))

mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()
display.update()

clock = time.Clock()
FPS = 60


game = True


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed,width,height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.direction = "left"
        self.rect.y = player_y


    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys_pressed[K_d] and self.rect.x < 595:
            self.rect.x += self.speed

    def fire (self):

        bullet=Bullet('bullet.png',self.rect.centerx,self.rect.top,15,20,30)
        bullets.add(bullet)


bullets = sprite.Group()

class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > 500:
            self.rect.x = random.randint(80, 700)
            self.rect.y = 0
            lost = lost + 1
sprite1 = Enemy('ufo.png',random.randint(50, 650),250,7,60,70)
sprite6 = Enemy('ufo.png',random.randint(50, 650),250,7,60,70)
sprite3 = Enemy('ufo.png',random.randint(50, 650),250,7,60,70)
sprite4 = Enemy('ufo.png',random.randint(50, 650),250,7,60,70)
sprite5 = Enemy('ufo.png',random.randint(50, 650),250,7,60,70)
sprite2 = Player('rocket.png',500,400,12,60,70)
monsters = sprite.Group()
lost = 0 #пропущено кораблей

font.init()
font1 = font.SysFont("Arial", 36)
monsters.add(sprite1,sprite3,sprite4,sprite5,sprite6)



class Bullet(GameSprite):
   def update(self):
       if self.rect.y<0:

        self.kill()

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

        elif e.type == KEYDOWN:
             if e.type == K_SPACE:
                ship.fire()

    window.blit(background, (0, 0))
    sprite2.reset()
    sprite2.update()
    monsters.draw(window)
    monsters.update()
    text_lose = font1.render("Пропущено: " + str(lost), 1, (255, 255, 255))
    window.blit(text_lose,(50,50))
    bullets.draw(window)
    bullets.update()
    sprites_list = sprite.groupcollide(
        monsters,bullets,True,True
    )
    for i in sprites_list :
        tym += 1
        sprite1 = Enemy('ufo.png', random.randint(50, 650), 250, 7, 60, 70)
        monsters.add(sprite1)
    display.update()
    clock.tick(FPS)