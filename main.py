import pygame
import random
import time

square_size = 20
def create_screen():
    screen_squares = []
    bomb_counter = 0
    for i in range (50):
        screen_squares.append([])
        for j in range(25):
            screen_squares[i].append([pygame.Rect(i*square_size, j*square_size, square_size, square_size), False])
    while bomb_counter <20:
        x = random.randint(0, 49)
        y = random.randint(0, 24)
        if not screen_squares[x][y][1]:
            bomb_counter += 1
            screen_squares[x][y][1] = True

    return screen_squares


def mine():
    mine_image = pygame.image.load('mine.png').convert()
    mine_image = pygame.transform.scale(mine_image, (square_size * 3, square_size * 1))
    return mine_image



def draw_screen(surface, screen_squares):
    for i in range(len(screen_squares)):
        for j in range(len(screen_squares[i])):
            pygame.draw.rect(surface, (0, 128, 0), screen_squares[i][j][0], 1)


def main():
    pygame.init()
    surface = pygame.display.set_mode((1000, 500))  # window
    screen_squares = create_screen()
    person_image = pygame.image.load('person.jpg').convert()
    person_image = pygame.transform.scale(person_image, (square_size*2, square_size*2))
    person_location = [0, 0]
    enter_pressed = False
    while True:
        surface.fill((0, 128, 0))
        draw_screen(surface, screen_squares)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    person_location[0] += square_size
                if event.key == pygame.K_LEFT:
                    person_location[0] -= square_size
                if event.key == pygame.K_UP:
                    person_location[1] -= square_size
                if event.key == pygame.K_DOWN:
                    person_location[1] += square_size
                if event.key == pygame.K_RETURN:
                    enter_pressed = True
                    surface.fill((0, 0, 0))
                    for i in range(len(screen_squares)):
                        for j in range(len(screen_squares[i])):
                            if screen_squares[i][j][1]:
                                pygame.draw.rect(surface, (255, 0, 0), screen_squares[i][j][0])

                                for row in range(len(screen_squares)):
                                    for col in range(len(screen_squares[row])):
                                        surface.blit(mine(),(i,j))




        surface.blit(person_image, (person_location[0], person_location[1]))
        pygame.display.flip()

        if enter_pressed:
            time.sleep(1)
            enter_pressed = False

    pygame.quit()

if __name__ == "__main__":
    main()