from pygame import*
from random import randint
from time import time as timer
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_speed, player_x, player_y, player_scale_x, player_scale_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_scale_x, player_scale_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x >=5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < 620:
            self.rect.x += self.speed
    def fire(self):
        bullet = Bullet('pngegg.png',10, self.rect.centerx, self.rect.top, 30, 20)
        bullets.add(bullet)
        

lost = 0



class Enemy(GameSprite):

    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > 500:
            self.rect.y = 0
            self.rect.x = randint(80, 620)
            lost += 1


class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y<0:
            self.kill()
    


finish = False
font.init()
font1 = font.SysFont(None, 80)
font2 = font.SysFont(None, 36)
win = font1.render('лютый', True, (255, 255, 255))
lose = font1.render('распил обеспечен', True, (255, 255, 255))

player = Player('95617217-4cb0-4944-bcbe-11491a4fce4c.jpg', 7, 400, 390, 130,130)
monsters = sprite.Group()
for i in range(1,2):
    monster = Enemy('pngwing.com.png',randint(1, 3), randint(40, 80), -40,70, 70 )
    monster1 = Enemy('pngwing.com.png',randint(1, 2), randint(80, 620), -40,50, 50 )
    monsters.add(monster)
    monsters.add(monster1)

asteroids = sprite.Group()
for i in range (1,3):
    asteroid = Enemy('pngegg2.png',randint(1, 2), randint(80, 620), -40,50, 50 )
    asteroids.add(asteroid)
mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()
fire_sound = mixer.Sound("fire.ogg")

window = display.set_mode((700, 500))
backround = transform.scale(image.load("qwerty.jpg"), (700, 500))
monster1 = sprite.Group()



speed = 10
clock = time.Clock()
FPS = 60
score = 1
goal = 100
bullets = sprite.Group()
max_lost = 200
game = True
live = 3
rel_time = False
num_fire=0
while game:

    for e in event.get():
        if e. type == QUIT:
            game = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                if num_fire <13 and rel_time== False:
                    num_fire+=1
                    player.fire()
                    fire_sound.play()
                if num_fire>=13 and rel_time==False:
                    last_time = timer()
                    rel_time=True

    
    if not finish:
        window.blit(backround, (0,0))


        player.update()
        player.reset()
        monsters.update()
        monsters.draw(window)
        bullets.update()
        bullets.draw(window)
        asteroids.update()
        asteroids.draw(window)
        
        if rel_time ==True:
            now_time = timer()
            if now_time - last_time<3:
                reload = font2.render('троит что-то...', 1, (250, 0,0))
                window.blit(reload, (400, 50))
            else:
                num_fire= 0
                rel_time = False

        Collides_list = sprite.groupcollide(monsters, bullets,True ,True)
        for c in Collides_list:
            score +=1
            monster = Enemy('pngwing.com.png',randint(1, 2), randint(80, 620), -40,100, 80 )
            monsters.add(monster)
        if sprite.spritecollide(player, monsters, False) or sprite.spritecollide (player, asteroids, False):
            live -=1
            sprite.spritecollide(player, monsters, True)
            sprite.spritecollide (player, asteroids, True) 


        if sprite.spritecollide(player,monsters, False) or lost >= max_lost or live == 0:
            finish = True
            
            window.blit(lose, (300, 270))
        text = font2.render('размотанно '+str(score),1, (255,255,255))
        window.blit(text, (10, 20))
        text_lost = font2.render('позади ' +str(lost), 1, (255, 255, 255))
        window.blit(text_lost, (10,50))
        if live == 3:
            live_color = (0,140, 0)
        if live == 2:
            live_color = (150,150,0)
        if live == 1:
            live_color = (150,0,0)
        text_live = font1.render(str(live), 1, live_color)
        window.blit(text_live, (650, 10))

    else:
        finish = False
        for b in bullets:
            b.kill()
        for m in monsters:
            m.kill()
        time.delay(3000)
        for i in range (1, 5):
            monster = Enemy('pngwing.com.png',randint(1, 2), randint(80, 620), -40,100, 80 )
            monsters.add(monster)
        for i in range (1,3):
            asteroid = Enemy('pngegg2.png',randint(1, 2), randint(80, 620), -40,50, 50 )
            asteroids.add(asteroid)


        display.update()
        clock.tick(FPS)
    display.update()
    clock.tick(FPS)