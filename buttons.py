import pygame


class Button:
    def __init__(self, width, height,  message, font_type=r'fonts/FreckleFace.ttf', font_size=50):
        self.width = width
        self.height = height
        self.inactive_color = (0, 0, 255)
        self.active_color = (53, 90, 221)
        self.button_sound = pygame.mixer.Sound(r'assets/button.wav')
        self.message = message
        self.font_type = font_type
        self.font_size = font_size

    def draw(self, display, x, y, callback=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x < mouse[0] < x + self.width and y < mouse[1] < y + self.height:

            pygame.draw.rect(display, self.active_color, (x, y, self.width, self.height))

            if click[0] == 1 and callback is not None:
                self.button_sound.play()
                pygame.time.delay(300)
                callback()
        else:
            pygame.draw.rect(display, self.inactive_color, (x, y, self.width, self.height))

        font = pygame.font.Font(self.font_type, self.font_size)
        text = font.render(self.message, True, (255, 134, 0))
        display.blit(text, (x + 10, y + 10))
