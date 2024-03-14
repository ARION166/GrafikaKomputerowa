import pygame

pygame.init()

WIDTH, HEIGHT = 600, 600
BACKGROUND_COLOR = (255, 255, 255)
LINE_COLOR = (255, 0, 0)
LINE_WIDTH = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BACKGROUND_COLOR)

    pygame.draw.line(screen, LINE_COLOR, (100, 100), (500, 100), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (500, 100), (100, 500), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (100, 500), (500, 500), LINE_WIDTH)

    pygame.display.flip()

pygame.quit()