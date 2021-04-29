import movement
from consts import ground_height


class Let(movement.Movement):
    def __init__(self, color, width, height, x, y, speed, direction):
        movement.Movement.__init__(self, x, y, speed, direction, width)
        self.width = width
        self.height = height
        self.color = color


class Triangles(Let):
    def __init__(self, display_width, display_height, count):
        Let.__init__(self, (104, 160, 245), 20, 20, display_width - 20 - ground_height, display_height - 20 - ground_height, 4, 1)
        self.type = 'triangle'
        self.count = count
