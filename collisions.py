import consts


def check_collisions(user, barriers):
    collision = False
    for barrier in barriers:
        if barrier.type == consts.landscape or barrier.type == consts.asteroid:
            check_landscape_collision(user, barrier)
        else:
            collision = collision or check_let_collision(user, barrier)

    return collision


def check_landscape_collision(user, barrier):
    count = 1
    try:
        count = barrier.count
    except:
        count = 1
    if user.x > barrier.x - user.width and user.x + user.width < barrier.x + barrier.width * count + user.width:
        if not barrier.collision:
            if barrier.y + barrier.height - consts.delta <= user.y <= barrier.y + barrier.height:
                user.set_jump(user.start_jump_y - barrier.y - barrier.height )
                barrier.set_collision(True)
            if barrier.y <= user.y + user.height <= barrier.y + consts.delta + 7:
                if barrier.x + barrier.width * count - consts.delta <= user.x <= barrier.x + barrier.width * count + user.width\
                        or barrier.x - user.width <= user.x <= barrier.x - user.width + consts.delta:
                    user.set_fall(consts.display_height - consts.ground_height - user.height - user.y)
                    barrier.set_collision(True)
                else:
                    user.stand(barrier.y - user.height)
                    user.set_jump(user.start_jump_y - barrier.y - barrier.height)
                    user.stop_fall()
        if barrier.y <= user.y <= barrier.y + barrier.height - consts.delta \
                or barrier.y + consts.delta <= user.y + user.height <= barrier.y + barrier.height \
                or user.y <= barrier.y and user.y + user.height >= barrier.y + barrier.height:
            user.ram(barrier.speed)
            barrier.set_collision(True)
        if user.start_jump_y == user.y and not user.make_fall:
            barrier.set_collision(False)
        if user.x >= barrier.x - user.width + consts.delta and user.x + user.width < barrier.x + barrier.width + user.width:
            if barrier.y <= user.y + user.height <= barrier.y + consts.delta:
                barrier.set_collision(False)
    else:
         if barrier.collision:
            barrier.set_collision(False)

    return False


def check_let_collision(user, barrier):
    count = 1
    try:
        count = barrier.count
    except:
        count = 1
    if user.x > barrier.x - user.width and user.x + user.width < barrier.x + barrier.width * count + user.width:
        if barrier.y <= user.y <= barrier.y + barrier.height \
                or barrier.y <= user.y + user.height <= barrier.y + barrier.height\
                or user.y + user.height >= barrier.y + barrier.height and user.y <= barrier.y:
            return True
    return False

