import pygame, time
from player import *
from colours import *


fpsClock = pygame.time.Clock()
pygame.init()
FPS = 60
W = 800
H = 800
PG_Width = 20
Block_Width = 18
window_size = (W, H)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("2Dtyan")
inGame = True

all_sprites = pygame.sprite.Group()
new_rect = Player()
all_sprites.add(new_rect)

r = [0, 0, Block_Width, Block_Width]

matrix = []
for y in range(int(W / PG_Width)):
    arr = []
    for x in range(int(W / PG_Width)):
        arr.append(1)
    matrix.append(arr)

while inGame:
    fpsClock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            inGame = False

    for y in range(int(W / PG_Width)):
        for x in range(int(W / PG_Width)):
            r[0], r[1] = PG_Width * y + 1, PG_Width * x + 1
            pygame.draw.rect(screen, YELLOW, r, 0)

    all_sprites.update()
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
