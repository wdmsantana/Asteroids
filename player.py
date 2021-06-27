import pygame
from bullet import Bullet
from pygame.constants import KEYDOWN, K_1, K_2, K_3, K_BACKSPACE, K_DOWN, K_ESCAPE, K_LEFT, K_RIGHT, K_SPACE, K_UP


class Player:

    def __init__(self, surface, vertices, name, points, lives):
        self.surface = surface
        self.vertices = vertices
        self.name = name
        self.points = points
        self.lives = lives

    def draw(self):
        pygame.draw.polygon(self.surface, (255, 255, 255), self.vertices)
        pygame.display.update()

    def move(self, key):
        if key == K_RIGHT:
            self.vertices[0][0] += 10
            self.vertices[1][0] += 10
            self.vertices[2][0] += 10
        if key == K_LEFT:
            self.vertices[0][0] -= 10
            self.vertices[1][0] -= 10
            self.vertices[2][0] -= 10

    def shoot(self):
        pass




from pygame.math import Vector2
from pygame.transform import rotozoom
from pygame.image import load


def load_sprite(name, with_alpha=True):

    path = f"assets/sprites/{name}.png"
    loaded_sprite = load(path)
    if with_alpha:
        return loaded_sprite.convert_alpha()
    else:
        return loaded_sprite.convert()


def wrap_position(position, surface):
    x, y = position
    w, h = surface.get_size()
    return Vector2(x % w, y % h)

UP = Vector2(0, -1)

class GameObject:
    def __init__(self, position, sprite, velocity):
        self.position = Vector2(position)
        self.sprite = sprite
        self.radius = sprite.get_width() / 2
        self.velocity = Vector2(velocity)

    def draw(self, surface):
        blit_positon = self.position - Vector2(self.radius)
        surface.blit(self.sprite, blit_positon)

    def move(self, surface):
        self.position = wrap_position(self.position + self.velocity, surface)

    def collides_with(self, other_obj):
        distance = self.position.distance_to(other_obj.position)
        return distance < self.radius + other_obj.radius


class Spaceship(GameObject):
    MANEUVERABILITY = 3
    ACCELARATION = 0.25

    def __init__(self, position):
        # Make a copy of the original UP vector
        self.direction = Vector2(UP)

        super().__init__(position, load_sprite("spaceship"), Vector2(0))

    def rotate(self, clockwise=True):
        sign = 1 if clockwise else -1
        angle = self.MANEUVERABILITY * sign
        self.direction.rotate_ip(angle)

    def draw(self, surface):
        angle = self.direction.angle_to(UP)
        rotated_surface = rotozoom(self.sprite, angle, 1.0)
        rotated_surface_size = Vector2(rotated_surface.get_size())
        blit_position = self.position - rotated_surface_size * 0.5
        surface.blit(rotated_surface, blit_position)

    def accelerate(self):
        self.velocity += self.direction * self.ACCELARATION


