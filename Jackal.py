import pygame
import random
from my_colors import *     # файл названия цвета
from my_picture import *

SCREEN_WIDTH, SCREEN_HEIGTH = 915, 915
IMAGE_BACKGROUND = pygame.image.load('Image/0.png')
FPS = 60


class Cells:
    def __init__(self, name, image_cell, i):
        self.name = name
        self.image_cell = image_cell
        self.x = 70 * (i % 13) + 5
        self.y = 70 * (i // 13) + 5
        self.rect_cell = pygame.draw.rect(screen, BLACK, (self.x, self.y, 65, 65))
        if self.name != 'sea':
            screen.blit(IMAGE_BACKGROUND, self.rect_cell)
        else:
            screen.blit(self.image_cell, self.rect_cell)

    def click(self):
        """ событие при нажатии мышкой """
        self.cell_animation(IMAGE_BACKGROUND, 65, 1, -1)
        self.cell_animation(self.image_cell, 0, 66, 1)

    def cell_animation(self, image, a, b, c):
        clock = pygame.time.Clock()
        for i in range(a, b, c):
            clock.tick(250)
            new_picture = pygame.transform.scale(image, (i, 65))
            self.rect_cell = pygame.draw.rect(screen, BLACK, (self.x, self.y, 65, 65))
            screen.blit(new_picture, self.rect_cell)
            pygame.display.update()


def picture_create():
    """ Создает клетку поля """
    picture_list = picture_name()   # считывает название картинок
    random.shuffle(picture_list)    # перемешивает картинки

    cells = []
    picture_list_all = [''] * 169
    counter_picture = 0
    for i in range(169):
        if i % 13 != 0 and (i + 1) % 13 != 0 and 14 < i < 154 and i != 24 and i != 144:
            picture_list_all[i] = picture_list[counter_picture]
            counter_picture += 1
        else:
            picture_list_all[i] = 'sea'

    # загружает все картинки
    image_cells = []
    for name in picture_list_all:
        image_name = 'Image/' + name + '.png'
        image_cells.append(pygame.image.load(image_name))

    # делает каждую клетку экземляром класса
    for i in range(len(picture_list_all)):
        cell = Cells(picture_list_all[i], image_cells[i], i)
        cells.append(cell)

    return cells


def game_main():
    """ тело игры """

    finished = False
    clock = pygame.time.Clock()     # скорость анимаций

    cells = picture_create()        # создает клетки

    while not finished:             # запуск игры (цикл)
        clock.tick(FPS)

        for event in pygame.event.get():    # события в игре
            if event.type == pygame.QUIT:   # выход из игры
                finished = True
            if event.type == pygame.MOUSEBUTTONDOWN:    # нажатие ЛКМ
                if event.button == 1:
                    x_mouse, y_mouse = pygame.mouse.get_pos()
                    i_cell = ((y_mouse-5)//70)*13 + (x_mouse-5)//70     # номер клетки
                    cells[i_cell].click()

        pygame.display.update()     # обновление экрана
        # screen.fill(BLACK)          # закрашивает экран

    pygame.quit()                   # выход из игры


if __name__ == '__main__':
    # сознание окна для игры
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGTH))
    pygame.display.set_caption("Jackal")
    pygame.display.update()

    game_main()
