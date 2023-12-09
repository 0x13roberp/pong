import pygame

pygame.init()

WIDTH, HEIGHT = 1000, 600

# window
wn = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("pong rober")
run = True

# colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# for the ball
radius = 15
ball_x = WIDTH / 2 - radius
ball_y = HEIGHT / 2 - radius
ball_vel_x = 0.7
ball_vel_y = 0.7

# paddle dimentions
paddle_width = 20
paddle_height = 120

left_paddle_y = HEIGHT / 2 - paddle_height / 2
right_paddle_y = HEIGHT / 2 - paddle_height / 2

left_paddle_x = 100 - paddle_width / 2
right_paddle_x = WIDTH - (100 - paddle_width / 2)

right_paddle_vel = 0
left_paddle_vel = 0

# main loop
while run:
    wn.fill(BLACK) # don't leave trails the ball
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False

        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_UP:
                right_paddle_vel = -0.9
            if i.key == pygame.K_DOWN:
                right_paddle_vel = 0.9
            if i.key == pygame.K_w:
                left_paddle_vel = -0.9
            if i.key == pygame.K_s:
                left_paddle_vel = 0.9

        if i.type == pygame.KEYUP:
            right_paddle_vel = 0
            left_paddle_vel = 0

    #movements
    ball_x += ball_vel_x
    ball_y += ball_vel_y
    right_paddle_y += right_paddle_vel
    left_paddle_y += left_paddle_vel

    # collisions
    # left paddle
    if left_paddle_x <= ball_x <= left_paddle_x + paddle_width:
        if left_paddle_y <= ball_y <= left_paddle_y + paddle_height:
            ball_x = left_paddle_x + paddle_width
            ball_vel_x *= -1

    # right paddle
    if right_paddle_x <= ball_x <= right_paddle_x + paddle_width:
        if right_paddle_y <= ball_y <= right_paddle_y + paddle_height:
            ball_x = right_paddle_x
            ball_vel_x *= -1

    # ball's movement controls
    if ball_y <= 0 + radius or ball_y >= HEIGHT - radius: # if the ball hits the floor
        ball_vel_y *= -1 # bounce

    # if the paddles goes out the screen
    if left_paddle_y >= HEIGHT - paddle_height:
        left_paddle_y = HEIGHT - paddle_height
    if left_paddle_y <= 0:
        left_paddle_y = 0
    if right_paddle_y >= HEIGHT - paddle_height:
        right_paddle_y = HEIGHT - paddle_height
    if right_paddle_y <= 0:
        right_paddle_y = 0

    if ball_x >= WIDTH - radius: # if the ball goes out, start again from the center
        ball_x = WIDTH / 2 - radius
        ball_y = HEIGHT / 2 - radius
        ball_vel_x *= -1
        ball_vel_y *= -1

    if ball_x <= 0 + radius:
        ball_x = WIDTH / 2 - radius
        ball_y = HEIGHT / 2 - radius
        ball_vel_x = 0.7
        ball_vel_y = 0.7


    pygame.draw.circle(wn, BLUE, (ball_x, ball_y), radius)
    pygame.draw.rect(wn, RED,pygame.Rect(left_paddle_x, left_paddle_y, paddle_width, paddle_height))
    pygame.draw.rect(wn, RED,pygame.Rect(right_paddle_x, right_paddle_y, paddle_width, paddle_height))
    pygame.display.update() # show the ball in the window