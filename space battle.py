from pygame import *

'''Необхідні класи'''
font.init() 
init()

counter, text0 = 4, '3'.rjust(3)
time.set_timer(USEREVENT, 1000)




#text
font1 = font.SysFont('Italic',30)
font2 = font.SysFont('ComicSans', 100)
score1 =  0
score2 =  0 
s = 'Score  ' + str(score1)+' : ' + str(score2)
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
win = image.load('win1.png')
winn2 = image.load('win2.png')
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
mars = GameSprite('mars.png', 850, 100, 0, 100, 100)
earth =  GameSprite('earth.png', 200, 100, 0, 100, 100)
blackhole = GameSprite('black hole.jpg', 400, 0, 0, 350, 300)
spawnpoint = GameSprite('checkpoint.png',475, 350, 0, 200,200)

display.set_caption('space battle') 
#player1 = GameSprite('racket.png',50,100,10,30,120)
#walls
wall1 = Wall(4, 39, 51, 750, 0, 50, 250)
wall2 = Wall(4, 39, 51, 350, 0, 50, 250)
wall3 = Wall(4, 39, 51, 350, 250, 450, 50)
wall4 = Wall(145, 113, 65, 275, 500, 100,100)
wall5 = Wall(145, 113, 65, 775, 500, 100,100 )
walls = []
walls.append(wall1)
walls.append(wall2)
walls.append(wall3)

#прапорці, що відповідають за стан гри
game = True
clock = time.Clock()
see = False

