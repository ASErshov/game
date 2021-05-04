import pygame
import time

import user
import consts
import collisions
from maps import all_maps

pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=512)
pygame.init()

def start_game():
    display_width = consts.display_width
    display_height = consts.display_height

    display = pygame.display.set_mode((display_width, display_height))
    pygame.display.set_caption('Some platformer')

    pygame.mixer.music.load(r'assets/background.mp3')
    pygame.mixer.music.set_volume(0.3)

    icon = pygame.image.load(r'assets/icon.png')
    background = pygame.image.load(r'assets/background.jpg')
    user_image = pygame.image.load(r'assets/user.png')
    pygame.display.set_icon(icon)

    clock = pygame.time.Clock()

    run = True
    usr = user.User(display_width, display_height)
    user_image = pygame.transform.scale(user_image, (usr.width, usr.height))
    first_tick = True
    pygame.mixer.music.play(-1)
    while run:
        if first_tick:
            (barriers, win_line) = all_maps[0]()
        first_tick = False

        fail = collisions.check_collisions(usr, barriers) or usr.x <= 0 or usr.y > consts.display_height
        win = win_line() <= -100
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
            pygame.mixer.music.stop()
            pause(display, 'You are lose, press enter to restart', clock)
            start_game()
            first_tick = True

        if win:
            pygame.mixer.music.stop()
            pause(display, 'You are win, press enter to restart, or n to next lvl', clock, 450)
            start_game()
            first_tick = True

        if usr.make_jump:
            usr.jump()
        if usr.make_fall:
            usr.fall()

        display.blit(background, (0, 0))

        display.blit(user_image, (usr.x, usr.y))

        for let in barriers:
            try:
                draw_let(display, let.type, let.color, let.x, let.y, let.width,
                         let.height, let.count)

            except:
                draw_let(display, let.type, let.color, let.x, let.y, let.width,
                         let.height)
            let.move()

        pygame.display.update()
        clock.tick(100)


def draw_let(display, type, color, x, y, width, height, count=1):
    if type == consts.triangle:
        for i in range(count):
            tmp_x = x + width * i
            pygame.draw.polygon(display, color, [(tmp_x, y + height), (tmp_x + width // 2, y), (tmp_x + width, y + height)])
    if type == consts.landscape:
        pygame.draw.rect(display, color, (x, y, width, height))
    if type == consts.asteroid:
        pygame.draw.circle(display, color, (x+width//2, y+width//2), width//2)
    if type == consts.laser:
        pygame.draw.circle(display, color, (x+width//2, y+width//2), width//2)


def print_text(display, message, x, y, font_color=(227, 169, 220), font_type=r'fonts/FreckleFace.ttf', font_size=50):
    font = pygame.font.Font(font_type, font_size)
    text = font.render(message, True, font_color)
    display.blit(text, (x, y))


def pause(display, message, clock, line_length=300):
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        print_text(display, message, consts.display_width // 2 - line_length, consts.display_height // 2 - 50)
        pygame.display.update()
        clock.tick(15)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            paused = False


start_game()
