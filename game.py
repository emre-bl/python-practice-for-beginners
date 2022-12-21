import random
import math
import pygame
import sys 
# comment english
harita = []  # map
for i in range(10):
    harita.append(['O']*10) 

x = 0   # x coordinate
y = 0   # y coordinate

treasure_x = random.randint(0,9) # treasure x coordinate
treasure_y = random.randint(0,9) # treasure y coordinate

while( treasure_x == 0 and treasure_y == 0): # treasure can't be in the starting point
    treasure_x = random.randint(0,9)
    treasure_y = random.randint(0,9)

mine_x = random.randint(2,7)  # mine x coordinate
mine_y = random.randint(2,7)  # mine y coordinate

while(mine_x == treasure_x and mine_y == treasure_y): # mine can't be in the treasure point
    mine_x = random.randint(2,7)
    mine_y = random.randint(2,7)
    


pygame.init() # initialize pygame
screen = pygame.display.set_mode((800,800)) # create screen
pygame.display.set_caption('Game') # set title
clock = pygame.time.Clock() # create clock for fps

harita_surface = pygame.image.load('harita.png').convert() # load map image
duck = pygame.image.load('duck.png').convert_alpha() # load duck image
duck_rect = duck.get_rect(center=(40,40)) # set duck image position

popup_visible = False # popup message visibility
popup_font = pygame.font.Font('Pixeltype.ttf', 80) # load font
popup_message = popup_font.render('',False,'Black') # create empty popup message
popup_message_rect = popup_message.get_rect(center=(100,100)) # set popup message position

end_surface = pygame.image.load('end.png').convert()
end_rect = end_surface.get_rect(center=(400,400))


is_finished = False # game is finished or not
safe_zones = [] # safe zones
danger_zones = [] # danger zones
most_dangerous_zone = [] # most dangerous zone

while(True): # main loop
    for event in pygame.event.get(): # get events
        if event.type == pygame.QUIT: # if user click close button
            pygame.quit() # quit pygame
            sys.exit() # quit program

    keys = pygame.key.get_pressed() # get pressed keys
    if keys[pygame.K_w] and y > 0 and not is_finished: # if user press w and y coordinate is greater than 0 and game is not finished
        duck_rect.y -= 80 # move duck image
        y -= 1 # change y coordinate
    elif keys[pygame.K_s] and y < 9 and not is_finished: # if user press s and y coordinate is smaller than 9 and game is not finished
        duck_rect.y += 80
        y += 1
    elif keys[pygame.K_a] and x > 0 and not is_finished: # if user press a and x coordinate is greater than 0 and game is not finished
        duck_rect.x -= 80
        x -= 1
    elif keys[pygame.K_d] and x < 9 and not is_finished: # if user press d and x coordinate is smaller than 9 and game is not finished
        duck_rect.x += 80
        x += 1

    if(x == treasure_x and y == treasure_y): # if user find treasure
        popup_message = popup_font.render('Hazineyi Buldunuz',False,'Black') # create popup message
        popup_visible = True # set popup message visibility
        is_finished = True # set game is finished 

    elif(x == mine_x and y == mine_y): # if user find mine
        popup_message = popup_font.render('You dead!',False,'Black')  # create popup message
        popup_visible = True
        is_finished = True
    
    elif(abs(x-mine_x) <= 2 and abs(y-mine_y) <= 2): # if user is in danger zone
        if(abs(x-mine_x) == 1 and abs(y-mine_y) == 0): # if user is in most dangerous zone
            most_dangerous_zone.append([x,y])
        elif(abs(x-mine_x) == 0 and abs(y-mine_y) == 1): # if user is in most dangerous zone
            most_dangerous_zone.append([x,y])
        else: 
            danger_zones.append([x,y]) # if user is in danger zone
            

    else: # if user is in safe zone
        safe_zones.append([x,y])


    screen.blit(harita_surface,(0,0))  # draw map image
    

    for i in range(len(safe_zones)): # draw safe zones
        pygame.draw.rect(screen,'green',(safe_zones[i][0]*80,safe_zones[i][1]*80,80,80))

    for i in range(len(danger_zones)): # draw danger zones
        pygame.draw.rect(screen,'red',(danger_zones[i][0]*80,danger_zones[i][1]*80,80,80))

    for i in range(len(most_dangerous_zone)): # draw most dangerous zone
        pygame.draw.rect(screen,'black',(most_dangerous_zone[i][0]*80,most_dangerous_zone[i][1]*80,80,80))

    screen.blit(duck,duck_rect) # draw duck image

    if popup_visible: # if popup message is visible
        screen.blit(end_surface,end_rect)
        screen.blit(popup_message,(200,300))

    
   
    pygame.display.update()
    clock.tick(10) # set fps

