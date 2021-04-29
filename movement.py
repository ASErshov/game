class Movement:
    def __init__(self, x, y, speed, direction, width):
        self.x = x
        self.y = y
        self.start_x = x
        self.start_y = y
        self.width = width
        self.speed = direction * speed

    def move(self):
        if self.x >= -self.width:
            self.x -= self.speed
        else:
            self.x = self.start_x
