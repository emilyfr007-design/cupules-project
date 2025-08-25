import consts
import pygame
import solider_module

# def draw_game(game_state):
#     screen.fill(consts.BACKGROUND_COLOR)
#     draw_arrow(game_state["rotated_arrow"])
#
#
#
#     if len(game_state["bubbles_popping"]):
#         BubblesGrid.animate_bubbles_pop(game_state["bubbles_popping"])
#         draw_bubbles_popping(game_state["bubbles_popping"])
#
#     elif game_state["state"] == consts.LOSE_STATE:
#         draw_lose_message()
#
#     elif game_state["state"] == consts.WIN_STATE:
#         draw_win_message()
#
#     pygame.display.flip()



background_colour = consts.BACKGROUND_COLOR


screen = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))


pygame.display.set_caption('Geeksforgeeks')


screen.fill(background_colour)

solider_module.create_solider(consts.SOLIDER_IMAGE)

pygame.display.flip()


running = True


while running:


    for event in pygame.event.get():


        if event.type == pygame.QUIT:
            running = False



