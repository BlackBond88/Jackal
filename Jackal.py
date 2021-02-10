import pygame
from my_colors import *     # файл названия цвета
from my_picture import *

SCREEN_WIDTH, SCREEN_HEIGTH = 1200, 800
FPS = 60


class Cells:
    def __init__(self, name):
        self.name = name

    def cell_draw(self, i):
        """ рисует клетки """
        self.i = i
        image_name = 'Image/' + self.name + '.png'
        image_cell = pygame.image.load(image_name)
        rect_cell = pygame.draw.rect(screen, BLACK, (100+self.i*100, 100, 100, 100))
        screen.blit(image_cell, rect_cell)

#rect = pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.heigth))

def picture_create():
    """ Создает клетку поля """
    picture_list = picture_load()   #
    cells = []
    i = 1
    for image in picture_list:      # создает клетки на поле
        cell = Cells(image)
        cell.cell_draw(i)
        i += 1
        cells.append(cell)

    return cells


def game_main():
    """ тело игры """

    finished = False
    clock = pygame.time.Clock()     # скорость анимаций

    cells = picture_create()                # создает массив картинок

    #for cell in cells:                      # рисует клетки
     #   cell.cell_draw()

    while not finished:             # запуск игры (цикл)
        clock.tick(FPS)

        for event in pygame.event.get():    # события в игре
            if event.type == pygame.QUIT:   # выход из игры
                finished = True

        pygame.display.update()     # обновление экрана
        #screen.fill(WHITE)          # закрашивает экран

    pygame.quit()                   # выход из игры


if __name__ == '__main__':
    # сознание окна для игры
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGTH))
    pygame.display.set_caption("Jackal")
    pygame.display.update()

    game_main()
