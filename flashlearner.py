# -*- coding: utf-8 -*-
# FlashLearner - a Flash Card based learning tool for Maemo
#                                                             ideamonk gmail.com
import os
import sys
import random

try:
    import pygame
except ImportError:
    print "You need python-pygame installed on your device."
    exit(0)

try:
    import cPickle as pickle
except ImportError:
    import pickle


WIDTH = 800
HEIGHT = 480
expansions = { "n":"noun", "aj":"adjective", "v":"verb" }
dontChange = 0

def randomizeWord():
    global wordnumber
    if (dontChange==0):
        wordnumber = random.randint (0,len(wordlist)-1)
    
if __name__ == '__main__':
    global wordnumber
    
    # setup display
    pygame.init()
    pygame.font.init()
    pygame.display.set_mode( (WIDTH,HEIGHT), pygame.DOUBLEBUF|pygame.HWSURFACE )
    pygame.display.set_caption ("FlashLearner 0.1")

    # load images
    paper_layer = pygame.image.load (os.path.join ("./ui","notepaper.png"))
    settings_layer = pygame.image.load (os.path.join ("./ui","notepaper_settings.png"))
    
    # setup buffers
    mybuffer = pygame.Surface ((WIDTH,HEIGHT))
    mybuffer.blit (paper_layer,(0,0))
    screen = pygame.display.get_surface()

    # Load wordlist
    # Show loading...
    font = pygame.font.Font(os.path.join ("./ui","lily.ttf"), 76)
    medfont = pygame.font.Font(os.path.join ("./ui","lily.ttf"), 34)
    smallfont = pygame.font.Font(os.path.join ("./ui","lily.ttf"), 28)
    text = font.render("loading...", 1, (10, 10, 10))
    textpos = text.get_rect(centerx=WIDTH/2,centery=HEIGHT/2)
    mybuffer.blit(text, textpos)
    screen.blit(mybuffer,(0,0))
    pygame.display.flip()
    
    # load actual wordlist
    wordlist = []
    fp = open (os.path.join("./flr","GRE Tools.flr"),"r")
    while True:
        line = fp.readline()
        if (len(line)==0):
            break
        wordlist.append ( line.split(':') )

    # hide the loading... message
    mybuffer.blit (paper_layer,(0,0))
    screen.blit(mybuffer,(0,0))
    pygame.display.flip()

    # load settings from pickler
    settings_file = os.path.join ("./settings/","flr_settings")
    if os.path.exists(settings_file):
        flr_settings = pickle.load(open(settings_file))
    else:
        # make one and store
        flr_settings = {'delay':20}
        pickle.dump(flr_settings, open(settings_file, 'w'))

    pygame.time.set_timer(pygame.USEREVENT+1, flr_settings['delay']*100)
    wordnumber = random.randint (0,len(wordlist)-1)
    while True:
        
        mybuffer.blit (paper_layer,(0,0))
        # ---------------------------------------------------------------------/

        # draw word
        text = font.render(wordlist[wordnumber][1], 1, (0, 0, 0))
        textpos = text.get_rect(centerx=WIDTH/2,centery=180)
        mybuffer.blit(text, textpos)
        
        # draw type
        try:
            text = medfont.render(expansions[wordlist[wordnumber][0]], 1, (85, 85, 85))
            textpos = text.get_rect(x=110,centery=80)
            mybuffer.blit(text, textpos)
        except:
            ''' don't draw '''
        
        # process mouse events
        for event in pygame.event.get():
            if event.type == pygame.USEREVENT+1:
                randomizeWord()
            if event.type == pygame.QUIT:
                break

        dontChange = 0
        if (pygame.mouse.get_pressed()[0]):
            if (pygame.mouse.get_pos()[1]>50):
                dontChange = 1
                torender = wordlist[wordnumber][2][:-1]
                if (len(torender)<40):
                    text = smallfont.render(torender, 1, (0, 0, 0))
                    textpos = text.get_rect(centerx=WIDTH/2,centery=260)
                    mybuffer.blit(text, textpos)
                else:
                    todolist=torender.split()
                    todoindex = 0
                    todo_y = 260
                    torender = ""
                    while (todoindex<len(todolist)):
                        torender += todolist[todoindex]+" "
                        if (len(torender)>40):
                            text = smallfont.render(torender, 1, (0, 0, 0))
                            textpos = text.get_rect(centerx=WIDTH/2,centery=todo_y)
                            mybuffer.blit(text, textpos)
                            torender = ""
                            todo_y+=smallfont.get_height() + 5 # offset gap
                            
                        todoindex+=1

        # ---------------------------------------------------------------------\
        screen.blit(mybuffer,(0,0))
        pygame.display.flip()
        
    raw_input()
   