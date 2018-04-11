# to do:  learn how to enter in capital letters

import pygame
import random
import csv
import time
import pyttsx3;
engine = pyttsx3.init();
pygame.init()
pygame.font.init()
import csv


def run():
    clock = pygame.time.Clock()
    
    
    
    def play_wrong():
        effect = pygame.mixer.Sound('wrong.wav')
        effect.play()
       
    
    	
    def update_screen():
        activity_window = pygame.draw.rect(screen, WHITE, (0,activity_y,width,height-activity_y), 0)

        load_image = pygame.image.load("snake.jpg")
        load_image = pygame.transform.scale(load_image, (400,200))
        screen.blit(load_image, ((width-400,height-200)))
        
        heading = myfont.render('NUMBERS', False, GREEN)
        screen.blit(heading,(10,10))
        
        instructions = myfont.render('Press [space bar] to hear the number', False, PINKYPURPLE)
        screen.blit(instructions,(10,10+gap))
        
        exit = myfont.render('Press [Esc] to exit at any time', False, PINKYPURPLE)
        screen.blit(exit,(10,10+gap*2))	
        score_string = str(score)
        text_score = "Score:  "+score_string
        write_score = myfont.render(text_score, False, PURPLE)
        screen.blit(write_score,(40,350))
    
    
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    GREEN = (0, 255, 0)
    PINKYPURPLE = (255,0,255)
    PURPLE = (153, 0 , 153)
    
    width = 600
    height = 480
    screen = pygame.display.set_mode((width, height), pygame.SRCALPHA)
    screen.fill(WHITE)
    activity_y = 100
    activity_height = 220
    
    def play_correct():
        effect = pygame.mixer.Sound('correct.wav')
        effect.play()
    
    def correct():
        correct = myfont.render("You are correct!", False, GREEN)
        screen.blit(correct,(40,250))
    
    show_score = pygame.USEREVENT + 1
    pause = pygame.USEREVENT + 2
    pygame.time.set_timer(show_score, 2000)
    pygame.time.set_timer(pause, 1000)
    
    
    font_size = 30
    gap = 40
    myfont = pygame.font.SysFont('Comic Sans MS', font_size)
    
    def speak(random_word):
        engine.say(random_word);
        engine.runAndWait() ;
        print (random_word)
    
    

    
    
    
    letters_revealed = 0
    letter_gap = 40
    blank_gap = 40
      
          
    done = False
    
    their_guess = []
    play = False
    
    #get the words and sentences into dictionary via .csv file
    
    reader = csv.DictReader(open('numbers.csv', 'r'))
    dict_list = []
    for line in reader:
        dict_list.append(line)
    
    total_words = len(dict_list)
    
              
    score = 0   
    
    
    
    while not done:
    
    	
        while not play:
            if score < len(dict_list):
                active_word_index = random.randint(0, score)
            else:
                active_word_index = random.randint(0, (len(dict_list)-1))
            random_word = (dict_list[active_word_index]["digit"])
            number = (dict_list[active_word_index]["number"])
            
                 
            wordaslist = list(random_word) 	
            update_screen()
            while letters_revealed <len(random_word):    
                write_number = myfont.render(number, False, BLUE)
                screen.blit(write_number,(10,10+gap*3))	
    
                heading = myfont.render('_', False, BLACK)
                screen.blit(heading,(10+letter_gap,200))
                letter_gap +=30
                letters_revealed +=1
            play = True
    
    
        for event in pygame.event.get():
            letter_gap = 30
            if event.type == pygame.QUIT:
                    done = True
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.QUIT
                print ("Thanks for playing!")
                done = True
            elif event.type == pause:
                corrected = True
                pygame.time.set_timer(pause, 0)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                speak(number)
            elif event.type == pygame.KEYDOWN:
                    print_letter = (pygame.key.name(event.key))
                    
                    if len(print_letter) ==1:
                        their_guess.append(print_letter)
                        letter = myfont.render(print_letter, False, GREEN)
                        screen.blit(letter,(20+(len(their_guess)*letter_gap),200))
                    elif print_letter =='backspace' and len(their_guess):
                        letter = myfont.render(print_letter, False, GREEN)
                        eraser = pygame.draw.rect(screen, BLACK, ((20+(len(their_guess)*letter_gap)),200, (letter_gap+20), font_size+5), 0)
                        
                        if len(their_guess) > 0 :
                            del their_guess[-1]
    
    
    					
        if event.type == show_score:
            if len(their_guess) >= len(wordaslist):
                
                if their_guess == wordaslist:
                    score += 1
                    play_correct()
    
    
    
                    
                else:
                    if score == 0:
                        play_wrong()
                        score = 0
                    else:
                        play_wrong()
                        score -= 1
                their_guess = []
                
                
                letters_revealed = 0; letter_gap = 40    
                play = False
            
             
        
        pygame.display.flip()
  
    
    
    
    
    
    
    