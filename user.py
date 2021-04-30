from consts import ground_height


class User:
    def __init__(self, display_width, display_height):
        self.width = 50
        self.height = 50
        self.x = display_width // 3
        self.y = display_height - self.height - ground_height
        self.color = (212, 136, 29)
        self.jump_counter = 25
        self.max_jump = 25
        self.start_jump_y = self.y
        self.make_jump = False
        self.make_fall = False
        self.fall_height = 0
        self.fall_counter = 0
        self.fall_sum = -0.25

    def set_make_jump(self):
        self.make_jump = True

    def set_jump(self, top):
        if self.make_jump:
            self.max_jump = top
            self.jump_counter = 0

    def jump(self):
        if self.jump_counter == 25:
            self.start_jump_y = self.y
        if self.jump_counter >= -self.max_jump:
            self.y -= self.jump_counter / 2.5
            self.jump_counter -= 1
        else:
            self.y = self.start_jump_y
            self.jump_counter = 25
            self.max_jump = 25
            self.make_jump = False

    def ram(self, speed):
        self.x -= speed

    def stand(self, y):
        self.start_jump_y = y
        self.y = y

    def fall(self):
        if self.fall_sum <= self.fall_height:
            self.y += self.fall_counter / 2.5
            self.fall_counter += 1
            self.fall_sum += self.fall_counter / 2.5
        else:
            self.y += self.fall_counter / 2.5
            self.make_fall = False
            self.fall_height = 0
            self.fall_counter = 0
            self.fall_sum = 0

    def set_fall(self, height):
        self.fall_height = height
        self.make_fall = True

    def stop_fall(self):
        if self.make_fall:
            self.make_fall = False
            self.fall_height = 0
            self.fall_counter = 0
            self.fall_sum = 0
