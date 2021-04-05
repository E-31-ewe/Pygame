import pygame

import math

pygame.init()

frame = width, height = (800, 600)


screen = pygame.display.set_mode(frame)

pygame.display.set_caption("Trigonometric functions")

font = pygame.font.SysFont('times-new-roman', 20)

run= True

BLACK= (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
PI = math.pi




x_point = ['-3п', ' 5п', '-2п', ' 3п', '-п ', ' п ', ' 0 ', ' п ', ' п ', ' 3п', ' 2п', ' 5п', ' 3п']

x_point1 = ['', '_ __', '', '_ __', '', '_ _', '', '   _', '', '   __', '', '   __', '']

x_point2 = ['', '  2', '', '  2', '', ' 2', '', ' 2', '', '  2', '', '  2', '']

y_point = [' 1.00', ' 0.75', ' 0.50', ' 0.25', ' 0.00', '-0.25', '-0.50', '-0.75', '-1.00']




while run:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            run = False

    screen.fill(WHITE)




    pygame.draw.rect(screen, BLACK, (70, 10, 660, 540), 2) 

    pygame.draw.line(screen, BLACK, (70, 280), (730, 280), 3) 

    pygame.draw.line(screen, BLACK, (400, 10), (400, 550), 3) 

    pygame.draw.line(screen, BLACK, (70, 40), (730, 40)) 

    pygame.draw.line(screen, BLACK, (70, 520), (730, 520))

    pygame.draw.line(screen, BLACK, (100, 10), (100, 550)) 

    pygame.draw.line(screen, BLACK, (700, 10), (700, 550)) 




    pygame.draw.line(screen, RED, (530, 60), (570, 60))

    for i in range(530, 570, 7):

        pygame.draw.line(screen, BLUE, (i, 90), (i + 3, 90))




    for i in range(100, 701, 100):

        if i != 500:

            pygame.draw.line(screen, BLACK, (i, 10), (i, 550))

        else:

            pygame.draw.line(screen, BLACK, (i, 10), (i, 40))

            pygame.draw.line(screen, BLACK, (i, 100), (i, 550))

    for x in range(100, 701, 50):

        pygame.draw.line(screen, BLACK, (x, 10), (x, 30))

        pygame.draw.line(screen, BLACK, (x, 550), (x, 530))

    for x in range(100, 701, 25):

        pygame.draw.line(screen, BLACK, (x, 10), (x, 20))

        pygame.draw.line(screen, BLACK, (x, 550), (x, 540))




    for q in range(40, 521, 60):

        pygame.draw.line(screen, BLACK, (70, q), (730, q))

    for x in range(40, 521, 30):

        pygame.draw.line(screen, BLACK, (70, x), (90, x))

        pygame.draw.line(screen, BLACK, (710, x), (730, x))

    for y in range(40, 521, 15):

        pygame.draw.line(screen, BLACK, (70, y), (80, y))

        pygame.draw.line(screen, BLACK, (720, y), (730, y))




    for q in range(100, 700):

        siny1 = 240 * math.sin((q - 100) / 100 * PI)

        siny2 = 240 * math.sin((q - 99) / 100 * PI)

        pygame.draw.aalines(screen, RED, False, [(q, 280 + siny1), ((q + 1), 280 + siny2)])




    for i in range(100, 700, 3):

        cosy1 = 240 * math.cos((i - 100) / 100 * PI)

        cosy2 = 240 * math.cos((i - 99) / 100 * PI)

        pygame.draw.aalines(screen, BLUE, False, [(i, 280 + cosy1), ((i + 1), 280 + cosy2)])




    screen.blit(font.render('sin(x)', False, BLACK), (475, 45))

    screen.blit(font.render('cos(x)', False, BLACK), (475, 75))

    screen.blit(font.render('X', False, BLACK), (393, 575))




    for x in range(100, 701, 50):

        screen.blit(font.render(x_point[(x - 100) // 50], False, BLACK), (x - 10, 550))

        screen.blit(font.render(x_point1[(x - 100) // 50], False, BLACK), (x - 20, 550))

        screen.blit(font.render(x_point2[(x - 100) // 50], False, BLACK), (x - 10, 570))

    for y in range(40, 521, 60):

        screen.blit(font.render(y_point[(y - 40) // 60], False, BLACK), (25, (y - 10)))




    pygame.display.flip()

pygame.quit()