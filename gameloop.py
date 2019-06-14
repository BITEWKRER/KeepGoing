# encoding : utf-8
# author : comi
from setting import *
from pygame import *
from Sprite import *
import pygame,sys
from random import *
vec = pygame.math.Vector2


class game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Keep-Going")
        self.screen = pygame.display.set_mode((width, height))
        self.FpsClock = pygame.time.Clock()
        self.playing = True
        self.running = True
        self.Waiting = True
        self.Pblood = 100
        self.Eblood = 100
        self.player = Player()
        self.enemy = Enemy()
        self.all_groups = pygame.sprite.Group()
        self.player_groups = pygame.sprite.Group()
        self.Map_groups = pygame.sprite.Group()
        self.Enemy_groups = pygame.sprite.Group()

    def new(self):
        self.player_groups.add(self.player)
        self.all_groups.add(self.player)

        self.Enemy_groups.add(self.enemy)
        self.all_groups.add(self.enemy)

        for platfroms in Map1:
            p = Platform(*platfroms)     # 取出所有值
            self.Map_groups.add(p)
            self.all_groups.add(p)

        self.run()

    def game_start(self,text):
        self.text_draw(width / 2, height / 4, 64, text)  # 文本
        self.text_draw(width / 2, height * 3 / 4, 25,'Press any key to continue',)  # 文本
        pygame.display.update()
        while self.Waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    self.Waiting = False

    def update(self):
        self.Map_groups.update()
        self.player_groups.update()
        self.enemy.Bullet_groups.update(self.enemy.flag)
        self.player.Bullet_groups.update(self.player.flag)
        self.Enemy_groups.update()

        hit = pygame.sprite.groupcollide(self.player.Bullet_groups, self.Map_groups, True,False)   # 子弹碰墙消失
        hit = pygame.sprite.groupcollide(self.enemy.Bullet_groups, self.Map_groups, True, False)

        PMC = pygame.sprite.spritecollide(self.player,self.Map_groups,False,False)      # 撞墙
        if PMC:
            key_pressed = pygame.key.get_pressed()
            if key_pressed[pygame.K_a]:
                self.player.pos.x = self.player.pos.x + gap
            if key_pressed[pygame.K_d]:
                self.player.pos.x = self.player.pos.x - gap
            if key_pressed[pygame.K_w]:
                self.player.pos.y = self.player.pos.y + gap
            if key_pressed[pygame.K_s]:
                self.player.pos.y = self.player.pos.y - gap

        EMC = pygame.sprite.spritecollide(self.enemy,self.Map_groups,False,False)       # 撞墙
        if EMC:
            key_pressed = pygame.key.get_pressed()
            if key_pressed[pygame.K_LEFT]:
                self.enemy.pos.x = self.enemy.pos.x + gap
            if key_pressed[pygame.K_RIGHT]:
                self.enemy.pos.x = self.enemy.pos.x - gap
            if key_pressed[pygame.K_UP]:
                self.enemy.pos.y = self.enemy.pos.y + gap
            if key_pressed[pygame.K_DOWN]:
                self.enemy.pos.y = self.enemy.pos.y - gap

    def run(self):
        while self.running:
            self.FpsClock.tick(Fps)
            self.events()
            self.draw_pic()
            self.update()

            if self.Eblood <= 0: # enemy
                self.screen.fill(black)
                self.game_start('P1 WIN!')
                time.sleep(1.5)
                self.running = False
                self.playing = False

            if self.Pblood <= 0: # Player
                self.screen.fill(black)
                self.game_start('P2 WIN!')
                time.sleep(1.5)
                self.running = False
                self.playing = False


    def text_draw(self, x, y, size, text):
        self.font = pygame.font.SysFont('arial', size)
        self.text_surf = self.font.render(text, True, red)
        self.text_rect = self.text_surf.get_rect()
        self.text_rect.center = (x, y)
        self.screen.blit(self.text_surf, self.text_rect)

    def draw_pic(self):
        self.screen.fill(white)
        self.text_draw(900,50,30,"KEEP")
        self.text_draw(900, 100, 30, "GOING")

        self.text_draw(820, 150, 20, "P1:")
        self.text_draw(820, 200, 20, "P2:")
        self.text_draw(900, 250, 20, "Attention!")
        self.text_draw(900,300,20,"The Bullet Can")
        self.text_draw(900, 350, 20, "Be Control!")

        self.bar_draw(850, 145, self.Pblood)
        hit = pygame.sprite.groupcollide(self.enemy.Bullet_groups, self.player_groups, True, False)
        if hit:
            self.Pblood = self.Pblood - randint(10, 15)
            self.bar_draw(850, 145, self.Pblood)

        self.bar_draw(850, 195, self.Eblood)
        hit = pygame.sprite.groupcollide(self.player.Bullet_groups, self.Enemy_groups, True, False)
        if hit:
            self.Eblood = self.Eblood - randint(10, 15)
            self.bar_draw(850, 195, self.Eblood)


        self.Map_groups.draw(self.screen)
        self.player_groups.draw(self.screen)
        self.Enemy_groups.draw(self.screen)
        self.player.Bullet_groups.draw(self.screen)
        self.enemy.Bullet_groups.draw(self.screen)

        pygame.display.update()

    def bar_draw(self, x, y, pct):
        #  draw a bar
        if pct <= 0:
            pct = 0
        Bar_Lenth = 100
        Bar_Height = 10
        Fill_Lenth = (pct / 100) * Bar_Lenth
        Out_rect = pygame.Rect(x, y, Bar_Lenth, Bar_Height)
        Fill_rect = pygame.Rect(x, y, Fill_Lenth, Bar_Height)
        pygame.draw.rect(self.screen, green, Fill_rect)
        pygame.draw.rect(self.screen, red, Out_rect, 2)

    def events(self):
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                self.running = False
                self.playing = False






