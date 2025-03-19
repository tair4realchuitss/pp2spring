import pygame
import sys
import datetime 

pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
center_x, center_y = width // 2, height // 2

pygame.display.set_caption("часики")

clock = pygame.time.Clock()

min_hand = pygame.image.load("min_hand.png")
sec_hand = pygame.image.load("sec_hand.png")
mickey = pygame.image.load("clock.png")


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    currrent_time = datetime.datetime.now()

    sec_angle = -round(currrent_time.second) * 6 
    min_angle = -currrent_time.minute * 6 

    
    rotR = pygame.transform.rotate(min_hand,min_angle)
    rotL = pygame.transform.rotate(sec_hand,sec_angle)

    screen.blit(mickey,(0,0))
    screen.blit(rotR, rotR.get_rect(center=(center_x, center_y)))
    screen.blit(rotL, rotL.get_rect(center=(center_x, center_y)))



    
    
    
    clock.tick(60)
    pygame.display.flip()