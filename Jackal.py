import pygame
from my_colors import *     # файл названия цвета
from my_picture import *

SCREEN_WIDTH, SCREEN_HEIGTH = 1200, 800
FPS = 60


class Cells:
    def __init__(self, name):
        self.name = name

    def create(self):
        """ Создает клетку поля """
        picture_list = picture_load()




def game_main():
    """ тело игры """

    finished = False
    clock = pygame.time.Clock()     # скорость анимаций

    while not finished:             # запуск игры (цикл)
        clock.tick(FPS)

        for event in pygame.event.get():    # события в игре
            if event.type == pygame.QUIT:   # выход из игры
                finished = True

        pygame.display.update()     # обновление экрана
        screen.fill(WHITE)          # закрашивает экран черным

    pygame.quit()                   # выход из игры


if __name__ == '__main__':
    # сознание окна для игры
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGTH))
    pygame.display.set_caption("Jackal")
    pygame.display.update()

    game_main()
