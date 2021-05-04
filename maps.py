import let
from consts import display_width, display_height, ground_height

start_point = display_width + 1000
start_y = display_height - ground_height


def generate_map1():
    map1 = [
        let.Ground(display_width, 20, 0,start_y),
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

    last = len(map1)-1

    def win_line():
        return map1[last].x + map1[last].width

    return (map1, win_line)


all_maps = [
    generate_map1
]
