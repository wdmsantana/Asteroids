import pygame

class Bullet():
    
    def __init__(self, parent, image, rect, speed, direction):
        self.parent = parent
        self.image = image
        self.rect = rect
        self.speed = speed
        self.direction = direction

    def update(self):
        pass

    def collidewith(self):
        pass