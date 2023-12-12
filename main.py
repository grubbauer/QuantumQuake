# Importing the librarys
import os
import sys
import pygame
import pygame.mixer as mixer 

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
playery = HEIGHT // 2

# Debug elements
debug = []
debug.append(f"WINDOW: {WIDTH, HEIGHT}")

# Adding the img and audio files
playertexture = pygame.image.load("resources/sprites/player/Sprite-0001-test.png")
playertexture = pygame.transform.scale(playertexture, (128, 128)) 
background = pygame.image.load("resources/sprites/background/Sprite-0001-test.png")
background = pygame.transform.scale(background,(WIDTH, HEIGHT)) 
mixer.music.load("resources/audio/mainms.wav")

# The CLOCK
clock = pygame.time.Clock()


running = True
while running:
    # Checking for event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            print(f"DEBUG: {debug}")
        # Condition Loop 
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                moving_right = True
            elif event.key == pygame.K_a:
                moving_left = True    
            elif event.key == pygame.K_w:
                moving_up = True
            elif event.key == pygame.K_s:
                moving_down = True
            elif event.key == pygame.K_ESCAPE:
                running = False
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                moving_right = False
            elif event.key == pygame.K_a:
                moving_left = False 
            elif event.key == pygame.K_w:
                moving_up = False
            elif event.key == pygame.K_s:
                moving_down = False

    if movingright:
        playerx += 10  
    if movingleft:
        playerx -= 10
    if movingup:
        playery -= 10
    if movingdown:
        playery += 10

    # Blitting
    screen.blit(background, (0,0)) 
    screen.blit(playertexture, (playerx, playery))

    # Refreshing
    pygame.display.flip()
    clock.tick(120) 
    
pygame.quit()
sys.exit()