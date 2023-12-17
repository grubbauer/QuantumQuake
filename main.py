# Initialise temporary values
tmp = 1

# Importing the librarys
import os
import sys
import time
import pygame
import pygame.mixer as mixer 
import logging
from colorlog import ColoredFormatter

# Initialising the programms
pygame.init()
mixer.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("The New Era")

# Setting up constants
WHITE = (255, 255, 255)
WIDTH, HEIGHT = pygame.display.Info().current_w, pygame.display.Info().current_h
# Setting up variables
movingright = False  
movingleft = False
movingup = False
movingdown = False
playerx = WIDTH // 2
playery = HEIGHT // 1.5



# Configure logging settings
logging.basicConfig(filename='resources/log/BlockBuster.log', level=logging.DEBUG, format='%(log_color)s[%(asctime)s]%(reset)s - [%(levelname)s] - [%(message)s]')

# Create a console handler and set the level to DEBUG
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

# Create a colored formatter with date and level colored appropriately, and add it to the console handler
formatter = ColoredFormatter(
    '%(purple)s[%(asctime)s]%(reset)s - %[(log_color)s%(levelname)s%(reset)s] - [%(message)s]',
    datefmt='%d-%m-%Y %H:%M:%S',
    log_colors={
        'DEBUG': 'cyan',
        'INFO': 'green',
        'WARNING': 'yellow',
        'ERROR': 'red',
        'CRITICAL': 'bold_red'
    },
    
)

console_handler.setFormatter(formatter)

# Add the console handler to the root logger
logging.getLogger().addHandler(console_handler)

# Debug elements
logging.debug("WindowsHeight: WIDTH:%s, HEIGHT:%s", WIDTH, HEIGHT)

# Adding the img and audio files
playertexture = pygame.image.load("resources/sprites/player/Sprite-0001-test.png")
playertexture = pygame.transform.scale(playertexture, (128, 128)) 
background = pygame.image.load("resources/sprites/background/Sprite-0001-test.png")
background = pygame.transform.scale(background,(WIDTH, HEIGHT)) 
bricktext = pygame.image.load("resources/sprites/brick/Sprite-0001-test.png")
basesetuptext = pygame.image.load("resources/sprites/background/Sprite-0003-test.png")
startbutton = pygame.image.load("resources/sprites/buttons/Sprite-0001-test.png")
mixer.music.load("resources/audio/mainms.wav")

# The CLOCK
clock = pygame.time.Clock()

# Setting up the BRICK
tmp = 10
brick_positions = [((tmp * 10)*i+(-50), 5) for i in range(1, 21)]
box_down = [False for _ in range(1, 21)]

paddle_width = 150
paddle_height = 20


# Setting up the ball
ball_radius = 20
ball_color = (255, 0, 0)  # Red.

ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_speed_x = 10
ball_speed_y = 10

logotime = True
if logotime:
        screen.fill(WHITE)
        screen.blit(basesetuptext, (0, 0))
        pygame.display.flip()
        time.sleep(1.5)
        pygame.display.flip()
        startbutton_rect = pygame.Rect(150, 50, 512, 512)
        screen.blit(startbutton, startbutton_rect.topleft)
        pygame.display.flip()

        while logotime:
            for event in pygame.event.get():

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if startbutton_rect.collidepoint(event.pos):
                        logotime = False
                elif event.type == pygame.KEYDOWN:
                    logotime = False




running = True
while running:
    # Checking for event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Condition Loop 
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                movingright = True
            elif event.key == pygame.K_a:
                movingleft = True    
            elif event.key == pygame.K_ESCAPE:
                running = False
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                movingright = False
            elif event.key == pygame.K_a:
                movingleft = False 
            

    if movingright:
        playerx += 10
    if movingleft:
        playerx -= 10

    # Update ball position
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Bounce off the walls
    if ball_x - ball_radius < 0 or ball_x + ball_radius > WIDTH:
        ball_speed_x = -ball_speed_x
    if ball_y - ball_radius < 0 or ball_y + ball_radius > HEIGHT:
        ball_speed_y = -ball_speed_y
    if ball_y + ball_radius > HEIGHT:  # Check if the ball touches the ground
            running = False

    # Check collision with player (paddle)
    paddle_rect = pygame.Rect(playerx, playery, paddle_width, paddle_height)
    if paddle_rect.colliderect((ball_x - ball_radius, ball_y - ball_radius, 2 * ball_radius, 2 * ball_radius)):
        ball_speed_y = -ball_speed_y

    # Check collision with bricks
    for i in range(20):
        if not box_down[i]:
            brick_rect = pygame.Rect(brick_positions[i][0], brick_positions[i][1], tmp * 10, 5)
            if brick_rect.colliderect((ball_x - ball_radius, ball_y - ball_radius, 2 * ball_radius, 2 * ball_radius)):
                ball_speed_y = -ball_speed_y
                box_down[i] = True

    # Blitting
    screen.blit(background, (0, 0))
    screen.blit(playertexture, (playerx, playery))

    for i in range(20):
        if not box_down[i]:
            screen.blit(bricktext, brick_positions[i])

    pygame.draw.circle(screen, ball_color, (ball_x, ball_y), ball_radius)

    # Refreshing
    pygame.display.flip()
    clock.tick(120)