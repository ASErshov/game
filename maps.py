import let
from consts import display_width, display_height, ground_height

start_point = display_width + 1000
start_y = display_height - ground_height


def generate_map1():
    map = [
        let.Ground(display_width, 20, 0, start_y),
        let.Triangles(start_point, start_y - 20, 3),
        let.Landscapes(200, 40, start_point + 160, start_y - 70),
        let.Triangles(start_point + 299, start_y - 90, 3),
        let.Landscapes(200, 40, start_point + 300, start_y - 200),
        let.Landscapes(40, 40, start_point + 500, start_y - 300),
        let.Landscapes(40, 40, start_point + 590, start_y - 300),
        let.Landscapes(40, 40, start_point + 680, start_y - 300),
        let.Landscapes(40, 40, start_point + 770, start_y - 350),
        let.Triangles(start_point + 775, start_y - 370, 1),
        let.Triangles(start_point + 600, start_y - 20, 4),
        let.Triangles(start_point + 710, start_y - 20, 4),
        let.Triangles(start_point + 820, start_y - 20, 4),
        let.Triangles(start_point + 930, start_y - 20, 4),
        let.Triangles(start_point + 1040, start_y - 20, 4),
        let.Landscapes(80, 40, start_point + 900, start_y - 200),
        let.Asteroid(30, -2000, start_y - 40, 5, -1),
        let.Asteroid(30, -3000, start_y - 60, 6, -1),
        let.Asteroid(30, -4800, start_y - 260, 6, -1),
        let.Laser(10, start_point + 7000, start_y - 50, 7, 1),
        let.Laser(10, start_point + 6800, start_y - 50, 7, 1),
        let.Landscapes(400, 40, start_point + 1100, start_y - 100),
        let.Landscapes(400, 40, start_point + 1570, start_y - 100),
        let.Landscapes(800, 40, start_point + 1200, start_y - 225),
    ]

    last = len(map)-1

    def win_line():
        return map[last].x + map[last].width

    return (map, win_line)

def generate_map2():
    map = [
        let.Ground(display_width, 20, 0, start_y),
        let.Asteroid(30, start_point + 3000, start_y - 60, 10, 1),
        let.Asteroid(30,  -8500, start_y - 260, 8, -1),
        let.Triangles(start_point + 700, start_y - 20, 5),
        let.Landscapes(40, 40, start_point + 700, start_y - 100),
        let.Landscapes(40, 40, start_point + 770, start_y - 150),
        let.Landscapes(40, 40, start_point + 840, start_y - 200),
        let.Landscapes(200, 40, start_point + 910, start_y - 250),
        let.Laser(10, start_point + 7900, start_y - 150, 10, 1),
        let.Laser(10, start_point + 7300, start_y - 50, 10, 1),
        let.Laser(10, start_point + 7300, start_y - 50, 10, 1),
        let.Laser(10, start_point + 10300, start_y - 245, 10, 1),
        let.Triangles(start_point + 1200, start_y - 340, 10),
        let.Landscapes(1000, 40, start_point + 1200, start_y - 325),
        let.Landscapes(500, 40, start_point + 1130, start_y - 225),
        let.Triangles(start_point + 2435, start_y - 145, 3),
        let.Triangles(start_point + 2150, start_y - 145, 2),
        let.Landscapes(700, 40, start_point + 1800, start_y - 125),
        let.Landscapes(80, 40, start_point + 2800, start_y - 50),
        let.Landscapes(80, 40, start_point + 2800 + 200, start_y - 125),
        let.Landscapes(80, 40, start_point + 2800 + 400, start_y - 225),
        let.Landscapes(80, 40, start_point + 2800 + 600, start_y - 325),
        let.Landscapes(80, 40, start_point + 2800 + 800, start_y - 425),
        let.Landscapes(80, 40, start_point + 2800 + 1000, start_y - 525),
        let.Landscapes(100, 600, start_point + 2800 + 1200, start_y - 600),
    ]

    last = len(map)-1

    def win_line():
        return map[last].x + map[last].width

    return (map, win_line)


all_maps = [
    generate_map1,
    generate_map2,
]
