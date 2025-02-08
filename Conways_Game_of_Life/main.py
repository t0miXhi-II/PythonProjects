import pygame  # Note: Pygame is a 2-dimensional library for game development

pygame.init()

BLACK = (0, 0, 0)
GREY = (128, 128, 128)
YELLOW = (255, 255, 0)

WIDTH, HEIGHT = 800, 800
TILE_SIZE = 20
GRID_WIDTH = WIDTH // TILE_SIZE
GRID_HEIGHT = HEIGHT //TILE_SIZE

FPS = 60 # Frame per second

screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

def main():  # code to run constantly
    running = True 

    while running:
        clock.tick(FPS) # run for a maximum of the FPS

        for event in pygame.event.get()
            if event.type == pygame.QUIT:
                