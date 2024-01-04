import sys
import pygame
import random
from game import Game

pygame.init()

screen_width = 750
screen_height = 700

image_fons = pygame.image.load('graphics/fons.png')


screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Space Adventure')

clock = pygame.time.Clock()

game = Game(screen_width, screen_height)


class Asteroid(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('graphics/asteroids.png')
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, screen_width - self.rect.width)
        self.rect.y = -self.rect.height
        self.speed = random.randint(2, 5)

    def update(self):
        self.rect.y += self.speed


asteroids_group = pygame.sprite.Group()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if random.randint(1, 100) == 1:
        new_asteroid = Asteroid()
        asteroids_group.add(new_asteroid)

    game.spaceship_group.update()
    asteroids_group.update()

    screen.blit(image_fons, (0, 0))
    game.spaceship_group.draw(screen)
    game.spaceship_group.sprite.bullets_group.draw(screen)
    asteroids_group.draw(screen)

    pygame.display.update()
    clock.tick(60)