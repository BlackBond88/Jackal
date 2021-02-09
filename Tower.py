import pygame
from my_colors import *

SCREEN_WIDTH, SCREEN_HEIGTH = 800, 600
FPS = 60


class Tower():
    def __init__(self, x, y, width, heigth):
        self.x = x
        self.y = y
        self.width = width
        self.heigth = heigth

    def draw(self):
        pygame.draw.rect(screen, WHITE, (self.x, self.y, self.width, self.heigth))


class Target():
    def __init__(self, x, y, width, heigth):
        self.x = x
        self.y = y
        self.width = width
        self.heigth = heigth

    def move(self):
        self.x += 1/5
        self.y += 1/5

    def draw(self):
        pygame.draw.rect(screen, RED, (self.x, self.y, self.width, self.heigth))


#class GameObject:



def game_main():
    #global my_tower
    zombie = Target(10, 10, 10, 10)
    my_tower = Tower(350, 50, 50, 50)

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
        my_tower.draw()

    pygame.quit()


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGTH))
    pygame.display.set_caption("MyGame")
    pygame.display.update()

    game_main()
