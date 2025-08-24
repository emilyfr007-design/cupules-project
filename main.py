import pygame
import game_field
import solider
import consts
import screen


state = {
    "is_window_open": True,
    "state": consts.RUNNING_STATE,

}




def main():
    pygame.init()
    game_field.create_matrix()


    while state["is_window_open"]:

        handle_user_events()

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
            solider.move_up()

        elif event.type == pygame.K_DOWN:
            solider.move_down()

        elif event.type == pygame.K_LEFT:
            solider.move_left()

        elif event.type == pygame.K_RIGHT:
            solider.move_right()


def is_lose():
    pass


def is_win():
    pass