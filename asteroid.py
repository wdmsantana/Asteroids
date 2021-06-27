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
