import pygame, time
from player import *
from colours import *
from characteristics import *
from enemy import *

fpsClock = pygame.time.Clock()
pygame.init()
window_size = (W, H)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("2Dtyan")
inGame = True

all_sprites = pygame.sprite.Group()

player_sprite = Player()
enemy_sprite = Enemy("assault_troop", 100, 100)
enemy_sprite1 = Enemy("assault_troop", 700, 700)

all_sprites.add(player_sprite)
all_sprites.add(enemy_sprite)
all_sprites.add(enemy_sprite1)

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

    screen.fill(SLIGHT_YELLOW)

    for y in range(int(W / PG_Width)):
        for x in range(int(W / PG_Width)):
            pygame.draw.rect(screen, YELLOW, (PG_Width * y + 1, PG_Width * x + 1, Block_Width, Block_Width), 0)

    all_sprites.update()
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
