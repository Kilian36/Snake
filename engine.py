'''
SNAKE BY KILIAN,FEBE AND TEO.....
'''

import pygame
# Display 500*500

#Serpente ---- testa con le caselle 

#Cibo ---- random generated
import random

class Snake():
    

    def __init__(self, position_head, position_tail):
        self.lenght=2
        self.positions=[position_tail,position_head]

    def move_snake(self, new_head_position, just_ate=False):
        '''
        Move snake positions, if snake just ate function creates a new position of the head
        else move every position following the head one
        '''
        if just_ate:
            self.positions.append([new_head_position[0],new_head_position[1]])
            #If i use new_head_position when it's value changepython 
            #when i determine the new head position the value will directly change in 
            #the value of the last element of self.position
            #Stack overflow question?
            self.lenght+=1
        else: 
            i=0 
            while i<self.lenght-1: 
                self.positions[i][0]=self.positions[i+1][0]
                self.positions[i][1]=self.positions[i+1][1]
                if i==len(self.positions)-2:
                    self.positions[i+1][0]=new_head_position[0]
                    self.positions[i+1][1]=new_head_position[1]
                    break
                i+=1
    def check_new_head(self, new_head_position):
        '''
        Return true if snake just ate himself
        '''
        for i in range(len(self.positions)-2):
            if new_head_position[0]==self.positions[i][0] and new_head_position[1]==self.positions[i][1]:
                return True
        return False 

def generate_food(snake):
    food_on_snake=True
    while food_on_snake:
        food_on_snake=False
        x_food=random.randint(0,19) #Grid length
        y_food=random.randint(0,19) #Grid length
        for snake_slice in snake.positions:
            if snake_slice[0]==x_food and snake_slice[1]==y_food:
                food_on_snake=True
    return x_food,y_food

def wait_time():
    start_ticks=pygame.time.get_ticks() #starter tick  
    finish=False
    while not finish:
            ##TIMING DEL LEVEL FINISHED
            seconds=(pygame.time.get_ticks()-start_ticks)/1000 #calculate how many seconds
            if seconds>2: 
               finish=True

#Game section
from pygame.locals import *

# 2 - Initialize the game
pygame.init()
pygame.font.init()
width, height = 500, 500
keys =1 #0 1 2 3 W A S D
coordinate_testa=[10,9]
screen=pygame.display.set_mode((width, height))
contatore=0
divisore=40
    

#STARTING THE GAME
# 6 - draw the snake
black_pixels=pygame.image.load("C:/Users/Kilian/Desktop/Games/Snake/body.png")
lose_img=pygame.image.load("C:/Users/Kilian/Desktop/Games/Snake/you_lose.png")
testa_su=pygame.image.load("C:/Users/Kilian/Desktop/Games/Snake/serpe alto.png")
testa_sx=pygame.image.load("C:/Users/Kilian/Desktop/Games/Snake/serpe sinistra.png")
testa_dx=pygame.image.load("C:/Users/Kilian/Desktop/Games/Snake/serpe destra.png")
testa_basso=pygame.image.load("C:/Users/Kilian/Desktop/Games/Snake/serpe basso.png")
food=pygame.image.load("C:/Users/Kilian/Desktop/Games/Snake/peperoncino.png")
position1=[10,10] #head_coordinate
position2=[10,11] #tail_coordinate
snake=Snake(position1,position2)
just_ate=True
#SNAKE PARTS
#IMAGES
#CONTROL OF DIRECTION
last_direction=1 #RIGHT
flag=True

#Frame controller
frame_controler=0
#Read record from file 
with open("C:/Users/Kilian/Desktop/Games/Snake/record.txt") as file:
    data=file.readline()
    record=int(data)
    
while flag:
    frame_controler+=1
    if frame_controler==20:
        frame_controler=0
        screen.fill(0)
        for i,snake_slice in enumerate(snake.positions): 
            #I've decided to make the snake 25x25xlength 
            x_coord=25*snake_slice[0]
            y_coord=25*snake_slice[1] 
            if i==snake.lenght-1:
                if last_direction==0:
                    screen.blit(testa_su,(x_coord,y_coord))
                elif last_direction==1:
                    screen.blit(testa_sx,(x_coord,y_coord))
                elif last_direction==2:
                    screen.blit(testa_basso,(x_coord,y_coord))
                else :
                    screen.blit(testa_dx,(x_coord,y_coord))
            else:
                screen.blit(black_pixels,(x_coord,y_coord))
    if just_ate:
        #Generate food
        x_food, y_food= generate_food(snake)
        just_ate=False
    screen.blit(food,(x_food*25,y_food*25))
    #Update the score 
    myfont = pygame.font.SysFont("monospace", 16)
    scoretext = myfont.render("Record = "+str(record)+ "  Score = "+str(snake.lenght-2), False, (255,255,255))
    screen.blit(scoretext, (260, 0))
    pygame.display.flip()

    for event in pygame.event.get():
        # check if the event is the X button 
        if event.type==pygame.QUIT:
            # if it is quit the game
            pygame.quit() 
        if event.type == pygame.KEYDOWN:
            if event.key==K_w:
                keys=0
            elif event.key==K_a:
                keys=1
            elif event.key==K_s:
                keys=2
            elif event.key==K_d:
                keys=3
        
        # 9 - Move player
    contatore += 1
    if contatore==divisore:
        contatore = 0
        if keys==0: # W ----> want to go up
            if last_direction!=2: #'DOWN': mantain the last direction
                last_direction=0 #Update the new direction (UP)
        elif keys==2: #S ----> want to go down
            if last_direction!=0:  #'UP':
                last_direction=2 #Update the saved direction (DOWN)
        elif keys==1: #A ----> want to go left
            if last_direction!=3: #  "RIGHT":
                last_direction=1
        elif keys==3: #D ----> want to go Right
            if last_direction!=1: #  "LEFT":
                last_direction=3
        #Now Move head
        if last_direction==0:
            if coordinate_testa[1]!=0:
                coordinate_testa[1]-=1
            else:
                coordinate_testa[1]=19   

        elif last_direction==1:
            if coordinate_testa[0]!=0:
                coordinate_testa[0]-=1
            else:
                coordinate_testa[0]=19
        elif last_direction==2:
            if coordinate_testa[1]!=19:
                coordinate_testa[1]+=1
            else:
                coordinate_testa[1]=0
        else:
            if coordinate_testa[0]!=19:
                coordinate_testa[0]+=1
            else:
                coordinate_testa[0]=0
        #Checking and moving the snake
        #Check if snake ate himself
        status=snake.check_new_head(coordinate_testa)
        if not status:
             #Check if the snake just ate food
            if x_food==coordinate_testa[0] and y_food==coordinate_testa[1]:
                just_ate=True
            #Move the snake in the next position
            snake.move_snake(coordinate_testa,just_ate)

        else :
            #280x180
            screen.blit(lose_img,(350/2,220))
            pygame.display.flip()
            if snake.lenght-2>record:
                record=snake.lenght-2
                with open("C:/Users/Kilian/Desktop/Snake/record.txt", "w") as file:
                    file.write(str(record))
            del(snake)
            snake=Snake(position1,position2)
            just_ate=True
            wait_time()

    


