import pygame
import random
from my_colors import *  # файл названия цвета
from my_picture import *

SCREEN_WIDTH, SCREEN_HEIGTH = 915, 915
IMAGE_BACKGROUND = pygame.image.load('Image/0.png')
ICON = pygame.image.load('Image/icon.png')
FPS = 60
PLAYERS_NUMBER = 1  # Для тестовой версии для одного игрока


class GameObject:
    def __init__(self, name):
        self.name = name
        self.cells = picture_create()  # создает клетки
        self.pirates = pirate_create(PLAYERS_NUMBER)  # создает пиратов

    def pirate_choice(self, x, y, i_cell):
        for i in range(3):
            pygame.draw.rect(screen, WHITE, (self.pirates[i].x, self.pirates[i].y, 18, 30), 2)
        for i in range(3):
            p_x = self.pirates[i].x
            p_y = self.pirates[i].y
            if ((p_x + 20) > x > p_x) and ((p_y + 34) > y > p_y):
                self.cells[i_cell + 13].marker = True
                pygame.draw.rect(screen, RED, (p_x, p_y, 18, 30), 2)
                c_x = self.cells[i_cell + 13].x
                c_y = self.cells[i_cell + 13].y
                pygame.draw.rect(screen, GREEN, (c_x - 2, c_y - 2, 68, 68), 2)
                return i
        return False

    def cell_marker(self):
        for cell in self.cells:
            cell.marker = False
            c_x = cell.x
            c_y = cell.y
            pygame.draw.rect(screen, BLACK, (c_x - 2, c_y - 2, 68, 68), 2)


class Cells:
    def __init__(self, name, image_cell, i, marker=False):
        self.name = name
        self.image_cell = image_cell
        self.i = i
        self.x = 70 * (i % 13) + 5
        self.y = 70 * (i // 13) + 5
        self.marker = marker
        if self.name != 'sea':
            screen.blit(IMAGE_BACKGROUND, (self.x, self.y))
        else:
            screen.blit(self.image_cell, (self.x, self.y))

    def click(self):
        """ событие при нажатии мышкой """
        if self.marker:
            self.animation(IMAGE_BACKGROUND, 65, 1, -1)
            self.animation(self.image_cell, 0, 66, 1)

    def animation(self, image, a, b, c):
        clock = pygame.time.Clock()
        for i in range(a, b, c):
            clock.tick(350)
            new_picture = pygame.transform.scale(image, (i, 65))
            pygame.draw.rect(screen, BLACK, (self.x, self.y, 65, 65))
            screen.blit(new_picture, (self.x, self.y))
            pygame.display.update()


class Pirate:
    def __init__(self, image_pirate, i):
        self.image_pirate = image_pirate
        self.x = 70 * 6 + 8 + i * 21
        self.y = 7

        self.rect_pirate = pygame.draw.rect(screen, WHITE, (self.x, self.y, 18, 30), 2)
        screen.blit(self.image_pirate, self.rect_pirate)

    def animation(self, i_cell):
        i_pirate = ((self.y - 5) // 70) * 13 + (self.x - 5) // 70
        if i_pirate == i_cell:
            return

        '''clock = pygame.time.Clock()
        for i in range(75):
            clock.tick(350)
            new_picture = pygame.transform.scale(self.image_pirate, (i, 65))
            pygame.transform.rotate(90)
            pygame.draw.rect(screen, BLACK, (self.x, self.y, 65, 65))
            screen.blit(new_picture, (self.x, self.y))
            pygame.display.update()'''


def picture_create():
    """ Создает клетку поля """
    picture_list = picture_name()  # считывает название картинок
    random.shuffle(picture_list)  # перемешивает картинки

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
    cells = []
    for i in range(len(picture_list_all)):
        cell = Cells(picture_list_all[i], image_cells[i], i)
        cells.append(cell)

    return cells


def pirate_create(n):
    """ Создает пирата """
    # Загружает картинки пиратов
    image_pirates = []
    for i in range(3):
        image_name = 'Image/pirate_' + str(i + 1) + '.png'
        image_pirates.append(pygame.image.load(image_name))

    # делает пирата экзмемпляром класса
    pirates = []
    for i in range(n * 3):
        pirate = Pirate(image_pirates[i], i)
        pirates.append(pirate)

    return pirates


def game_main():
    """ тело игры """

    finished = False
    clock = pygame.time.Clock()  # скорость анимаций

    game = GameObject('Jackal')

    while not finished:  # запуск игры (цикл)
        clock.tick(FPS)

        for event in pygame.event.get():  # события в игре
            if event.type == pygame.QUIT:  # выход из игры
                finished = True
            if event.type == pygame.MOUSEBUTTONUP:  # нажатие ЛКМ
                if event.button == 1:
                    x_mouse, y_mouse = pygame.mouse.get_pos()
                    i_cell = ((y_mouse - 5) // 70) * 13 + (x_mouse - 5) // 70  # номер клетки
                    pirate_choice = game.pirate_choice(x_mouse, y_mouse, i_cell)
                    if not pirate_choice:
                        game.pirates[pirate_choice].animation(i_cell)
                        game.cells[i_cell].click()
                        game.cell_marker()

        pygame.display.update()  # обновление экрана
        # screen.fill(BLACK)          # закрашивает экран

    pygame.quit()  # выход из игры


if __name__ == '__main__':
    # сознание окна для игры
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGTH))
    pygame.display.set_icon(ICON)
    pygame.display.set_caption("Jackal")
    pygame.display.update()

    game_main()
