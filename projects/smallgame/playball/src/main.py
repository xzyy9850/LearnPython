import pygame
import sys
import const
from pygame.locals import QUIT
from game import Game

pygame.init()
DISPLAYSURF = pygame.display.set_mode(const.GAME_SIZE)
game = Game(DISPLAYSURF)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    game.update()
    DISPLAYSURF.fill((255, 255, 255))
    game.draw()
    pygame.display.update()
