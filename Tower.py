import pygame
from my_colors import *

SCREEN_WIDTH, SCREEN_HEIGTH = 800, 600
FPS = 60


class GameObject:
    def __init__(self, x, y, width, heigth, color):
        self.x = x
        self.y = y
        self.width = width
        self.heigth = heigth
        self.color = color
        self.center_x = self.x + self.width / 2
        self.center_y = self.x + self.width / 2

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.heigth))


class Tower(GameObject):
    pass


class Target(GameObject):
    def move(self, tower_x, tower_y):
        k = (self.y - tower_y) / (self.x - tower_x)
        b = tower_x - k * tower_y
        self.x += 1
        self.y = k * self.x + b


def game_main():
    zombie = Target(10, 10, 10, 10, RED)
    my_tower = Tower(350, 350, 50, 50, WHITE)

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
        zombie.move(my_tower.center_x, my_tower.center_y)
        zombie.draw()

    pygame.quit()


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGTH))
    pygame.display.set_caption("MyGame")
    pygame.display.update()

    game_main()
