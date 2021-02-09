import pygame


SCREEN_WIDTH, SCREEN_HEIGTH = 800, 600


def game_main():
    finished = False

    while not finished:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True


    #pygame.display.update()


if __name__ == "__main__":
    pygame.init()
    pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGTH))
    #pygame.display.update()

    game_main()
