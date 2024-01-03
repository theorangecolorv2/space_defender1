import sys
from spaceship import Spaceship
from bullet import Bullet
import pygame

pygame.init()

screen_width = 750
screen_height = 700

GREY = (29, 29, 27)

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Space Adventure')

clock = pygame.time.Clock()

spaceship = Spaceship(screen_width, screen_height)
spaceship_group = pygame.sprite.GroupSingle()
spaceship_group.add(spaceship)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    spaceship_group.update()

    screen.fill(GREY)
    spaceship_group.draw(screen)
    spaceship_group.sprite.bullets_group.draw(screen)

    pygame.display.update()
    clock.tick(60)
