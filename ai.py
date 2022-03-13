from characteristics import *
from math import ceil, sin, sqrt


def no_wall_hitting_module(dif_x, dif_y, abs_dif, b_x, b_y, speed):
    if W <= b_x or b_x <= 0:
        if -speed * dif_y / max(abs_dif, 1) < 0:
            return 0, -speed * dif_y / max(abs_dif, 1) - abs(-speed * dif_x / max(abs_dif, 1))
        else:
            return 0, -speed * dif_y / max(abs_dif, 1) + abs(-speed * dif_x / max(abs_dif, 1))
    elif H <= b_y or b_y <= 0:
        if -speed * dif_x / max(abs_dif, 1) < 0:
            return -speed * dif_x / max(abs_dif, 1) - abs(-speed * dif_y / max(abs_dif, 1)), 0
        else:
            return -speed * dif_x / max(abs_dif, 1) + abs(-speed * dif_y / max(abs_dif, 1)), 0


def sue_ai(p_x, p_y, b_x, b_y, speed):
    dif_x = p_x - b_x
    dif_y = p_y - b_y
    abs_dif = sqrt(dif_x ** 2 + dif_y ** 2)
    return speed * dif_x / max(abs_dif, 1), speed * dif_y / max(abs_dif, 1)


def dist_ai(p_x, p_y, b_x, b_y, speed, rangee):
    dif_x = p_x - b_x
    dif_y = p_y - b_y
    abs_dif = sqrt(dif_x ** 2 + dif_y ** 2)
    if abs_dif < rangee:
        # if min(b_x, W - b_x) + min(b_y, H - b_y) < 100:
        #     return 0, 0  # Доделать буст режим в углу
        if W > b_x > 0 and H > b_y > 0:
            return -speed * dif_x / max(abs_dif, 1), -speed * dif_y / max(abs_dif, 1)
        else:
            return no_wall_hitting_module(dif_x, dif_y, abs_dif, b_x, b_y, speed)

    else:
        return speed * dif_x / max(abs_dif, 1), speed * dif_y / max(abs_dif, 1)


def avoid_ai(p_x, p_y, b_x, b_y, speed):
    dif_x = p_x - b_x
    dif_y = p_y - b_y
    abs_dif = sqrt(dif_x ** 2 + dif_y ** 2)
    if W > b_x > 0 and H > b_y > 0:
        return -speed * dif_x / max(abs_dif, 1), -speed * dif_y / max(abs_dif, 1)
    else:
        return no_wall_hitting_module(dif_x, dif_y, abs_dif, b_x, b_y, speed)


def move_calculate(enemy_type, player_x, player_y, bot_x, bot_y):
    x_change, y_change = 0, 0
    if enemy_stat[enemy_type]["intelligence"] == "straight_up_engagement":
        x_change, y_change = sue_ai(player_x, player_y, bot_x, bot_y, enemy_stat[enemy_type]["speed"])
    elif enemy_stat[enemy_type]["intelligence"] == "distancing":
        x_change, y_change = dist_ai(player_x, player_y, bot_x, bot_y, enemy_stat[enemy_type]["speed"],
                                     enemy_stat[enemy_type]["range"])
    elif enemy_stat[enemy_type]["intelligence"] == "avoiding":
        x_change, y_change = avoid_ai(player_x, player_y, bot_x, bot_y, enemy_stat[enemy_type]["speed"],
                                      enemy_stat[enemy_type]["range"])
    return x_change, y_change
