import pygame

import user
import let
import consts
import movement

pygame.init()


def start_game():
    display_width = consts.display_width
    display_height = consts.display_height

    display = pygame.display.set_mode((display_width, display_height))
    pygame.display.set_caption('Some platformer')

    icon = pygame.image.load(r'assets/icon.png')
    background = pygame.image.load(r'assets/background.jpg')
    user_image = pygame.image.load(r'assets/user.png')
    pygame.display.set_icon(icon)

    clock = pygame.time.Clock()

    run = True
    usr = user.User(display_width, display_height)
    user_image = pygame.transform.scale(user_image, (usr.width, usr.height))
    triangles = let.Triangles(display_width, display_height, 5)
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            usr.set_make_jump()

        if usr.make_jump:
            usr.jump()

        display.blit(background, (0, 0))

        display.blit(user_image, (usr.x, usr.y))
        draw_let(display, triangles.type, triangles.color, triangles.x, triangles.y, triangles.width, triangles.height, triangles.count)
        triangles.move()
        pygame.display.update()
        clock.tick(200)


def draw_let(display, type, color, x, y, width, height, count):
    if type == consts.triangle:
        for i in range(count):
            tmp_x = x + width * i
            pygame.draw.polygon(display, color, [(tmp_x, y + height), (tmp_x + width // 2, y), (tmp_x + width, y + height)])


start_game()
