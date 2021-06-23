import pygame

from asteroid import Asteroid
from ufo import UFO
from player import Player


class Screen:
    def __init__(self, width, height, asteroids, ufo, player):
        self.width = width
        self.height = height
        self.asteroids = []
        self.ufo = UFO()
        self.player = Player()

    def draw_hud(self):
        pass

    def draw_elements(self):
        pass
