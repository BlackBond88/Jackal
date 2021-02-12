import pygame
from my_colors import *     # файл названия цвета
from my_picture import *

SCREEN_WIDTH, SCREEN_HEIGTH = 915, 915
FPS = 60


class Cells:
    def __init__(self, name):
        self.name = name

    def cell_draw(self, i):
        """ рисует клетки """
        image_name = 'Image/' + self.name + '.png'
        image_cell = pygame.image.load(image_name)
        x = 70 * (i % 13) + 5
        y = 70 * (i // 13) + 5
        rect_cell = pygame.draw.rect(screen, BLACK, (x, y, 65, 65))
        screen.blit(image_cell, rect_cell)


def picture_create():
    """ Создает клетку поля """
    picture_list = picture_name()   # считывает название картинок
    cells = []
    counter = 0
    for image in picture_list:      # делаем каждую клетку экземляром класса
        cell = Cells(image)
        cells.append(cell)
        cell.cell_draw(counter)
        counter += 1

    return cells


def game_main():
    """ тело игры """

    finished = False
    clock = pygame.time.Clock()     # скорость анимаций

    picture_create()

    while not finished:             # запуск игры (цикл)
        clock.tick(FPS)

        for event in pygame.event.get():    # события в игре
            if event.type == pygame.QUIT:   # выход из игры
                finished = True
            if event.type == pygame.MOUSEBUTTONDOWN:    # нажатие ЛКМ
                if event.button == 1:
                    print("22")

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
