import pygame
import random
from my_colors import *

SCREEN_WIDTH, SCREEN_HEIGTH = 800, 600
FPS = 60


class GameObject:
    def __init__(self, x, y, width, heigth, health, color):
        self.x = x
        self.y = y
        self.width = width
        self.heigth = heigth
        self.health = health
        self.color = color
        self.center_x = self.x + self.width / 2
        self.center_y = self.x + self.width / 2

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.heigth))

    def is_alive(self):
        if self.health > 0:
            return self.health > 0
        else:
            return self.health < 0


class Tower(GameObject):
    pass


class Target(GameObject):
    def move(self, tower_x, tower_y):
        k = self.x - tower_x
        if k < 0:
            k = (self.y - tower_y) / k
            b = tower_x - k * tower_y
            self.x += 1
            self.y = k * self.x + b
        elif k > 0:
            k = (self.y - tower_y) / k
            b = tower_x - k * tower_y
            self.x -= 1
            self.y = k * self.x + b
        else:
            self.health = 0


def generate_random_target(width, heigth, color, quantity):
    targets = []
    for i in range(quantity):
        x = random.randint(0, SCREEN_WIDTH - width)
        y = random.randint(0, SCREEN_HEIGTH - heigth)
        target = Target(x, y, width, heigth, 10, color)
        targets.append(target)
    return targets


def game_main():
    zombies = generate_random_target(10, 10, RED, 10)
    my_tower = Tower(350, 350, 50, 50, 1000, WHITE)

    finished = False
    clock = pygame.time.Clock()

    while not finished:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True

        pygame.display.update()
        screen.fill(BLACK)

        my_tower.draw()
        for zombie in zombies:
            zombie.move(my_tower.center_x, my_tower.center_y)
            zombie.draw()
            if not zombie.is_alive():
                zombies.remove(zombie)
        if not zombies:
            finished = True
    pygame.quit()


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGTH))
    pygame.display.set_caption("MyGame")
    pygame.display.update()

    game_main()
