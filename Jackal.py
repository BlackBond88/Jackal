import pygame
import random
from my_colors import *
from my_picture import *

SCREEN_WIDTH = 915
SCREEN_HEIGTH = 915
CELL_SIZE = 70
FIELD_SIZE = 13
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
        self.image_cell = image
        self.i = i              # номер клетки
        self.j = j
        self.x = CELL_SIZE * i + 5     # координата клетки
        self.y = CELL_SIZE * j + 5
        self.active = False

        self.image = self.image_cell
        if self.name != 'sea':
            self.image = image_back

    def click_cell(self):
        self.image = self.image_cell


class Pirate:
    """
    Класс пиратов, содержит информацию о каждом пирте
    """
    def __init__(self, number, player, image_pirate, image_select):
        self.number = number
        self.player = player
        self.image_pirate = image_pirate
        self.image_select = image_select
        self.image = self.image_pirate
        self.selected = False
        self.on_ship = True

        if self.number == 0:
            self.x_local = 4
            self.y_local = 3
        if self.number == 1:
            self.x_local = 32 + 4
            self.y_local = 3
        if self.number == 2:
            self.x_local = 32 + 4
            self.y_local = 32 + 3

        if self.player.color == RED:
            self.x = FIELD_SIZE // 2 * CELL_SIZE + self.x_local + 5
            self.y = self.y_local + 5


class Coin:
    """
    Класс монет, содержит информацию о всех монетах
    """


class Ship:
    """
    Класс кораблей, содержит информацию о кораблях
    """
    def __init__(self, player, image):
        self.player = player
        self.image = image
        self.x = FIELD_SIZE // 2 * CELL_SIZE + 5
        self.y = 5
        self.cell = 6


class GameField:
    """
    Класс поля, содержит информацию об объктах,
    которые находятся на игровом моле
    """
    def __init__(self):
        self.image_back = pygame.image.load('Image/0.png')
        self.select = False
        self.pirates = []
        self.cells = []
        self.ship = ''

    def cells_create(self):
        # считывает название картинок
        picture_list_play = picture_name()
        # перемешивает название картинок
        random.shuffle(picture_list_play)

        # заполняем двумерный моссив именами клеток вместе с "морем"
        n = FIELD_SIZE
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
        for j in range(n):  # наоборот, чтобы массив записывался сверху вних
            for i in range(n):
                image_name = 'Image/' + str(picture_list[i][j]) + '.png'
                image = pygame.image.load(image_name)
                cell = Cell(picture_list[i][j], image, self.image_back, i, j)
                self.cells.append(cell)

        return self.cells

    def pirate_create(self, player):
        image = pygame.image.load('Image/pirate.png')
        image_select = pygame.image.load('Image/pirate_select.png')
        # создаем экземпляр каждого пирата
        for i in range(3):
            pirate = Pirate(i, player, image, image_select)
            self.pirates.append(pirate)

        return self.pirates

    def ship_create(self, player):
        image = pygame.image.load('Image/ship.png')
        # создаем экземпляр коробля для каждого игрока
        self.ship = Ship(player, image)

        return self.ship

    def pirate_select(self, x, y):
        # проверяет попадает ли клик на пирата
        self.select = False
        for pirate in self.pirates:
            if pirate.x < x < pirate.x + 25 and pirate.y < y < pirate.y + 25:
                pirate.image = pirate.image_select
                pirate.selected = True
                self.select = True
            else:
                pirate.image = pirate.image_pirate
                pirate.temp = pirate.selected
                pirate.selected = False
        if not self.select:
            for pirate in self.pirates:
                pirate.selected = pirate.temp

    def pirate_move(self, i_cell):
        # двигает пирата
        if not self.select:
            for pirate in self.pirates:
                if pirate.selected:
                    pirate.x = self.cells[i_cell].x + pirate.x_local
                    pirate.y = self.cells[i_cell].y + pirate.y_local

    def check_on_ship(self, i_cell):
        # проверяет находится ли пират на корабле
        for pirate in self.pirates:
            if pirate.selected:
                if i_cell != self.ship.cell:
                    pirate.on_ship = False
                else:
                    pirate.on_ship = True

    def ship_move(self, i_cell):
        # двигает корабль
        pass

    def available_cells(self, i_cell):
        for cell in self.cells:
            cell.active = False
        # определяет какие клетки доступны для клика
        for pirate in self.pirates:
            if pirate.selected:
                if not pirate.on_ship:
                    self.cells[i_cell + 12].active = True
                    self.cells[i_cell + 13].active = True
                    self.cells[i_cell + 14].active = True
                    self.cells[i_cell + 1].active = True
                    self.cells[i_cell - 1].active = True
                    self.cells[i_cell - 12].active = True
                    self.cells[i_cell - 13].active = True
                    self.cells[i_cell - 14].active = True

        for cell in self.cells:
            if cell.name == 'sea':
                cell.active = False

        for pirate in self.pirates:
            if pirate.selected:
                if pirate.on_ship:
                    self.cells[i_cell + 1].active = True
                    self.cells[i_cell - 1].active = True
                    self.cells[i_cell + 13].active = True

        if not self.select:
            for cell in self.cells:
                cell.active = False


