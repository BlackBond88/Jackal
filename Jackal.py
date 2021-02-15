import pygame
import random
from my_colors import *     # файл названия цвета
from my_picture import *

SCREEN_WIDTH, SCREEN_HEIGTH = 915, 915
FPS = 60


class Cells:
    def __init__(self, name):
        self.name = name

    def cell_draw(self, i , image_name='Image/0.png'):
        """ рисует клетки """
        if self.name == 'sea':
            image_name = 'Image/' + self.name + '.png'
        self.image_cell = pygame.image.load(image_name)
        self.x = 70 * (i % 13) + 5
        self.y = 70 * (i // 13) + 5
        self.rect_cell = pygame.draw.rect(screen, BLACK, (self.x, self.y, 65, 65))
        screen.blit(self.image_cell, self.rect_cell)

    def click(self):
        """ событие при нажатии мышкой """
        self.cell_animation(self.image_cell, 65, 1, -1)

        image_name = 'Image/' + self.name + '.png'
        image_cell = pygame.image.load(image_name)

        self.cell_animation(image_cell, 0, 66, 1)

    def cell_animation(self, image, a, b, c):
        clock = pygame.time.Clock()
        for i in range(a, b, c):
            clock.tick(300)
            new = pygame.transform.scale(image, (i, 65))
            self.rect_cell = pygame.draw.rect(screen, BLACK, (self.x, self.y, 65, 65))
            screen.blit(new, self.rect_cell)
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

    for image in picture_list_all:      # делаем каждую клетку экземляром класса
        cell = Cells(image)
        cells.append(cell)

    return cells


def game_main():
    """ тело игры """

    finished = False
    clock = pygame.time.Clock()     # скорость анимаций

    cells = picture_create()
    for i in range(len(cells)):
        cells[i].cell_draw(i)

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
