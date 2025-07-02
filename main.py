import pygame, sys, random

def ball_function():
    # moving the ball
    global ball_speed_x, ball_speed_y
    ball.x += ball_speed_x
    ball.y += ball_speed_y
    if ball.top <= 0 or ball.bottom >= SCREEN_HEIGHT:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= SCREEN_WIDTH:
        ball_restart()
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1

def player_animation():
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= SCREEN_HEIGHT:
        player.bottom = SCREEN_HEIGHT

def opponent_animation():
    if opponent.top < ball.y:
        opponent.top += opp_speed
    if opponent.bottom > ball.y:
        opponent.top -= opp_speed

def ball_restart():
    global ball_speed_x, ball_speed_y
    ball.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    ball_speed_y *= random.choice((1, -1))
    ball_speed_x *= random.choice((1, -1))




#general setup
pygame.init()
clock = pygame.time.Clock()


# setting up main window
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 960
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pong")

# game rectangles
ball = pygame.Rect(SCREEN_WIDTH/2 - 15, SCREEN_HEIGHT/2 -15, 30, 30)
player = pygame.Rect(SCREEN_WIDTH - 20, SCREEN_HEIGHT/2 -70, 10, 140)
opponent = pygame.Rect(10, SCREEN_HEIGHT/2 -70, 10, 140)

# colors
bg_color = (54, 32, 110)
paddle_color = (183, 121, 133)
white_color = (230, 232, 223)

# speed variables
ball_speed_x = 7
ball_speed_y = 7
player_speed = 0
opp_speed = 7

while True:
    #handling input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 7
            if event.key == pygame.K_UP:
                player_speed -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 7
            if event.key == pygame.K_UP:
                player_speed += 7

    ball_function()
    player_animation()
    opponent_animation()

    # visuals
    screen.fill(bg_color)
    pygame.draw.rect(screen, paddle_color, player)
    pygame.draw.rect(screen, paddle_color, opponent)
    # turns your rectangle to an ellipse, but since all sides are the same, it'll be a circle
    pygame.draw.ellipse(screen, white_color, ball)
    pygame.draw.aaline(screen, white_color, (SCREEN_WIDTH/2, 0), (SCREEN_WIDTH/2, SCREEN_HEIGHT))

    # updating window
    pygame.display.flip()
    clock.tick(60)
