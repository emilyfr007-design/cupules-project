import pygame
import consts
import screen


def create_solider():
    solider = pygame.image.load("solider_img.png")
    solider_img_size = pygame.transform.scale(solider, (consts.SOLIDER_WIDTH, consts.SOLIDER_HEIGHT))
    display = screen.screen.blit(solider_img_size, (0, 0))

    return display





def move_up():
    pass


def move_down():
    pass


def move_left():
    pass



def move_right():
    pass