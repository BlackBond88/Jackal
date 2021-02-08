import pygame


def main():
    pygame.init()
    size = (800, 600)
    red = (255, 0, 0)
    black = (250, 250, 250)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("MyGame")
    image_icon = pygame.image.load("icon.png")


    font = pygame.font.SysFont('Comic Sans MS', 16)

    text = font.render("Добро пожаловать в игру MyGame! ", True, red, black)
    width, heigth = text.get_size()
    x, y = 0, 0
    direct_x, direct_y = 1, 1

    fps = 60
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        clock.tick(fps)
        screen.fill(black)
        image = image_icon.get_rect()
        screen.blit(image_icon, image)
        screen.blit(text, (x, y))
        x += direct_x
        y += direct_y
        if x + width >= 800 or x <= 0:
            direct_x = - direct_x
        if y + heigth >= 600 or y <= 0:
            direct_y = - direct_y
        pygame.display.update()
        image = image_icon.get_rect()
        screen.blit(image_icon, image)


if __name__ == "__main__":
    main()
