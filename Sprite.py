# encoding : utf-8
# antuor : comi
from setting import *
from pygame import *
import pygame,sys,time


vec = pygame.math.Vector2

class Player(pygame.sprite.Sprite):
    Bullet_groups = pygame.sprite.Group()
    flag = 1
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(r'img\down.png').convert()
        self.image.set_colorkey(white)
        self.rect = self.image.get_rect()
        self.rect.midbottom = (115, 130)

        self.pos = vec(115, 130)

        self.last_time = time.time()

    def update(self):
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_a]:
            self.image = pygame.image.load(r'img\left.png').convert()
            self.image.set_colorkey(white)
            self.pos.x -= move_space
            self.flag = 2
        if key_pressed[pygame.K_d]:
            self.image = pygame.image.load(r'img\right.png').convert()
            self.image.set_colorkey(white)
            self.pos.x += move_space
            self.flag = 1
        if key_pressed[pygame.K_w]:
            self.image = pygame.image.load(r'img\up.png').convert()
            self.image.set_colorkey(white)
            self.pos.y -= move_space
            self.flag = 3
        if key_pressed[pygame.K_s]:
            self.image = pygame.image.load(r'img\down.png').convert()
            self.image.set_colorkey(white)
            self.pos.y += move_space
            self.flag = 4
        if key_pressed[pygame.K_SPACE]:
            self.shoot()
        self.rect.midbottom = self.pos

    def shoot(self):
        self.now = time.time()
        if self.now - self.last_time > 0.8:
            pygame.mixer.music.load(r'sounds\expl.wav')
            pygame.mixer.music.play()
            bullet = Bullet(self.pos.x, self.pos.y)
            self.Bullet_groups.add(bullet)
            self.last_time = self.now


class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((w, h))
        self.image.fill(yellow)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Enemy(pygame.sprite.Sprite):
    Bullet_groups = pygame.sprite.Group()
    flag = 1

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(r'img\down.png').convert()
        self.image.set_colorkey(white)
        self.rect = self.image.get_rect()
        self.rect.midbottom = (315, 130)
        self.pos = vec(315, 130)
        self.bar = 100
        self.last_time = time.time()
        self.flag = 1

    def update(self):
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_LEFT]:
            self.image = pygame.image.load(r'img\left.png').convert()
            self.image.set_colorkey(white)
            self.pos.x -= move_space
            self.flag = 2
        if key_pressed[pygame.K_RIGHT]:
            self.image = pygame.image.load(r'img\right.png').convert()
            self.image.set_colorkey(white)
            self.pos.x += move_space
            self.flag = 1
        if key_pressed[pygame.K_UP]:
            self.image = pygame.image.load(r'img\up.png').convert()
            self.image.set_colorkey(white)
            self.pos.y -= move_space
            self.flag = 3
        if key_pressed[pygame.K_DOWN]:
            self.image = pygame.image.load(r'img\down.png').convert()
            self.image.set_colorkey(white)
            self.pos.y += move_space
            self.flag = 4
        if key_pressed[pygame.K_p]:
            self.shoot()

        self.rect.midbottom = self.pos

    def shoot(self):

        self.now = time.time()
        if self.now - self.last_time > 0.8:
            pygame.mixer.music.load(r'sounds\expl.wav')
            pygame.mixer.music.play()
            bullet = Bullet(self.pos.x, self.pos.y)
            self.Bullet_groups.add(bullet)
            self.Bullet_groups.update(self.flag)
            self.last_time = self.now


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(r'img\dot.png ').convert()
        self.image.set_colorkey(white)
        self.rect = self.image.get_rect()
        self.rect.centerx = x + 10
        self.rect.bottom = y - 12
        self.speed = 5

    def update(self,flag):
        if flag == 1:   # right
            self.rect.x += self.speed
        if flag == 2:   # left
            self.rect.x -= self.speed
        if flag == 3:   #up
            self.rect.y -= self.speed
        if flag == 4:   # down
            self.rect.y += self.speed
