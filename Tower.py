import pygame
from my_colors import *


SCREEN_WIDTH, SCREEN_HEIGTH = 800, 600
FPS = 60


class Target:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 50
        self.heigth = 50

    def move(self):
        self.x += 1
        self.y += 1

    def draw(self):
        pygame.draw.rect(screen, (RED), (self.x, self.y, self.width, self.heigth))


def game_main():

    zombie = Target(10, 10)

    finished = False
    clock = pygame.time.Clock()

    while not finished:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True

        pygame.display.update()
        screen.fill(BLACK)

        zombie.move()
        zombie.draw()

    pygame.quit()

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGTH))
    pygame.display.set_caption("MyGame")
    pygame.display.update()

    game_main()
