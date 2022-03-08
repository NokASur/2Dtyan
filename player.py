import pygame
from colours import *
from main import *


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.w, self.h = 18, 18
        self.image = pygame.Surface((self.w, self.h))
        self.color = GREEN
        self.image.fill(self.color)
        self.speed = 1
        self.rect = self.image.get_rect()
        self.rect.centerx = W/2
        self.rect.centery = H/2

    def update(self):
        if pygame.key.get_pressed()[pygame.K_UP]:
            self.rect.centery -= self.speed
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            self.rect.centery += self.speed
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            self.rect.centerx -= self.speed
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            self.rect.centerx += self.speed
        if self.rect.centery < 0:
            self.rect.centery = 0
        if self.rect.centery > H:
            self.rect.centery = H
        if self.rect.centerx < 0:
            self.rect.centerx = 0
        if self.rect.centerx > W:
            self.rect.centerx = W
