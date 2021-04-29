from consts import ground_height


class User:
    def __init__(self, display_width, display_height):
        self.width = 50
        self.height = 50
        self.x = display_width // 3
        self.y = display_height - self.height - ground_height
        self.color = (212, 136, 29)
        self.jump_counter = 20
        self.make_jump = False

    def set_make_jump(self):
        self.make_jump = True

    def jump(self):
        if self.jump_counter >= -20:
            self.y -= self.jump_counter / 2.5
            self.jump_counter -= 1
        else:
            self.jump_counter = 20
            self.make_jump = False
