import pygame, sys
from pygame.locals import *

screen = pygame.display.set_mode((800, 550))

blue = (0, 0, 255)
black = (0, 0, 0)
gray = (197, 197, 197)
green = (0, 255, 0)
red = (255, 0, 0)
yellow = (255, 241, 73)
pink = (249, 57, 255)
purple = (167, 0, 238)
white = (255, 255, 255)


circle_p = pygame.image.load("full-moon.png")
rect_p = pygame.image.load("rect.png")
eraser = pygame.image.load("eraser.png")
button_1 = pygame.transform.scale(rect_p, (100, 100))
button_2 = pygame.transform.scale(circle_p, (100, 100))
rect_rect = pygame.Rect(25, 300, 150, 100)
circle_rect = pygame.Rect(45, 390, 100, 66)
stamp = "paint"
stamp="paint2"
stamp_state = False


pygame.init()
menu_font = pygame.font.Font(None, 34)
menu_font2 = pygame.font.Font(None, 26)
menu_text = menu_font.render("Paint MENU", True, green)
clear_text = menu_font.render("Clear", True, blue)
color_text = menu_font2.render("Choose the color", True, yellow)
save_text= menu_font.render("Save", True, black)
draw = False
brush_size = 5
brush_color = black

menu_rect = pygame.Rect(0, 0, 200, 600)
screen_rect = pygame.Rect(200, 0, 600, 600)

green_rect = pygame.Rect(0, 60, 50, 50)
red_rect = pygame.Rect(50, 60, 50, 50)
blue_rect = pygame.Rect(100, 60, 50, 50)
pink_rect = pygame.Rect(150, 60, 50, 50)
yellow_rect = pygame.Rect(0, 110, 50, 50)
white_rect = pygame.Rect(50, 110, 50, 50)
purple_rect = pygame.Rect(100, 110, 50, 50)
gray_rect = pygame.Rect(150, 110, 50, 50)

clear_rect = pygame.Rect(58, 480, 70, 25)
eraser_rect = pygame.Rect(20, 180, 150, 98)
square=pygame.Rect(0,175, 200, 120)
save_rect=pygame.Rect(58,510,70,25)
save_flag = False
file_number = 1
    
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            draw = True
        if event.type == MOUSEBUTTONUP:
            draw = False

    mouse_pos = pygame.mouse.get_pos()
    if draw == True and mouse_pos[0] > 100 and stamp_state == False:
        pygame.draw.line(screen, brush_color, mouse_pos, mouse_pos, brush_size)
        save_flag = False
    
    mouse_pos = pygame.mouse.get_pos()
    if draw == True and mouse_pos[0] > 100 and stamp == "paint" and stamp_state == True:
        screen.blit(button_1, mouse_pos)
        draw = False
        save_flag = False
    if draw == True:
        if rect_rect.collidepoint(mouse_pos):
            stamp = "paint"
            stamp_state = True
    
    mouse_pos = pygame.mouse.get_pos()
    if draw == True and mouse_pos[0] > 100 and stamp == "paint2" and stamp_state == True:
        screen.blit(button_2, mouse_pos)
        draw = False
        save_flag = False
    if draw == True:
        if circle_rect.collidepoint(mouse_pos):
            stamp = "paint2"
            stamp_state = True

    if draw == True:    
        if red_rect.collidepoint(mouse_pos):
            brush_color = red
            stamp_state = False
        if green_rect.collidepoint(mouse_pos):
            brush_color = green
            stamp_state = False
        if blue_rect.collidepoint(mouse_pos):
            brush_color = blue
            stamp_state = False
        if yellow_rect.collidepoint(mouse_pos):
            brush_color = yellow
            stamp_state = False
        if pink_rect.collidepoint(mouse_pos):
            brush_color = pink
            stamp_state = False
        if gray_rect.collidepoint(mouse_pos):
            brush_color = gray
            stamp_state = False
        if purple_rect.collidepoint(mouse_pos):
            brush_color = purple
            stamp_state = False
        if white_rect.collidepoint(mouse_pos):
            brush_color = white
            stamp_state = False
    if draw == True:
        if eraser_rect.collidepoint(mouse_pos):
            brush_color=black
            stamp_state = False
    
    if draw == True:
        if clear_rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen, black, screen_rect)
    if draw == True:
        if save_rect.collidepoint(mouse_pos):
            save_surf=pygame.Surface((600, 550))
            save_surf.blit(screen, (0, 0), (200, 0, 600, 550))
            try:
                with open("image" + str(file_number) + ".png"):
                    file_number = file_number + 1
                    save_flag = True
            except IOError:
                save_flag = True
            pygame.image.save(save_surf, 'image' + str(file_number)+'.png')
    
    pygame.draw.rect(screen, black, menu_rect)
    pygame.draw.rect(screen, white, square)
    screen.blit(menu_text, (30, 10))
    pygame.draw.line(screen, gray, (200,0), (200,600), 2)
    pygame.draw.line(screen, gray, (0, 35), (200, 35), 1)
    pygame.draw.line(screen, gray, (0, 170), (200, 170), 1)
    pygame.draw.line(screen, gray, (0, 470), (200, 470), 1)
    screen.blit(color_text, (25, 40))
    pygame.draw.rect(screen, gray, clear_rect)
    pygame.draw.rect(screen, gray, save_rect)
    screen.blit(clear_text, (60,480))
    screen.blit(save_text, (65,510))
    

    pygame.draw.rect(screen, green, green_rect)
    if brush_color == green:
        border = 3
    else:
        border = 1
    pygame.draw.rect(screen, black, green_rect, border)
    
    pygame.draw.rect(screen, red, red_rect)
    if brush_color == red:
        border = 3
    else:
        border = 1
    pygame.draw.rect(screen, black, red_rect, border)
    
    pygame.draw.rect(screen, blue, blue_rect)
    if brush_color == blue:
        border = 3
    else:
        border = 1
    pygame.draw.rect(screen, black, blue_rect, border)

    pygame.draw.rect(screen, pink, pink_rect)
    if brush_color == pink:
        border = 3
    else:
        border = 1
    pygame.draw.rect(screen, black, pink_rect, border)

    pygame.draw.rect(screen, yellow, yellow_rect)
    if brush_color == yellow:
        border = 3
    else:
        border = 1
    pygame.draw.rect(screen, black, yellow_rect, border)
    
    pygame.draw.rect(screen, white, white_rect)
    if brush_color == white:
        border = 3
    else:
        border = 1
    pygame.draw.rect(screen, black, white_rect, border)

    pygame.draw.rect(screen, purple, purple_rect)
    if brush_color == purple:
        border = 3
    else:
        border = 1
    pygame.draw.rect(screen, black, purple_rect, border)
    
    pygame.draw.rect(screen, gray, gray_rect)
    if brush_color == gray:
        border = 3
    else:
        border = 1
    pygame.draw.rect(screen, black, gray_rect, border)
    

    screen.blit(eraser, eraser_rect)
    if brush_color == black:
        border = 3
    else:
        border = 1
    pygame.draw.rect(screen, white, eraser_rect, border)
    screen.blit(rect_p, rect_rect)
    pygame.draw.rect(screen, black, rect_rect, 1)
    screen.blit(circle_p, circle_rect)
    pygame.draw.rect(screen, black, circle_rect, 1)
    
    pygame.display.update() 
