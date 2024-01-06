import pygame
from spaceship import Spaceship
from asteroid import Asteroid


class Game:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.spaceship_group = pygame.sprite.GroupSingle()
        self.spaceship_group.add(Spaceship(self.screen_width, self.screen_height))
        self.asteroids_group = pygame.sprite.Group()
        self.asteroids_group.add(Asteroid(self.screen_width, self.screen_height))
        self.lives = 3
        self.run = True
        self.score = 0

    def check_for_collisions(self):
        if self.spaceship_group:
            for bullet_sprite in self.spaceship_group.sprite.bullets_group:
                if pygame.sprite.spritecollide(bullet_sprite, self.asteroids_group, True):
                    bullet_sprite.kill()
                    self.score += 1
        if self.asteroids_group:
            for asteroids_sprite in self.asteroids_group:
                if pygame.sprite.spritecollide(asteroids_sprite, self.spaceship_group, False):
                    asteroids_sprite.kill()
                    self.lives -= 1
                    if self.lives == 0:
                        self.game_over()
                        self.score = 0
        if self.asteroids_group:
            for asteroid in self.asteroids_group:
                if pygame.sprite.spritecollide(asteroid, self.spaceship_group, False):
                    self.game_over()
                    self.score = 0

    def game_over(self):
        self.run = False

    def reset(self):
        self.run = True
        self.lives = 3
        self.spaceship_group.sprite.reset()
        self.asteroids_group.empty()