import pygame
from enum import Enum

FPS = 60
CELL_SIZE = 50


class Cell():
    VOID = 0
    CROSS = 1
    ZERO = 2


class Player:
    """
    Класс игрока, содержащий тип значков и имя.
    """
    def __init__(self, name, cell_type):
        self.name = name
        self.cell_type = cell_type


class GameField:
    def __init__(self):
        self.height = 3
        self.width = 3
        self.cells = [[Cell.VOID]*self.width for i in range(self.height)]


class GameFieldView:
    """
    Виджет игрового поля, который отображает его на экране, а также выясняет место клика
    """
    def __init__(self, field):
        # загрузить картинки занчков клеток...
        self._image_field = pygame.image.load('Image/field.png')
        self._image_cross = pygame.image.load('Image/cross.png')
        self._image_zero = pygame.image.load('Image/zero.png')
        # отобразить первичное состояние поля
        self.field = field
        self.height = field.height * CELL_SIZE
        self.width = field.width * CELL_SIZE

    def draw(self, f):
        for i in range(3):
            for j in range(3):
                f.blit(self._image_cross, (i * CELL_SIZE, j * CELL_SIZE))

    def check_coords_correct(self, x, y):
        return True     # TODO: self._heeght учесвть

    def get_coords(self, x, y):
        return 0, 0    # TODO: реально вычислить клетку клика


class GameRoundManager:
    """
    Менеджер игры, запускающий все процессы.
    """
    def __init__(self, player1: Player, player2: Player):
        self._players = [player1, player2]
        self._current_player = 0
        self.field = GameField()

    def handle_click(self, i, j):
        player = self._players[self._current_player]
        # игрок делает клик на поле
        print("click_handled", i, j)


class GameWindow:
    """
    Содержит виджет поля,
    а также менеджер игрового раунда.
    """
    def __init__(self):
        # инициализация pygame
        pygame.init()

        # Window
        self._width = 800
        self._height = 600
        self._title = "Crosses $ Zeroes"
        self._screen = pygame.display.set_mode((self._width, self._height))
        pygame.display.set_caption(self._title)

        player1 = Player("Петя", Cell.CROSS)
        player2 = Player("Вася", Cell.ZERO)
        self._game_manager = GameRoundManager(player1, player2)
        self._field_widget = GameFieldView(self._game_manager.field)

    def main_loop(self):
        finished = False
        clock = pygame.time.Clock()
        while not finished:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    finished = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    if self._field_widget.check_coords_correct(x, y):
                        i, j = self._field_widget.get_coords(x, y)
                        self._game_manager.handle_click(i, j)

            self._field_widget.draw(self._screen)
            pygame.display.flip()
            clock.tick(FPS)


def main():
    window = GameWindow()
    window.main_loop()
    print('Game over!')


if __name__ == "__main__":
    main()
