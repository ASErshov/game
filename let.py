import movement
from consts import ground_height
import consts


class Let(movement.Movement):
    def __init__(self, color, width, height, x, y, speed=2, direction=1):
        movement.Movement.__init__(self, x, y, speed, direction, width)
        self.width = width
        self.height = height
        self.color = color
        self.collision = False

    def set_collision(self, flag):
        self.collision = flag


class Triangles(Let):
    def __init__(self, x, y, count):
        Let.__init__(self, (104, 160, 245), 20, 20, x, y)
        self.type = consts.triangle
        self.count = count


class Landscapes(Let):
    def __init__(self, widh, height, x, y):
        Let.__init__(self, (104, 160, 245), widh, height, x, y)
        self.type = consts.landscape
