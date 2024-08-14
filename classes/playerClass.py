import pygame
from pygame import *


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player,self).__init__()
        self.surface = pygame.Surface((20,20))
        #self.surface = pygame.image.load("picture")
        #self.surface = pygame.transform.scale(self.surface,(100,50))
        self.rect = self.surface.get_rect()
        self.surface.fill ("black")
        self.rect.center = [300,300]
        self.mask = pygame.mask.from_surface(self.surface)
        self.speed = 0

    def update(self, keys_pressed):
        if keys_pressed[K_SPACE]:
            self.speed  = -3 
        self.speed = self.speed+0.1

        self.rect.y += self.speed

    