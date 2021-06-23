import pygame


class Bullet:
    def __init__(self, parent, x, y, dx, dy, image, rect, speed, direction):
        self.parent = parent
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.image = image
        self.rect = rect
        self.speed = speed
        self.dx = dx
        self.dy = dy

    def draw(self):
        pass

    def update(self):
        pass

    def collides_with(self, target):
        pass
