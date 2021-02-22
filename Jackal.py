import pygame
import random
from my_colors import *
from my_picture import *


FIELD_SIZE = 13


class Player:
    """
    Класс игрока, содержащий имя игрока и цвет пиртов
    """


class Cell:
    """
    Класс клетки, содержит имена всех клеток
    """
    def __init__(self):
        pass


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
        pass

    def cell_create(self):
        # считывает название картинок
        picture_list_play = picture_name()
        # перемешивает название картинок
        random.shuffle(picture_list_play)

        n = FIELD_SIZE
        picture_list = [[''] * n for i in range(n)]
        for i in range(n):
            for j in range(n):
                if j != 0 and j != (n - 1) and i != 0 and i != (n - 1):
                    picture_list[i, j] = picture_list_play[i]
                else:
                    picture_list[i, j] = 'sea'

class GameRound:
    """
    Класс, который отвечает за игровой раунд
    """


class GameWindow:
    """
    Класс, отвечающий за игровое окно
    """


class EventHandling:
    """
    Класс, отвечает за обработку событий в игре
    """


class Drawing:
    """
    Класс прорисовки, отвечает за графику в игре
    """


if __name__ == '__main__':
    test = GameField()
