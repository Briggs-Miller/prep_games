import pygame
import random
import time
clock = pygame.time.Clock()
pygame.init()
pygame.font.init()

def run():
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
    screen.fill(WHITE)
    
    show_score = pygame.USEREVENT + 1
    pause = pygame.USEREVENT + 2
    pygame.time.set_timer(show_score, 2000)
    pygame.time.set_timer(pause, 1000)
    
    font_size = 30
    gap = 40
    myfont = pygame.font.SysFont('Comic Sans MS', font_size)
    
    def play_wrong():
        effect = pygame.mixer.Sound('wrong.wav')
        effect.play()
    
    def play_correct():
        effect = pygame.mixer.Sound('correct.wav')
        effect.play()
        
    def update_screen():
        heading = myfont.render('ORDER THE NUMBERS', False, GREEN)
        screen.blit(heading,(10,10))
        
        instructions = myfont.render('Press [Esc] to exit at any time', False, PINKYPURPLE)
        screen.blit(instructions,(10,10+gap))
        
        score_string = str(score)
        text_score = "Score:  "+score_string
        write_score = myfont.render(text_score, False, PURPLE)
        screen.blit(write_score,(40,350))
        
    done = False
    play = False
    score = 0
    their_guess = []
    guess_list = []
    combined_number = ""
    
    while not done:
    
        while not play:
            if score <0:
                range_lower = 0
                range_upper = 10
                amount_of_numbers_to_be_guessed = 3
            elif score < 5:
                range_lower = 0
                amount_of_numbers_to_be_guessed = 3
                range_upper = 20 + ((int(score)-1) * 10)
            elif score <20:
                range_lower = 0
                amount_of_numbers_to_be_guessed = (int((score*(.2))+2))
                range_upper = (3**(score))
            else:
                range_lower = int((level - 9)*-10)
                amount_of_numbers_to_be_guessed = (int((level*(.1))+2))
                range_upper = int((level-9)*10)
        
            the_numbers = []
        
            while len(the_numbers) < amount_of_numbers_to_be_guessed:
        
            
                the_random_number = random.randint(range_lower, range_upper)
        
                # -- check the number isn't in the list already
                if the_random_number not in the_numbers:
                    the_numbers.append(the_random_number)
        
            numbers_string = ", ".join(str(x) for x in the_numbers)
            string_numbers = "Put " + numbers_string + " in order from smallest to largest"
            print_numbers = myfont.render(string_numbers, False, PINKYPURPLE)
            screen.blit(print_numbers, (10,10+gap*2))
            guess_list = the_numbers
            guess_list.sort()
            play = True
    
            
        if len(their_guess) < len(guess_list):
            write_prompt = (len(their_guess)+1)
            string_prompt = "Number " + str(write_prompt) + " is:  "
            print_prompt = myfont.render(string_prompt, False, PINKYPURPLE)
            screen.blit(print_prompt, (10, 100 + gap*write_prompt))
    
        elif len(their_guess) == len(guess_list):
            if their_guess == guess_list:
    
                play = False
                score +=1
                play_correct()
                guess_list = []
                their_guess = []
                screen.fill(WHITE)
            else:
    
                play = False
                score -=1
                play_wrong()
                guess_list = []
                their_guess = []
                screen.fill(WHITE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.QUIT
                print ("Thanks for playing!")
                done = True
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                their_guess.append(int(combined_number))
                combined_number = ""
    
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
                if len(combined_number) >0:
                    combined_number = combined_number[:(len(combined_number)-1)]  
                    pygame.draw.rect(screen, WHITE, ((220),(100 + (gap*write_prompt)), (200), font_size+5), 0)
                    print_number = myfont.render(combined_number, False, PINKYPURPLE)
                    screen.blit(print_number, (220, 100 + (gap*write_prompt)))                
                
            elif event.type == pygame.KEYDOWN:
    
                print_letter = (pygame.key.name(event.key))
                try:               
                    val = int(print_letter)
                    string_number = str(print_letter)
                    combined_number += string_number
                    print_number = myfont.render(combined_number, False, PINKYPURPLE)
                    screen.blit(print_number, (220, 100 + (gap*write_prompt))) 
                except ValueError:
                    continue
    
                
    
        
    
            
                
        update_screen()
        pygame.display.flip()
    
    
    
    
    
    
    
    
    