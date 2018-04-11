import pygame
import random
import csv
import time
import pyttsx3;
engine = pyttsx3.init();
pygame.init()
pygame.font.init()
import numbers
import spelling
import sentence
import gaps
import endings
import order


done = False


clock = pygame.time.Clock()

font_size = 30
gap = 80
myfont = pygame.font.SysFont('Comic Sans MS', font_size)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
PINKYPURPLE = (255,0,255)
PURPLE = (153, 0 , 153)

width = 800
height = 480
screen = pygame.display.set_mode((width, height), pygame.SRCALPHA)
backdrop = pygame.image.load('bg_rainbow.jpg')
fill_bg = pygame.transform.scale(backdrop, (width, height))

def button(msg,x,y,w,h,ic,ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()         
    else:
        pygame.draw.rect(screen, ic,(x,y,w,h))

    smallText = pygame.font.Font("freesansbold.ttf",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    screen.blit(textSurf, textRect)  

def text_objects(text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()

def quit():
    pygame.QUIT
    done = True
    print ("Thank for playing!")
    



while not done:
    for event in pygame.event.get():
 
        if event.type == pygame.QUIT:
            pygame.QUIT
            done = True
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.QUIT
            done = True
            
            
    screen.fill(WHITE)
    screen.blit(fill_bg, (0,0))
    myfont = pygame.font.SysFont('Comic Sans MS', 60)
    heading = myfont.render('Menu', False, PINKYPURPLE)
    screen.blit(heading,(10,10))
    
    button("Numbers", 150,150+gap, 100, 50, PURPLE, PINKYPURPLE, numbers.run)
    button("Spelling", 150, 150+gap*2, 100, 50, PURPLE, PINKYPURPLE, spelling.run)
    button("Sentence", 200+gap, 150+gap, 100, 50, PURPLE, PINKYPURPLE, sentence.run)
    button("Fill gaps", 200+gap, 150+gap*2, 100, 50, PURPLE, PINKYPURPLE, gaps.run)
    button("Endings", 250+gap*2, 150+gap, 100, 50, PURPLE, PINKYPURPLE, endings.run)
    button("Ordering", 250+gap*2, 150+gap*2, 100, 50, PURPLE, PINKYPURPLE, order.run)
    
    pygame.display.update()
    clock.tick(15)

