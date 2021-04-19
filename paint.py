import pygame
import random

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
 

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

game_over = False

prev, cur = None, None
screen.fill(BLACK)
color = (5, 5, 5)


while not game_over:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      game_over = True
    #if event.type == pygame.K_r:
        #color = RED
    #if event.type == pygame.K_g:
        #color = GREEN
    #if event.type == pygame.K_b:
        #color = BLUE
    #if event.type == pygame.K_w:
        #color = WHITE
    if event.type == pygame.MOUSEBUTTONDOWN:
      prev = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEMOTION:
      cur = pygame.mouse.get_pos()
      if prev:
        pygame.draw.line(screen, RED, prev, cur, 1)
        prev = cur
    if event.type == pygame.MOUSEBUTTONUP:
      prev = None

    if prev:
     pygame.draw.circle(screen, RED, prev, 10)
    if event.type == pygame.K_c:
        if event.type == pygame.MOUSEMOTION:
            pygame.draw.line(screen, BLACK, prev, cur, 1)
    
    
    

  

  pygame.display.flip()

  clock.tick(30)


pygame.quit()