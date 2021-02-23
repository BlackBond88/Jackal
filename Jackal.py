import pygame
import random
from my_colors import *
from my_picture import *

SCREEN_WIDTH = 915
SCREEN_HEIGTH = 915
ICON = pygame.image.load('Image/icon.png')
GAME_NAME = 'Jackal'
FPS = 60


class Player:
    """
    Класс игрока, содержащий имя игрока и цвет пиртов
    """
    def __init__(self, name, color):
        self.name = name
        self.color = color


class Cell:
    """
    Класс клетки, содержит имена всех клеток
    """
    def __init__(self, name, image, image_back, i, j):
        self.name = name
        self.image = image
        self.image_back = image_back
        self.i = i              # номер клетки
        self.j = j
        self.x = 70 * i + 5     # координата клетки
        self.y = 70 * j + 5



class Pirate:
    """
    Класс пиратов, содержит информацию о каждом пирте
    """


class Coin:
    """
    Класс монет, содержит информацию о всех монетах
    """


class Ship:
    """
    Класс кораблей, содержит информацию о кораблях
    """


class GameField:
    """
    Класс поля, содержит информацию об объктах,
    которые находятся на игровом моле
    """
    def __init__(self):
        self.field_size = 13
        self.imgage_back = pygame.image.load('Image/0.png')

    def cells_create(self):
        # считывает название картинок
        picture_list_play = picture_name()
        # перемешивает название картинок
        random.shuffle(picture_list_play)

        # заполняем двумерный моссив именами клеток вместе с "морем"
        n = self.field_size
        # добавляем клетки по краям поля
        picture_list_play.insert(0, 'sea')
        picture_list_play.insert(n - 3, 'sea')
        picture_list_play.insert((n - 2) * (n - 3), 'sea')
        picture_list_play.insert((n - 2) * (n - 2) - 1, 'sea')
        picture_list = [[''] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if j != 0 and j != (n - 1) and i != 0 and i != (n - 1):
                    picture_list[i][j] = picture_list_play[(j-1) * (n-2) + i-1]
                else:
                    picture_list[i][j] = 'sea'

        # создаем экземпляр каждой клетки
        cells = []
        for i in range(n):
            for j in range(n):
                image_name = 'Image/' + str(picture_list[i][j]) + '.png'
                image = pygame.image.load(image_name)
                cell = Cell(picture_list[i][j], image, self.imgage_back, i, j)
                cells.append(cell)

        return cells


class EventHandling:
    """
    Класс, отвечает за обработку событий в игре
    """


class Drawing:
    """
    Класс прорисовки, отвечает за графику в игре
    """
    def __init__(self, objects, screen):
        self.objects = objects
        self.screen = screen


class GameRound:
    """
    Класс, который отвечает за игровой раунд
    """
    def __init__(self, player1):
        self._players = player1
        self._current_player = 0

        # создает игровое поле
        self.field = GameField()
        self.cells = self.field.cells_create()


class GameWindow:
    """
    Класс, отвечающий за игровое окно
    """
    def __init__(self):
        # инициализация pygame
        pygame.init()

        # Window
        self._width = SCREEN_WIDTH
        self._height = SCREEN_HEIGTH
        self._title = GAME_NAME
        self._screen = pygame.display.set_mode((self._width, self._height))
        pygame.display.set_caption(self._title)

        # Игроки
        player1 = Player("Петя", RED)
        self.game_manager = GameRound(player1)

    # цикл игры
    def main_loop(self):
        finished = False
        clock = pygame.time.Clock()
        while not finished:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    finished = True
                if event.type == pygame.MOUSEBUTTONUP:  # нажатие ЛКМ
                    if event.button == 1:
                        x_mouse, y_mouse = pygame.mouse.get_pos()
                        

            # Прорисовка
            for cell in self.game_manager.cells:
                if cell.name != 'sea':
                    self._screen.blit(cell.image_back, (cell.x, cell.y))
                else:
                    self._screen.blit(cell.image, (cell.x, cell.y))

            pygame.display.flip()
            clock.tick(FPS)


def main():
    window = GameWindow()
    window.main_loop()
    print('Game over!')


if __name__ == '__main__':
    main()
