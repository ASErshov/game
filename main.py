import pygame

import user
import let
import consts
import movement
import collisions


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
    triangles = let.Triangles(display_width - 20 - 100, display_height - 20 - consts.ground_height, 5)
    landscape = let.Landscapes(200, 40, display_width - 500, display_height - 100 - consts.ground_height)
    landscape2 = let.Landscapes(200, 40, display_width - 400, display_height - 60 - consts.ground_height)
    barriers = [landscape2, landscape]
    while run:
        fail = collisions.check_collisions(usr, barriers) or usr.x <= 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and not usr.make_fall:
            usr.set_make_jump()
        if keys[pygame.K_ESCAPE]:
            pause(display, 'Paused, press enter to continue', clock)

        if fail:
            pause(display, 'You are lose, press enter to restart', clock)
            start_game()

        if usr.make_jump:
            usr.jump()
        if usr.make_fall:
            usr.fall()

        display.blit(background, (0, 0))

        display.blit(user_image, (usr.x, usr.y))
        draw_let(display, triangles.type, triangles.color, triangles.x, triangles.y, triangles.width, triangles.height, triangles.count)
        draw_let(display, landscape.type, landscape.color, landscape.x, landscape.y, landscape.width, landscape.height)
        draw_let(display, landscape2.type, landscape2.color, landscape2.x, landscape2.y, landscape2.width, landscape2.height)
        triangles.move()
        landscape.move()
        landscape2.move()
        pygame.display.update()
        clock.tick(50)


def draw_let(display, type, color, x, y, width, height, count=1):
    if type == consts.triangle:
        for i in range(count):
            tmp_x = x + width * i
            pygame.draw.polygon(display, color, [(tmp_x, y + height), (tmp_x + width // 2, y), (tmp_x + width, y + height)])
    if type == consts.landscape:
        pygame.draw.rect(display, color, (x, y, width, height))


def print_text(display, message, x, y, font_color = (227, 169, 220), font_type=r'fonts/FreckleFace.ttf', font_size=50):
    font = pygame.font.Font(font_type, font_size)
    text = font.render(message, True, font_color)
    display.blit(text, (x, y))


def pause(display, message, clock):
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        print_text(display, message, consts.display_width // 2 - 300, consts.display_height // 2 - 50)
        pygame.display.update()
        clock.tick(15)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            paused = False


start_game()
