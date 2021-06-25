import pygame
import random

from pygame.constants import *


LARGE_ASTEROID = 20
NORMAL_ASTEROID = 12
LITTLE_ASTEROID = 8


class Asteroid:
    def __init__(self, surface, position, color, size, dx, dy, speed):
        self.surface = surface
        self.position = list(position)
        self.color = color
        self.size = size
        self.dx = dx
        self.dy = dy
        self.speed = speed

    def draw_asteroid(self):
        pygame.draw.circle(self.surface, self.color, self.position, self.size)

    def move_asteroid(self):
        if self.dx == 'RIGHT':
            self.position[0] += self.speed
        if self.dx == 'LEFT':
            self.position[0] -= self.speed

        if self.dy == 'UP':
            self.position[1] -= self.speed
        if self.dy == 'DOWN':
            self.position[1] += self.speed

        # Asteroid crossing movements through screen
        if self.position[0] > 800:  # Crossing horizontally
            self.position[0] = 0
        if self.position[0] < 0:
            self.position[0] = 800

        if self.position[1] > 600:  # Crossing vertically
            self.position[1] = 0
        if self.position[1] < 0:
            self.position[1] = 600

    def split_asteroid(self):
        if self.size == LARGE_ASTEROID:
            size = NORMAL_ASTEROID
        elif self.size == NORMAL_ASTEROID:
            size = LITTLE_ASTEROID
        elif self.size == LITTLE_ASTEROID:
            return None

        dxs, dys = ['LEFT', 'RIGHT'], ['UP', 'DOWN']
        random.shuffle(dxs)
        random.shuffle(dys)

        return [Asteroid(self.surface, self.position, self.color, size,
                dxs[0], dys[0], self.speed),
                Asteroid(self.surface, self.position, self.color, size,
                dxs[1], dys[1], self.speed)]


# --TESTING CLASS-- #
if __name__ == '__main__':
    pygame.init()

    screen = pygame.display.set_mode((800, 600))
    screen.fill((0, 0, 0))

    init_dx = ['RIGHT', 'LEFT']
    init_dy = ['UP', 'DOWN']
    position = (400, 300)
    asteroid = Asteroid(screen, position, (255, 0, 0), LARGE_ASTEROID,
                        random.choice(init_dx), random.choice(init_dy), 0.25)
    asteroids = [asteroid]

    running = True
    while running:

        for a in asteroids:
            a.move_asteroid()
            a.draw_asteroid()

        pygame.display.flip()
        pygame.time.Clock().tick(10)

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                    pygame.quit()
                if event.key == K_1:
                    asteroid.size = LITTLE_ASTEROID
                if event.key == K_2:
                    asteroid.size = NORMAL_ASTEROID
                if event.key == K_3:
                    asteroid.size = LARGE_ASTEROID

                # Change direction just for mechanics testing
                if event.key == K_RIGHT:
                    asteroid.dx = 'RIGHT'
                if event.key == K_LEFT:
                    asteroid.dx = 'LEFT'
                if event.key == K_UP:
                    asteroid.dy = 'UP'
                if event.key == K_DOWN:
                    asteroid.dy = 'DOWN'

                # Change asteroid speed for mechanics testing
                if event.key == K_BACKSPACE:
                    asteroid.speed = 0.125
                if event.key == K_SPACE:
                    asteroid.speed = 0.5

                # Split the asteroid
                if event.key == K_s:
                    newbies = []

                    for a in asteroids:
                        if (res := a.split_asteroid()):
                            newbies += res

                    asteroids = list(newbies)

        screen.fill((0, 0, 0))
