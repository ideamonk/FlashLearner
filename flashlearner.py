# -*- coding: utf-8 -*-
# FlashLearner - a Flash Card based learning tool for Maemo
#                                                             ideamonk gmail.com
import os
import sys
import pygame

WIDTH = 800
HEIGHT = 480

if __name__ == '__main__':
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
    font = pygame.font.Font(os.path.join ("./ui","lily.ttf"), 36)
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

    


    raw_input()
   