class EventHandling:
    """
    Класс, отвечает за обработку событий в игре
    """
    def __init__(self):
        self.i_cell = 0

    def cursor_position(self, x, y):
        # определяет на какой клетке сделан клик
        self.i_cell = ((y - 5) // CELL_SIZE) * FIELD_SIZE + (x - 5) // CELL_SIZE
        return self.i_cell


class Drawing:
    """
    Класс прорисовки, отвечает за графику в игре
    """
    def __init__(self, screen, game):
        self.screen = screen
        self.game = game

    def draw_all(self):
        for cell in self.game.cells:
            self.screen.blit(cell.image, (cell.x, cell.y))
            if cell.active:
                pygame.draw.rect(self.screen, GREEN, (cell.x - 2, cell.y - 2, 68, 68), 2)

        self.screen.blit(self.game.ships.image, (self.game.ships.x, self.game.ships.y))

        for pirate in self.game.pirates:
            self.screen.blit(pirate.image, (pirate.x, pirate.y))


class GameRound:
    """
    Класс, который отвечает за игровой раунд
    """
    def __init__(self, player1):
        self.players = player1
        self._current_player = 0

        # создает игровое поле
        self.field = GameField()
        self.cells = self.field.cells_create()
        self.pirates = self.field.pirate_create(self.players)
        self.ships = self.field.ship_create(self.players)


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
        self.screen = pygame.display.set_mode((self._width, self._height))
        pygame.display.set_caption(self._title)

        # Игроки
        player1 = Player("Петя", RED)
        self.game_manager = GameRound(player1)
        self.event = EventHandling()

        # Прорисовка
        self.draw = Drawing(self.screen, self.game_manager)

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
                        # определяет на какую клетку был клик
                        x_mouse, y_mouse = pygame.mouse.get_pos()
                        i_cell = self.event.cursor_position(x_mouse, y_mouse)

                        # определяет нажат ли пират
                        self.game_manager.field.pirate_select(x_mouse, y_mouse)

                        # определяет находится ли пират на корабле
                        self.game_manager.field.check_on_ship(i_cell)

                        if self.game_manager.cells[i_cell].active:
                            # переворачивает клетку
                            self.game_manager.cells[i_cell].click_cell()

                            # двигает пирата
                            self.game_manager.field.pirate_move(i_cell)

                        # Проверка на какие клетки можно нажимать
                        self.game_manager.field.available_cells(i_cell)

            # Прорисовка
            self.draw.draw_all()

            pygame.display.flip()
            clock.tick(FPS)
            self.screen.fill(BLACK)


def main():
    window = GameWindow()
    window.main_loop()


if __name__ == '__main__':
    main()
