import pygame
import game_field
import solider_module
import consts
import screen
from solider_module import create_solider

state = {
    "original_solider": solider_module.create_solider(consts.SOLIDER_IMAGE),
    "is_window_open": True,
    "state": consts.RUNNING_STATE,
}

def main():
    pygame.init()
    game_field.create_matrix()


    while state["is_window_open"]:

    if is_lose():
        state["state"] = consts.LOSE_STATE
    elif is_win():
        state["state"] = consts.WIN_STATE


    screen.draw_game(state)









def handle_user_events():
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            state["is_window_open"] = False

        elif state["state"] != consts.RUNNING_STATE:
            continue

        if event.type == pygame.K_UP:
            solider_module.move_up()

        elif event.type == pygame.K_DOWN:
            solider_module.move_down()

        elif event.type == pygame.K_LEFT:
            solider_module.move_left()

        elif event.type == pygame.K_RIGHT:
            solider_module.move_right()

        elif event.type == pygame.K_KP_ENTER:
            game_field.show_trap()





def is_lose():
    pass


def is_win():
    pass