from pygame import *
'''Необхідні класи'''
 
class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height

        # картинка стіни - прямокутник потрібних розмірів і кольору
        self.image = Surface([self.width, self.height])
        self.image.fill((color_1, color_2, color_3))
# кожен спрайт має зберігати властивість rect - прямокутник
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y

    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))



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
        if keys [K_RIGHT] and self.rect.x < win_width - 150:
            self.rect.x += self.speed
        if keys [K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed
    def update_l(self):
        keys = key.get_pressed()
        
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
        if keys[K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys [K_d] and self.rect.x < win_width - 100:
            self.rect.x += self.speed
        
    
    def fire(self):
        bullet = Bullet('bullet1.png',self.rect.centerx,self.rect.centery,15,15,10)
        bullets.add(bullet)
    
    def fire2(self):
        bullet = Bullet2('bullet2.png',self.rect.centerx,self.rect.centery,15,15,10)
        bullets2.add(bullet)

class Bullet(GameSprite):
    def update(self):
        self.rect.x += 10
        if self.rect.x > 1100:
            self.kill()
bullets = sprite.Group()

class Bullet2(GameSprite):
    def update(self):
        self.rect.x -= 10
        if self.rect.x < 0:
            self.kill()
bullets2 = sprite.Group()



#ігрова сцена:

win_width = 1200
win_height = 600
window = display.set_mode((win_width, win_height))
back = image.load('spaceback.png')
spaceship1 = Player('spaceship1.png',100,450,15,100,125)
spaceship2 = Player('spaceship2.png',1000,400,15,150,200)
monster1 = GameSprite('moster1.png', 345,600,9,15,10)
monster2 = GameSprite('moster2.png', 582,894,9,15,10)
monster3 = GameSprite('moster3.png', 582,894,9,15,10)
monster4 = GameSprite('moster4.png', 582,894,9,15,10)
coin = GameSprite('coinspace.png', 582,894,9,15,10)
h1 = GameSprite('human1.png', 0,450,9,60,90)
h2 = GameSprite('human2.png', 0,350,9,60,90)
h3 = GameSprite('human3.png', 0,250,9,60,90)
h4 = GameSprite('human4.png', 0,150,9,60,90)
h5 = GameSprite('human5.png', 0,50,9,60,90)
m1 = GameSprite('marshmn1.png', 1140,450,9,60,90)
m2 = GameSprite('marshmn2.png', 1140,350,9,60,90)
m3 = GameSprite('marshmn3.png', 1140,250,9,60,90)
m4 = GameSprite('marshmn4.png', 1140,150,9,60,90)
m5 = GameSprite('marshmn5.png', 1140,50,9,60,90)
blackhole = GameSprite('black hole.jpg', 400, 0, 0, 350, 300)

display.set_caption('space battle') 
#player1 = GameSprite('racket.png',50,100,10,30,120)
#walls
wall1 = Wall(153, 135, 163, 750, 0, 50, 250)
wall2 = Wall(153, 135, 163, 350, 0, 50, 250)
wall3 = Wall(153,135,163, 350, 250, 450, 50)

walls = []
walls.append(wall1)
walls.append(wall2)
walls.append(wall3)

#прапорці, що відповідають за стан гри
game = True
clock = time.Clock()


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        elif e.type == KEYDOWN:
            if e.key == K_e:
                spaceship1.fire()
        elif e.type == KEYDOWN:
            if e.key == K_m:
                spaceship2.fire2()
        

    
    #player1.reset()
    window.blit(back,(0,0))
    bullets.update()
    bullets.draw(window)
    spaceship1.update_l()
    spaceship2.update_r()
    spaceship1.reset()
    spaceship2.reset()
    monster1.reset() 
    monster2.reset()
    monster3.reset()
    monster4.reset()
    blackhole.reset()
    h1.reset()
    h2.reset()
    h3.reset()
    h4.reset()
    h5.reset()
    m1.reset()
    m2.reset()
    m3.reset()
    m4.reset()
    m5.reset()
    wall1.draw_wall()
    wall2.draw_wall()
    wall3.draw_wall()
   
  
   
    
   
   
   
   
    display.update()
    clock.tick(60)


