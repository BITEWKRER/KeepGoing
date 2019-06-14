# encoding : utf-8
# anthor : comi
from gameloop import *
from pygame import *
import pygame,sys,time

if __name__ == '__main__':
    player = game()
    player.game_start('KEEP-GOING')
    while player.playing:
          player.new()
    player.screen.fill(black)
    player.game_start('GAME-OVER')
    time.sleep(1.5)

