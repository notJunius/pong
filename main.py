import pygame, sys

#general setup
pygame.init()
clock = pygame.time.Clock()


# setting up main window
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pong")

# game rectangles
ball = pygame.Rect(SCREEN_WIDTH/2 - 15, SCREEN_HEIGHT/2 -15, 30, 30)
player = pygame.Rect(SCREEN_WIDTH - 20, SCREEN_HEIGHT/2 -70, 10, 140)
opponent = pygame.Rect(10, SCREEN_HEIGHT/2 -70, 10, 140)


while True:
    #handling input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # updating window
    pygame.display.flip()
    clock.tick(60)
