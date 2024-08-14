from typing import Any
import pygame
from pygame.locals import *
import random
import time

import classes.playerClass
import classes.enemyClass

from classes.playerClass import Player
from classes.enemyClass import Enemy

pygame.init()
clock = pygame.time.Clock()

WIDTH = 1000
HEIGHT = 600

gravity = 0 

screen = pygame.display.set_mode((WIDTH,HEIGHT))

hero = Player()


add_enemy = pygame.USEREVENT+1
pygame.time.set_timer(add_enemy,1200) #triggers every x milliseconds

all_sprites = pygame.sprite.Group()
all_enemies = pygame.sprite.Group()
all_sprites.add(hero)

running = True
while running:

    

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running == False



        if event.type == add_enemy:
            height = random.randint(100,400)
            enemy2 = Enemy((WIDTH+100,height+350),5)

            
            all_sprites.add(enemy2)
            all_enemies.add(enemy2)
        

        if hero.rect.top < 0:
            hero.rect.top = HEIGHT  

        if hero.rect.bottom > HEIGHT:
            hero.rect.top = 0

            
    keys = pygame.key.get_pressed()
    for sprite in all_sprites:
        sprite.update(keys)

    screen.fill("white")

    for sprite in all_sprites:
        screen.blit(sprite.surface,sprite.rect)

    if pygame.sprite.spritecollideany(hero,all_enemies):
        if pygame.sprite.spritecollide(hero,all_enemies,False,pygame.sprite.collide_mask):
            running = False
            


    pygame.display.update()
    clock.tick(60)

pygame.quit()
