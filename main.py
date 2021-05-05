import pygame
import time

import user
import consts
import collisions
import buttons
from maps import all_maps

pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=512)
pygame.init()
round = 0


def start_game():
    display_width = consts.display_width
    display_height = consts.display_height

    display = pygame.display.set_mode((display_width, display_height))
    pygame.display.set_caption('Some platformer')

    pygame.mixer.music.load(r'assets/background.mp3')
    pygame.mixer.music.set_volume(0.3)

    icon = pygame.image.load(r'assets/icon.png')
    background = pygame.image.load(r'assets/background.jpg')

    pygame.display.set_icon(icon)

    clock = pygame.time.Clock()



    def run_game():
        global round
        user_image = pygame.image.load(r'assets/user.png')
        usr = user.User(display_width, display_height)
        user_image = pygame.transform.scale(user_image, (usr.width, usr.height))
        run = True
        first_tick = True
        end = False
        pygame.mixer.music.play(-1)
        while run:
            if first_tick:
                if len(all_maps) > round:
                    (barriers, win_line) = all_maps[round]()
                else:
                    end = True
            first_tick = False

            if end:
                pygame.mixer.music.stop()
                pygame.draw.rect(display, (0, 0, 0), (0, 0, display_width, display_height))
                pause(display, 'It was last lvl you are passed the game', clock)
                round = 0
                start_game()
                first_tick = True

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
            if keys[pygame.K_r]:
                pygame.mixer.music.stop()
                run_game()
                first_tick = True

            if fail:
                pygame.mixer.music.stop()
                pause(display, 'You are lose, press enter to restart', clock)
                run_game()
                first_tick = True

            if win:
                pygame.mixer.music.stop()
                pause(display, 'You are win, press enter to restart, or n to next lvl', clock, 450, True)
                run_game()
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

    show_menu(display, clock, run_game)


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


def pause(display, message, clock, line_length=300, win=False):
    global round

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
        if keys[pygame.K_n] and win:
            paused = False
            round += 1


def show_menu(display, clock, run_game):
    menu_bckgr = pygame.image.load(r'assets/menu.jpg')
    show = True
    button_lvl = buttons.Button(250, 70, 'Choose LVL')
    button_start = buttons.Button(270, 70, 'Start Game')

    while show:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        display.blit(menu_bckgr, (0, 0))
        button_start.draw(display, 840, 100, run_game)
        button_lvl.draw(display, 850, 200, show_lvls(display, clock, run_game))

        pygame.display.update()
        clock.tick(60)


def show_lvls(display, clock, run_game):

    def choose_lvl(lvl):
        def tmp_lvl():
            global round
            round = lvl
            run_game()
        return tmp_lvl

    def tmp():
        menu_bckgr = pygame.image.load(r'assets/menu.jpg')
        show = True
        lvl_buttons = []
        for lvl in range(len(all_maps)):
            lvl_buttons.append(buttons.Button(50, 70, str(lvl)))
        while show:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            display.blit(menu_bckgr, (0, 0))

            for lvl in range(len(all_maps)):
                lvl_buttons[lvl].draw(display, 170 + 220 * lvl, 100, choose_lvl(lvl))

            pygame.display.update()
            clock.tick(60)
    return tmp


start_game()

