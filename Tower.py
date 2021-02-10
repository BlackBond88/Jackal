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
        self.center_y = self.y + self.heigth / 2

    def draw(self):
        self.color = BLACK
        rect = pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.heigth))
        screen.blit(picture, rect)

    def is_alive(self):
        if self.health > 0:
            return self.health > 0
        else:
            return self.health < 0


class Tower(GameObject):
    def move(self, x, y):
        self.x += x
        self.y += y
        self.center_x = self.x + self.width / 2
        self.center_y = self.y + self.heigth / 2

class Target(GameObject):
    def move(self, tower_x, tower_y):
        if tower_y - self.y != 0:
            tg = (tower_x - self.x) / (tower_y - self.y)
            cos = 1 / (1 + tg ** 2) ** (1 / 2)
            sin = tg / (1 + tg ** 2) ** (1 / 2)
            x = sin
            y = cos
        else:
            y = 0
            if tower_x - self.x > 0:
                x = 1
            else:
                x = -1
        if abs(tower_x - self.x) < 20 and abs(tower_y - self.y) < 20:
            self.health = 0
        elif tower_y - self.y >= 0:
            self.x += x
            self.y += y
        elif tower_y - self.y < 0:
            self.x -= x
            self.y -= y



def generate_random_target(width, heigth, color, quantity):
    targets = []
    for i in range(quantity):
        x = random.randint(0, SCREEN_WIDTH - width)
        y = random.randint(0, SCREEN_HEIGTH - heigth)
        target = Target(x, y, width, heigth, 10, color)
        targets.append(target)
    return targets


def game_main():
    zombies = generate_random_target(10, 10, RED, 1000)
    my_tower = Tower(350, 250, 50, 50, 1000, WHITE)

    finished = False
    clock = pygame.time.Clock()


    while not finished:
        clock.tick(FPS)

        my_tower.draw()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    my_tower.move(-25, 0)
                if event.key == pygame.K_RIGHT:
                    my_tower.move(25, 0)
                if event.key == pygame.K_DOWN:
                    my_tower.move(0, 25)
                if event.key == pygame.K_UP:
                    my_tower.move(0, -25)

        pygame.display.update()
        screen.fill(BLACK)


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
    picture = pygame.image.load("zom.gif")
    picture = pygame.transform.scale(picture, (20, 20))


    pygame.display.set_caption("MyGame")
    pygame.display.update()

    game_main()
