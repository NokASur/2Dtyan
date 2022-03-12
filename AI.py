from characteristics import *
from math import ceil


def sue_ai(p_x, p_y, b_x, b_y, speed):
    dif_x = p_x - b_x
    dif_y = p_y - b_y
    x_c = 0
    y_c = 0
    if dif_x < 0:
        x_c = -speed
    elif dif_x > 0:
        x_c = speed
    if dif_y < 0:
        y_c = -speed
    elif dif_y > 0:
        y_c = speed
    return x_c, y_c


def move_calculate(enemy_type, player_x, player_y, bot_x, bot_y):
    x_change, y_change = 0, 0
    if enemy_stat[enemy_type]["intelligence"] == "straight_up_engagement":
        x_change, y_change = sue_ai(player_x, player_y, bot_x, bot_y, enemy_stat[enemy_type]["speed"])
    # elif enemy_stat[enemy_type]["intelligence"] == "distancing":
    #     x_change, y_change = dist_ai(player_x, player_y, bot_x, bot_y)
    # elif enemy_stat[enemy_type]["intelligence"] == "avoiding":
    #     x_change, y_change = avoid_calc_ai(player_x, player_y, bot_x, bot_y)
    return x_change, y_change
