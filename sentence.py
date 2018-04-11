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

clock = pygame.time.Clock()


def run():

    def play_wrong():
        effect = pygame.mixer.Sound('wrong.wav')
        effect.play()
       
    def get_random_word(word_list):
        list_choice = random.randint(0, 10)
        if list_choice > 8:
            a = random.choice(word_list).rstrip()
        else:
            a = random.choice(high_freq).rstrip()
        return a
    
    	
    def update_screen():
        screen.fill(PINKYPURPLE)
        
        heading = myfont.render('SENTENCE:  FILL THE GAP', False, WHITE)
        screen.blit(heading,(10,10))
        
        instructions = myfont.render('Press [space bar] to hear the sentence', False, WHITE)
        screen.blit(instructions,(10,10+gap))
        
        exit = myfont.render('Press [Esc] to exit at any time', False, WHITE)
        screen.blit(exit,(10,10+gap*2))	
        score_string = str(score)
        text_score = "Score:  "+score_string
        write_score = myfont.render(text_score, False, GREEN)
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
    pygame.time.set_timer(show_score, 1000)
    pygame.time.set_timer(pause, 1000)
    
    
    font_size = 30
    gap = 40
    
    def speak(random_word):
        engine.say(random_word);
        engine.runAndWait() ;
        print (random_word)
    
    
    myfont = pygame.font.SysFont('Comic Sans MS', font_size)
    letters_revealed = 0
    letter_gap = 40
    blank_gap = 40
      
          
    done = False
    
    their_guess = []
    play = False
    
    #get the words and sentences into dictionary via .csv file
    
    reader = csv.DictReader(open('vedawords.csv', 'r'))
    dict_list = []
    for line in reader:
        dict_list.append(line)
    
    total_words = len(dict_list)
    
              
    score = 0   
    
    while not done:
    
    	
        while not play:
            active_word_index = random.randint(0, total_words-1)
            random_word = (dict_list[active_word_index]["word"])
            sentence = (dict_list[active_word_index]["sentence"])
            blank_sentence = sentence.replace(random_word, '?')
            random_word = random_word.lower()     
            wordaslist = list(random_word) 	
            update_screen()
            while letters_revealed <len(random_word):    
                write_sentence = myfont.render(blank_sentence, False, BLUE)
                screen.blit(write_sentence,(10,10+gap*3))	
    
                heading = myfont.render('_', False, WHITE)
                screen.blit(heading,(10+letter_gap,200))
                letter_gap +=30
                letters_revealed +=1
            image_word = random_word+".jpg"
            
            try:
                load_image = pygame.image.load(image_word)
                load_image = pygame.transform.scale(load_image, (250,200))
                screen.blit(load_image, ((width-250,height-200)))
            except:
                pass
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
                speak(sentence)
            elif event.type == pygame.KEYDOWN:
                    print_letter = (pygame.key.name(event.key))
                    
                    if len(print_letter) ==1:
                        their_guess.append(print_letter)
                        letter = myfont.render(print_letter, False, GREEN)
                        screen.blit(letter,(20+(len(their_guess)*letter_gap),200))
                    elif print_letter =='backspace' and len(their_guess):
                        letter = myfont.render(print_letter, False, GREEN)
                        eraser = pygame.draw.rect(screen, PINKYPURPLE, ((20+(len(their_guess)*letter_gap)),200, (letter_gap+20), font_size+5), 0)
                        
                        if len(their_guess) > 0 :
                            del their_guess[-1]
    
    
    					
        if event.type == show_score:
            if len(their_guess) >= len(wordaslist):
                
                if their_guess == wordaslist:
                    score += 1
                    play_correct()
    
    
    
                    
                else:
                    play_wrong()
                    score -= 1
                their_guess = []
                
                
                letters_revealed = 0; letter_gap = 40    
                play = False
            
             
        
        pygame.display.flip()
        
        
        
    
    
    
    
    
    