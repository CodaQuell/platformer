import pygame
from pygame import *

class Enemy(pygame.sprite.Sprite,):
    def __init__(self,centre,speed):
        super(Enemy,self).__init__()
        self.surface = pygame.Surface((100,100))
        #self.surface = pygame.image.load("picture")
        #self.surface = pygame.transform.scale(self.surface,(100,50))
        self.rect = self.surface.get_rect()
        self.surface.fill ("red")
        #self.mask = pygame.mask.from_surface(self.surface)
        self.rect.center = centre
        self.speed = speed 

    def update(self, keys_pressed):
        self.rect.x -= self.speed
        
        if self.rect.right < 0:
            self.kill()