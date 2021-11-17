import pygame 
import sys

#adding more comments

from pygame.constants import SWSURFACE #sys is system module to end the program
x_mode = 420
y_mode = 600


def draw_floor():
    screen.blit(floor_surface,(floor_x_position,500))
    screen.blit(floor_surface,(floor_x_position + 420,500)) #second floor that sticks to the first one
        
def create_pipe():
    new_pipe = pipe_surface.get_rect(midtop=(x_mode+200,y_mode/2))
    return new_pipe

def move_pipe(pipes):
    
    for pipe in pipes:
        pipe.centerx -= 5
     
    return pipes


def draw_pipes(pipes):
    for pipe in pipes:
        screen.blit(pipe_surface,(0,0)) 

pygame.init() #inittialize game

screen = pygame.display.set_mode((x_mode,y_mode))
clock = pygame.time.Clock()

#Game variables
gravity = 0.25
bird_movement = 0




bg_surface = pygame.image.load('D:/Daddy/Study/Python/FlappyBird/assets/background-day.png').convert()#to convert to python game images
bg_surface = pygame.transform.scale(bg_surface,(x_mode,y_mode))

floor_surface = pygame.image.load('D:/Daddy/Study/Python/FlappyBird/assets/base.png').convert()
floor_surface = pygame.transform.scale(floor_surface,(x_mode,100))
floor_x_position = 0

bird_surface = pygame.image.load("D:/Daddy/Study/Python/FlappyBird/assets/bluebird-midflap.png").convert()
#bird_surface = pygame.transform.scale(bird_surface)
bird_rect = bird_surface.get_rect(center=(100,300))

pipe_surface = pygame.image.load("D:/Daddy/Study/Python/FlappyBird/assets/pipe-green.png").convert()
#pipe_surface = pygame.transform.scale2x(pipe_surface)

pipe_list =[]

#using timer
SPAWNPIPE = pygame.USEREVENT #trigger by timer not by key
pygame.time.set_timer(SPAWNPIPE,1200) #mili seconds 1.2 second 


pipe_list.append(create_pipe())
       
while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit() #to end the program properly
            
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_SPACE:
                bird_movement = 0
                bird_movement -= 12
        if e.type == SPAWNPIPE:
       #     pipe_list.append(create_pipe())
            print("a")
            
    screen.blit(bg_surface,(0,0)) #no idea why the name is blit but it is to put the surface on display surface i.e. background
    
    
    #birds
    #move the bird
    bird_movement += gravity #0.25, 0.5, 0.75, 1 so on
    #move the rectange of the bird
    bird_rect.centery += bird_movement     
    screen.blit(bird_surface,bird_rect)
    
    #pipes
    #pipe_list = move_pipe(pipe_list)
       
    
    floor_x_position = floor_x_position - 1
    
    draw_floor()
    draw_pipes(pipe_list)
    
    if floor_x_position <= -420: #if the second floor reach the left hand side cordinate
        floor_x_position=0 #reset the position of the first floor
            
    pygame.display.update()
    clock.tick(120)