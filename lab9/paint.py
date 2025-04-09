import pygame
import math

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

# Drawing settings
radius = 10
mode = 'blue'   # Default color
shape = 'free'  # Default shape
points = []
drawing = False
start_pos = None

# Main loop flag
running = True
while running:
    pressed = pygame.key.get_pressed()
    alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
    ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            # Exit combinations
            if event.key == pygame.K_w and ctrl_held:
                running = False
            if event.key == pygame.K_F4 and alt_held:
                running = False
            if event.key == pygame.K_ESCAPE:
                running = False

            # Color selection
            if event.key == pygame.K_r:
                mode = 'red'
            elif event.key == pygame.K_g:
                mode = 'green'
            elif event.key == pygame.K_b:
                mode = 'blue'
            elif event.key == pygame.K_y:
                mode = 'yellow'
            elif event.key == pygame.K_k:
                mode = 'black'
            elif event.key == pygame.K_w:
                mode = 'white'

            # Shape selection
            if event.key == pygame.K_e:
                shape = 'eraser'
            elif event.key == pygame.K_f:
                shape = 'free'
            elif event.key == pygame.K_c:
                shape = 'circle'
            elif event.key == pygame.K_t:
                shape = 'rect'
            elif event.key == pygame.K_s:
                shape = 'square'
            elif event.key == pygame.K_q:
                shape = 'right_triangle'
            elif event.key == pygame.K_a:
                shape = 'equilateral_triangle'
            elif event.key == pygame.K_d:
                shape = 'rhombus'

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                drawing = True
                start_pos = event.pos
            elif event.button == 3:
                radius = max(1, radius - 1)

        if event.type == pygame.MOUSEWHEEL:
            if event.y > 0:
                radius = min(200, radius + 2)
            elif event.y < 0:
                radius = max(1, radius - 2)

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                drawing = False
                end_pos = event.pos

                # Shape rendering
                if shape == 'circle':
                    center = ((start_pos[0] + end_pos[0]) // 2, (start_pos[1] + end_pos[1]) // 2)
                    rad = max(abs(end_pos[0] - start_pos[0]) // 2, abs(end_pos[1] - start_pos[1]) // 2)
                    pygame.draw.circle(screen, mode, center, rad, 2)

                elif shape == 'rect':
                    rect = pygame.Rect(start_pos, (end_pos[0] - start_pos[0], end_pos[1] - start_pos[1]))
                    pygame.draw.rect(screen, mode, rect, 2)

                elif shape == 'square':
                    size = min(abs(end_pos[0] - start_pos[0]), abs(end_pos[1] - start_pos[1]))
                    top_left = (start_pos[0], start_pos[1])
                    pygame.draw.rect(screen, mode, (top_left[0], top_left[1], size, size), 2)

                elif shape == 'right_triangle':
                    pygame.draw.polygon(screen, mode, [start_pos, (start_pos[0], end_pos[1]), end_pos], 2)

                elif shape == 'equilateral_triangle':
                    side = abs(end_pos[0] - start_pos[0])
                    height = side * math.sqrt(3) / 2
                    top = (start_pos[0] + side / 2, start_pos[1])
                    left = (start_pos[0], start_pos[1] + height)
                    right = (start_pos[0] + side, start_pos[1] + height)
                    pygame.draw.polygon(screen, mode, [top, left, right], 2)

                elif shape == 'rhombus':
                    mid_x = (start_pos[0] + end_pos[0]) // 2
                    mid_y = (start_pos[1] + end_pos[1]) // 2
                    dx = abs(end_pos[0] - start_pos[0]) // 2
                    dy = abs(end_pos[1] - start_pos[1]) // 2
                    points = [
                        (mid_x, start_pos[1]),
                        (end_pos[0], mid_y),
                        (mid_x, end_pos[1]),
                        (start_pos[0], mid_y)
                    ]
                    pygame.draw.polygon(screen, mode, points, 2)

        if event.type == pygame.MOUSEMOTION and drawing:
            if shape == 'free':
                pygame.draw.circle(screen, mode, event.pos, radius)
            elif shape == 'eraser':
                pygame.draw.circle(screen, (0, 0, 0), event.pos, radius)

    pygame.display.flip()
    clock.tick(60)

# Quit pygame
pygame.quit()
