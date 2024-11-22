import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Create the screen object
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("My Pygame")

# Set the FPS (frames per second)
clock = pygame.time.Clock()

# Main game loop
while True:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Fill the screen with a color (e.g., light blue)
    screen.fill((173, 216, 230))

    # Update the screen
    pygame.display.flip()

    # Set the frames per second (FPS)
    clock.tick(60)
