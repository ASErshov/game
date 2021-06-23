import pygame
import time

import user
import consts
import collisions
import buttons
from maps import all_maps

pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=512)
pygame.init()


class Game:
    def __init__(self):
        self.round = 0
        self.display_width = consts.display_width
        self.display_height = consts.display_height

        self.display = pygame.display.set_mode((self.display_width, self.display_height))

        self.icon = pygame.image.load(r'assets/icon.png')
        self.background = pygame.image.load(r'assets/background.jpg')

        self.clock = pygame.time.Clock()

    def start_game(self):
        pygame.display.set_caption('Some platformer')

        pygame.mixer.music.load(r'assets/background.mp3')
        pygame.mixer.music.set_volume(0.3)

        pygame.display.set_icon(self.icon)

        self.show_menu()

    def run_game(self):
        user_image = pygame.image.load(r'assets/user.png')
        usr = user.User(self.display_width, self.display_height)
        user_image = pygame.transform.scale(user_image, (usr.width, usr.height))
        run = True
        first_tick = True
        end = False
        pygame.mixer.music.play(-1)
        while run:
            if first_tick:
                if len(all_maps) > self.round:
                    (barriers, win_line) = all_maps[self.round]()
                else:
                    end = True
            first_tick = False

            if end:
                pygame.mixer.music.stop()
                pygame.draw.rect(self.display, (0, 0, 0), (0, 0, self.display_width, self.display_height))
                self.pause('It was last lvl you are passed the game')
                self.round = 0
                self.start_game()
                first_tick = True

            fail = collisions.check_collisions(usr, barriers) or usr.x <= 0 or usr.y > self.display_height
            win = win_line() <= -100
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE] and not usr.make_fall:
                usr.set_make_jump()
            if keys[pygame.K_ESCAPE]:
                self.pause('Paused, press enter to continue')
            if keys[pygame.K_r]:
                pygame.mixer.music.stop()
                self.run_game()
                first_tick = True

            if fail:
                pygame.mixer.music.stop()
                self.pause('You are lose, press enter to restart')
                self.run_game()
                first_tick = True

            if win:
                pygame.mixer.music.stop()
                self.pause('You are win, press enter to restart, or n to next lvl', 450, True)
                self.run_game()
                first_tick = True

            if usr.make_jump:
                usr.jump()
            if usr.make_fall:
                usr.fall()

            self.display.blit(self.background, (0, 0))

            self.display.blit(user_image, (usr.x, usr.y))

            for let in barriers:
                try:
                    self.draw_let(let.type, let.color, let.x, let.y, let.width,
                             let.height, let.count)

                except:
                    self.draw_let(let.type, let.color, let.x, let.y, let.width,
                             let.height)
                let.move()

            pygame.display.update()
            self.clock.tick(100)

    def draw_let(self, type, color, x, y, width, height, count=1):
        if type == consts.triangle:
            for i in range(count):
                tmp_x = x + width * i
                pygame.draw.polygon(self.display, color,
                                    [(tmp_x, y + height), (tmp_x + width // 2, y), (tmp_x + width, y + height)])
        if type == consts.landscape:
            pygame.draw.rect(self.display, color, (x, y, width, height))
        if type == consts.asteroid:
            pygame.draw.circle(self.display, color, (x + width // 2, y + width // 2), width // 2)
        if type == consts.laser:
            pygame.draw.circle(self.display, color, (x + width // 2, y + width // 2), width // 2)

    def print_text(self, message, x, y, font_color=(227, 169, 220), font_type=r'fonts/FreckleFace.ttf', font_size=50):
        font = pygame.font.Font(font_type, font_size)
        text = font.render(message, True, font_color)
        self.display.blit(text, (x, y))

    def pause(self, message, line_length=300, win=False):
        global round

        paused = True
        while paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            self.print_text(message, self.display_width // 2 - line_length, self.display_height // 2 - 50)
            pygame.display.update()
            self.clock.tick(15)

            keys = pygame.key.get_pressed()
            if keys[pygame.K_RETURN]:
                paused = False
            if keys[pygame.K_n] and win:
                paused = False
                self.round += 1

    def show_menu(self):
        menu_bckgr = pygame.image.load(r'assets/menu.jpg')
        show = True
        button_lvl = buttons.Button(250, 70, 'Choose LVL')
        button_start = buttons.Button(270, 70, 'Start Game')

        while show:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            self.display.blit(menu_bckgr, (0, 0))
            button_start.draw(self.display, 840, 100, self.run_game)
            button_lvl.draw(self.display, 850, 200, self.show_lvls)

            pygame.display.update()
            self.clock.tick(60)

    def choose_lvl(self, lvl):
        def tmp_lvl():
            self.round = lvl
            self.run_game()
        return tmp_lvl

    def show_lvls(self):

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
            self.display.blit(menu_bckgr, (0, 0))

            for lvl in range(len(all_maps)):
                lvl_buttons[lvl].draw(self.display, 170 + 220 * lvl, 100, self.choose_lvl(lvl))

            pygame.display.update()
            self.clock.tick(60)


game = Game()
game.start_game()