while game:
    for e in event.get():
        if e.type == USEREVENT: 
            counter -= 1
            text0 = str(counter).rjust(3) if counter > 0 else ' '
        if e.type == QUIT:
            game = False
        elif e.type == KEYDOWN:
            if e.key == K_e:
                spaceship1.fire()
            if e.key == K_m:
                spaceship2.fire2()
        

    
    #player1.reset()
    window.blit(back,(0,0))
    bullets.update()
    bullets2.update()
    bullets2.draw(window)
    bullets.draw(window)
    spaceship1.update_l()
    spaceship2.update_r()
    spawnpoint.reset()
    spaceship1.reset()
    spaceship2.reset()
    monster1.reset() 
    monster2.reset()
    monster3.reset()
    monster4.reset()
    blackhole.reset()
    h1.reset()
    mars.reset()
    earth.reset()
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
    wall4.draw_wall()
    wall5.draw_wall()
   
    
    if sprite.spritecollide(spaceship2,bullets,True):
        spaceship2.rect.x = 475
        spaceship2.rect.y = 350
    if sprite.spritecollide(spaceship1,bullets2,True):
        spaceship1.rect.x = 475
        spaceship1.rect.y = 350
    if sprite.collide_rect(spaceship2,mars) or sprite.collide_rect(spaceship1,earth):
        wall3.rect.x = 435454
        counter = 4
        see = True
    if sprite.collide_rect(spaceship1,mars):
        spaceship1.rect.x = 475
        spaceship1.rect.y = 350
    if sprite.collide_rect(spaceship2,earth): 
        spaceship2.rect.x = 475
        spaceship2.rect.y = 350

    if sprite.collide_rect(spaceship2,h1): 
        h1.rect.x= spaceship2.rect.x
        h1.rect.y = spaceship2.rect.y
    elif sprite.collide_rect(spaceship2,h2): 
        h2.rect.x= spaceship2.rect.x
        h2.rect.y = spaceship2.rect.y
    elif sprite.collide_rect(spaceship2,h3): 
        h3.rect.x= spaceship2.rect.x
        h3.rect.y = spaceship2.rect.y
    elif sprite.collide_rect(spaceship2,h4): 
        h4.rect.x= spaceship2.rect.x
        h4.rect.y = spaceship2.rect.y
    elif sprite.collide_rect(spaceship2,h5): 
        h5.rect.x= spaceship2.rect.x
        h5.rect.y = spaceship2.rect.y
    if sprite.collide_rect(spaceship1,m1):
        m1.rect.x = spaceship1.rect.x
        m1.rect.y = spaceship1.rect.y
    elif sprite.collide_rect(spaceship1,m2):
        m2.rect.x = spaceship1.rect.x
        m2.rect.y = spaceship1.rect.y
    elif sprite.collide_rect(spaceship1,m3):
        m3.rect.x = spaceship1.rect.x
        m3.rect.y = spaceship1.rect.y
    elif sprite.collide_rect(spaceship1,m4):
        m4.rect.x = spaceship1.rect.x
        m4.rect.y = spaceship1.rect.y
    elif sprite.collide_rect(spaceship1,m5):
        m5.rect.x = spaceship1.rect.x
        m5.rect.y = spaceship1.rect.y

    
    

    for b in bullets:
        if sprite.collide_rect(b,wall4):
            b.kill()
        elif sprite.collide_rect(b,wall5):
            b.kill()
    for b in bullets:
        if sprite.collide_rect(b,wall1):
            b.kill()
        elif sprite.collide_rect(b,wall2):
            b.kill()
        elif sprite.collide_rect(b,wall3):
            b.kill()
    
        
    for n in bullets2:
        if sprite.collide_rect(n,wall5):
            n.kill()
        elif sprite.collide_rect(n,wall4):
            n.kill()
    for n in bullets2:
        if sprite.collide_rect(n,wall1):
            n.kill()
        elif sprite.collide_rect(n,wall2):
            n.kill()
        elif sprite.collide_rect(n,wall3):
            n.kill()
       
        


    if sprite.collide_rect(spaceship1,wall4):
        spaceship1.rect.right = wall4.rect.left
    if sprite.collide_rect(spaceship2,wall5):
        spaceship2.rect.left = wall5.rect.right
    
    if sprite.collide_rect(blackhole, h1):
        h1.rect.x = 378945
        h1.rect.y = 47832
        score2 += 1
        s = 'Score  ' + str(score1)+' : ' + str(score2)
    if sprite.collide_rect(blackhole, h2):
        h2.rect.x = 378945
        h2.rect.y = 47832
        score2 += 1
        s = 'Score  ' + str(score1)+' : ' + str(score2)
    if sprite.collide_rect(blackhole, h3):
        h3.rect.x = 378945
        h3.rect.y = 47832
        score2 += 1
        s = 'Score  ' + str(score1)+' : ' + str(score2)
    if sprite.collide_rect(blackhole, h4):
        h4.rect.x = 378945
        h4.rect.y = 47832
        score2 += 1
        s = 'Score  ' + str(score1)+' : ' + str(score2)
    if sprite.collide_rect(blackhole, h5):
        h5.rect.x = 378945
        h5.rect.y = 47832
        score2 += 1
        s = 'Score  ' + str(score1)+' : ' + str(score2)
    if sprite.collide_rect(blackhole, m1):
        m1.rect.x = 378945
        m1.rect.y = 47832
        score1 += 1
        s = 'Score  ' + str(score1)+' : ' + str(score2)
    if sprite.collide_rect(blackhole, m2):
        m2.rect.x = 378945
        m2.rect.y = 47832
        score1 += 1
        s = 'Score  ' + str(score1)+' : ' + str(score2)
    if sprite.collide_rect(blackhole, m3):
        m3.rect.x = 378945
        m3.rect.y = 47832
        score1 += 1
        s = 'Score  ' + str(score1)+' : ' + str(score2)
    if sprite.collide_rect(blackhole, m4):
        m4.rect.x = 378945
        m4.rect.y = 47832
        score1 += 1
        s = 'Score  ' + str(score1)+' : ' + str(score2)
    if sprite.collide_rect(blackhole, m5):
        m5.rect.x = 378945
        m5.rect.y = 47832
        score1 += 1
        s = 'Score  ' + str(score1)+' : ' + str(score2)

     
    if score1 == 5:
        spaceship2.rect.x = 378942
        spaceship2.rect.y = 389722
        window.blit(text2,(300,300))
        
    if score2 == 5:
        spaceship1.rect.x = 378942
        spaceship1.rect.y = 389722
        window.blit(text3,(300,300))
        
        
       
          


    text = font1.render(s,True,(255,255,255))
    text2 = font2.render('player1 won',True,(255,255,255))
    text3 = font2.render('player2 won', True,(255,255,255))
    window.blit(text,(100,100))
    
    
    if counter == 0:
        see = False
        wall3.rect.x = 350
        wall3.rect.y = 250
    if see:
        window.blit(font1.render(text0, True, (255,255,255)), (550,250))
    
    
    
    
  
    
   
    display.update()
    clock.tick(60)


