import pygame


class Bullet:

    def __init__(self, parent, image, rect, speed, dx, dy):
        self.parent = parent
        self.image = image
        self.rect = rect
        self.speed = speed
        self.dx = dx
        self.dy = dy

    def update(self):
        pass

    def collidewith(self):
        pass
