import pygame

import sys

def run_game():
    # Initialize pygame, settings, and screen object.
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")

    # Set the background color.
    bg_color = (230, 230, 230)

    # Start the main loop for the game.
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            # Redraw the screen, each pass through the loop.
            screen.fill(bg_color)

            # Make the most recently drawn screen visible.
            pygame.display.flip()
run_game()