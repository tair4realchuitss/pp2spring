import pygame
import sys

pygame.init()

red = (255, 0, 0)
white = (255, 255, 255)
speed = 20
radius = 25
width, height = 680, 500
screen = pygame.display.set_mode((width, height))
ball_pos = [500, 250]
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                ball_pos[0] = max(ball_pos[0]-speed,radius)
            if event.key == pygame.K_RIGHT:
                ball_pos[0] = min(ball_pos[0]+speed,width-radius)
            if event.key == pygame.K_UP:
                ball_pos[1] = max(ball_pos[1]-speed,radius)
            if event.key == pygame.K_DOWN:
                ball_pos[1] = min(ball_pos[1]+speed,height-radius)
    screen.fill(white)

    
    pygame.draw.circle(screen, red, ball_pos, 25)  

        
   
    pygame.display.flip()
