import pygame

# Инициализация Pygame
pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()


radius = 10
mode = 'blue'  # Цвет по умолчанию
shape = 'free'  # Режим рисования
points = []
drawing = False
start_pos = None

# Основной цикл
running = True
while running:
    pressed = pygame.key.get_pressed()
    alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
    ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and ctrl_held:
                running = False
            if event.key == pygame.K_F4 and alt_held:
                running = False
            if event.key == pygame.K_ESCAPE:
                running = False
            
            # Выбор цвета
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
                
            # Выбор инструмента
            if event.key == pygame.K_e:
                shape = 'eraser'
            elif event.key == pygame.K_f:
                shape = 'free'
            elif event.key == pygame.K_c:
                shape = 'circle'
            elif event.key == pygame.K_t:
                shape = 'rect'
                
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # ЛКМ - рисование
                drawing = True
                start_pos = event.pos
            elif event.button == 3:  # ПКМ - изменение радиуса
                radius = max(1, radius - 1)
        if event.type == pygame.MOUSEWHEEL:
            if event.y > 0:  # Прокрутка вверх — увеличиваем радиус
                radius = min(200, radius + 2)
            elif event.y < 0:  # Прокрутка вниз — уменьшаем радиус
                radius = max(1, radius - 2)
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                drawing = False
                if shape in ['circle', 'rect']:
                    end_pos = event.pos
                    
                    if shape == 'circle':
                        center = ((start_pos[0] + end_pos[0]) // 2, (start_pos[1] + end_pos[1]) // 2)
                        rad = max(abs(end_pos[0] - start_pos[0]) // 2, abs(end_pos[1] - start_pos[1]) // 2)
                        pygame.draw.circle(screen, mode, center, rad, 2)
                    elif shape == 'rect':
                        rect = pygame.Rect(start_pos, (end_pos[0] - start_pos[0], end_pos[1] - start_pos[1]))
                        pygame.draw.rect(screen, mode, rect, 2)
                    
        if event.type == pygame.MOUSEMOTION and drawing:
            if shape == 'free':
                pygame.draw.circle(screen, mode, event.pos, radius)
            elif shape == 'eraser':
                pygame.draw.circle(screen, (0, 0, 0), event.pos, radius)
                
    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()
