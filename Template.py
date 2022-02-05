# Quick starter template for any pygame project
import pygame
pygame.init()

# Variables
size = width, height = 1280, 720
speed = [2, 2]
white = (255, 255, 255)
carryOn = True

screen = pygame.display.set_mode(size) # Size of the screen
clock = pygame.time.Clock() # Creates an object to help track time

# Game loop
while carryOn:

    for event in pygame.event.get(): # Detects events
        if event.type == pygame.QUIT: pygame.quit() # Shut down

    screen.fill(white) # Background color
    pygame.display.flip() # Update full display Surface to screen

    clock.tick(60) # 60fps limiter
