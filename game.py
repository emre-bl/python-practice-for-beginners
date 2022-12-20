import random
import math
import pygame
import sys 

harita = []
for i in range(10):
    harita.append(['O']*10)

x = 0
y = 0

hazine_x = random.randint(0,9)
hazine_y = random.randint(0,9)

while( hazine_x == 0 and hazine_y == 0):
    hazine_x = random.randint(0,9)
    hazine_y = random.randint(0,9)

mayin_x = random.randint(2,7)
mayin_y = random.randint(2,7)

while(mayin_x == hazine_x and mayin_y == hazine_y):
    mayin_x = random.randint(2,7)
    mayin_y = random.randint(2,7)
    


pygame.init()
screen = pygame.display.set_mode((400,400))
pygame.display.set_caption('Harita Game')
clock = pygame.time.Clock()

harita_surface = pygame.image.load('harita.png').convert()
duck = pygame.image.load('duck.png').convert_alpha()
duck_rect = duck.get_rect(center=(20,20))

popup_visible = False
popup_font = pygame.font.Font('Pixeltype.ttf', 40)
popup_message = popup_font.render('',False,'Black')
popup_message_rect = popup_message.get_rect(center=(100,100))


is_finished = False
safe_zones = []
danger_zones = []
most_dangerous_zone = []

while(True):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #get input from user with pygame
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and y > 0 and not is_finished:
        duck_rect.y -= 40
        y -= 1
    elif keys[pygame.K_s] and y < 9 and not is_finished:
        duck_rect.y += 40
        y += 1
    elif keys[pygame.K_a] and x > 0 and not is_finished:
        duck_rect.x -= 40
        x -= 1
    elif keys[pygame.K_d] and x < 9 and not is_finished:
        duck_rect.x += 40
        x += 1

    if(x == hazine_x and y == hazine_y):
        popup_message = popup_font.render('Hazineyi Buldunuz',False,'Black')
        popup_visible = True
        is_finished = True

    elif(x == mayin_x and y == mayin_y):
        popup_message = popup_font.render('Mayina Bastiniz',False,'Black')
        popup_visible = True
        is_finished = True
    
    elif(abs(x-mayin_x) <= 2 and abs(y-mayin_y) <= 2):
        if(abs(x-mayin_x) == 1 and abs(y-mayin_y) == 0):
            most_dangerous_zone.append([x,y])
        elif(abs(x-mayin_x) == 0 and abs(y-mayin_y) == 1):
            most_dangerous_zone.append([x,y])
        else:
            danger_zones.append([x,y])
            

    else:
        safe_zones.append([x,y])


    screen.blit(harita_surface,(0,0))
    

    for i in range(len(safe_zones)):
        pygame.draw.rect(screen,'green',(safe_zones[i][0]*40,safe_zones[i][1]*40,40,40))

    for i in range(len(danger_zones)):
        pygame.draw.rect(screen,'red',(danger_zones[i][0]*40,danger_zones[i][1]*40,40,40))

    for i in range(len(most_dangerous_zone)):
        pygame.draw.rect(screen,'black',(most_dangerous_zone[i][0]*40,most_dangerous_zone[i][1]*40,40,40))

    screen.blit(duck,duck_rect)

    if popup_visible:
        screen.blit(harita_surface,(0,0))
        screen.blit(popup_message,(100,300))

    
   
    pygame.display.update()
    clock.tick(10)

