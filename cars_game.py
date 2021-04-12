import pygame
import random
pygame.init()

frame = pygame.display.set_mode((400,600))
background = pygame.image.load("./images/bg.png")
pygame.display.set_caption("Need for speed 2.0")
font = pygame.font.SysFont('Times new roman',40)

isDone = False
isBul = False

enemyImg = pygame.image.load("./images/Enemy.png")
playerImg = pygame.image.load("./images/Player.png")
coinImg = pygame.image.load('./images/coin.png')
score = 0 
coins = 0

player_x = 200
player_y = 500


enemy_x = random.randint(0, 360)
enemy_y = 0
enemy_dy = 5


coin_x = random.randint(0,360)
coin_y = random.randint(100,200)
coin_dy = 5


music = pygame.mixer.Sound("music.wav")
crash = pygame.mixer.Sound("crash.wav")






def show_player(x, y):
    frame.blit(playerImg, (x, y))

def show_enemy(x, y):
    frame.blit(enemyImg, (x, y))

def show_coin(x, y):
    frame.blit(coinImg, (x, y))
        
    

def isCollision(enemy_x, enemy_y, player_x, player_y):
    if player_x in range(enemy_x, enemy_x + 70) and player_y in range(enemy_y, enemy_y + 70):
        return True
    return False




def show_score(x, y):
    sc = font.render("Score: " + str(score), True, (0, 0, 0))
    frame.blit(sc, (x, y))
def show_coins(x,y):
    co = font.render("Coins: " + str(coins), True, (0, 0, 0))
    frame.blit(co,(x,y))


while not isDone:

    music.play()
    
    


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isDone = True
    pressed = pygame.key.get_pressed()
    
    if coin_y >= 580:
        coin_y = 0
        coin_x = random.randint(0, 360)
    if coin_x in range(player_x,player_x + 70) and coin_y in range(player_y, player_y + 70):
        coin_y = 0
        coin_x = random.randint(0, 360)
        coins += 1
    else:
        coin_y += coin_dy




    if enemy_y >= 580:
        enemy_y = 0
        enemy_x = random.randint(0, 360)
        score += 1
    else:
        enemy_y += enemy_dy


    if pressed[pygame.K_LEFT]:
        player_x -= 5
    

    if pressed[pygame.K_RIGHT]:
        player_x += 5

    if (player_x < 0 or player_x > 735):
        player_x = player_x % 735

    if enemy_y < 0 or enemy_y > 735:
        enemy_y += enemy_y
    frame.blit(background, (0, 0))
        


    isCol = isCollision(enemy_x, enemy_y, player_x, player_y)
    if isCol:
        enemy_x = random.randint(100, 700)
        enemy_y = random.randint(20, 50)
        isBul = False

    show_player(player_x, player_y)
    show_enemy(enemy_x, enemy_y)
    show_coin(coin_x,coin_y)
    show_score(235, 30)
    show_coins(30,30)
    pygame.display.update()
