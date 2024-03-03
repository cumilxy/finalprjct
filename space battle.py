from pygame import *
'''Необхідні класи'''
 
# клас-батько для спрайтів
class GameSprite(sprite.Sprite):
    #конструктор класу
    def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
        super().__init__()
        # кожен спрайт повинен зберігати властивість image - зображення
        self.image = transform.scale(image.load(player_image), (wight, height)) #разом 55,55 - параметри
        self.speed = player_speed
        # кожен спрайт повинен зберігати властивість rect - прямокутник, в який він вписаний
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
   
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

# клас-спадкоємець для спрайту-гравця (керується стрілками)    
class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

#ігрова сцена:

win_width = 1200
win_height = 600
window = display.set_mode((win_width, win_height))
back = 
spaceship1 = Player('spaceship1.png',0,0,15,10,15)
spaceship2 = Player('spaceship2.png',1200,600,15,10,15)
monster1 = GameSprite('moster1.png', 345,600,9,15,10)
monster2 = GameSprite('moster2.png', 582,894,9,15,10)
monster3 = GameSprite('moster3.png', 582,894,9,15,10)
monster4 = GameSprite('moster4.png', 582,894,9,15,10)
coin = GameSprite('coinspace.png', 582,894,9,15,10)
h1 = GameSprite('human1.png', 582,894,9,15,10)
h2 = GameSprite('human2.png', 582,894,9,15,10)
h3 = GameSprite('human3.png', 582,894,9,15,10)
h4 = GameSprite('human4.png', 582,894,9,15,10)
h5 = GameSprite('human5.png', 582,894,9,15,10)
m1 = GameSprite('marshmn1.png', 582,894,9,15,10)
m2 = GameSprite('marshmn2.png', 582,894,9,15,10)
m3 = GameSprite('marshmn3.png', 582,894,9,15,10)
m4 = GameSprite('marshmn4.png', 582,894,9,15,10)
m5 = GameSprite('marshmn5.png', 582,894,9,15,10)
display.set_icon(back,'spaceback.png')
display.set_caption('space battle') 
#player1 = GameSprite('racket.png',50,100,10,30,120)






#прапорці, що відповідають за стан гри
game = True
clock = time.Clock()


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    #player1.reset()

spaceship1.reset()
spaceship2.reset()
   
display.update()
clock.tick(60)


