from dataclass import Pokemon
from utils import TestRequirements, tuple_checker, generate_pokemon, get_pokemon
from utils import color_dark, color, color_light
try:
    TestRequirements().test_requirements()
except Exception as e:
    print(e)
    exit()

import pygame
import os
import random
from urllib.request import urlopen

pygame.mixer.init()
pygame.init()

clock = pygame.time.Clock()

hollow_font = pygame.font.Font('Fonts/PokemonHollow.ttf',35)
solid_font = pygame.font.Font('Fonts/PokemonSolid.ttf',35)

pygame.mixer.music.load("Music.mp3")
pygame.mixer.music.play(loops=-1)

# Set up the drawing window
SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 900
screen = pygame.display.set_mode([1600, 900])
bg = pygame.image.load(os.path.join('Images', 'Background.png')).convert()
BG_WIDTH = SCREEN_WIDTH/2
BG_HEIGHT = SCREEN_HEIGHT
BG_center = (
    (SCREEN_WIDTH-BG_WIDTH/2-100),
    (SCREEN_HEIGHT-BG_HEIGHT/2-150))
background = pygame.transform.scale(bg, (BG_WIDTH, BG_HEIGHT))
pokemon_boxes = [(0,0), (SCREEN_WIDTH/4,0), (0,SCREEN_HEIGHT/4), (SCREEN_WIDTH/4,SCREEN_HEIGHT/4)]

# Pokemon footprint definition
footprint = random.choice(get_pokemon())
footprint_image = pygame.image.load(os.path.join('Sprites', str(footprint)+'.png')).convert()
footprint_image = pygame.transform.scale(footprint_image, (200, 200))

# Pokemon sprites and names
pokemon_1, pokemon_2, pokemon_3, pokemon_4 = generate_pokemon(footprint)
name1 = hollow_font.render(pokemon_1.name, True, color_dark)
name2 = hollow_font.render(pokemon_2.name, True, color_dark)
name3 = hollow_font.render(pokemon_3.name, True, color_dark)
name4 = hollow_font.render(pokemon_4.name, True, color_dark)
pokemon_box = pygame.image.load(os.path.join('Images', 'Card.png')).convert()
pokemon_box = pygame.transform.scale(pokemon_box, (SCREEN_WIDTH/4, SCREEN_HEIGHT/4))

width = screen.get_width()
height = screen.get_height()
  
running = True
while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False

        #checks if a mouse is clicked
        if event.type == pygame.MOUSEBUTTONDOWN:
            #if the mouse is clicked on the
            # button the game is terminated
            if tuple_checker(mouse, pokemon_boxes[0]) == True:
                print("BOX 1")
                if pokemon_1.correct == True:
                    print('Correct!')
                else:
                    print("WRONG LOL")

            if tuple_checker(mouse, pokemon_boxes[1]) == True:
                print("BOX 2")
                if pokemon_2.correct == True:
                    print('Correct!')
                else:
                    print("WRONG LOL")

            if tuple_checker(mouse, pokemon_boxes[2]) == True:
                print("BOX 3")
                if pokemon_3.correct == True:
                    print('Correct!')
                else:
                    print("WRONG LOL")

            if tuple_checker(mouse, pokemon_boxes[3]) == True:
                print("BOX 4")
                if pokemon_4.correct == True:
                    print('Correct!')
                else:
                    print("WRONG LOL")

    # Fill the background with white

    screen.blit(background, (SCREEN_WIDTH-BG_WIDTH ,0))
    #screen.blit(footprint_image, (640, 360)
    screen.blit(footprint_image, BG_center)
    pygame.display.flip()

    screen.blit(pokemon_box, pokemon_boxes[0])
    screen.blit(pokemon_box, pokemon_boxes[1])
    screen.blit(pokemon_box, pokemon_boxes[2])
    screen.blit(pokemon_box, pokemon_boxes[3])

    screen.blit(pokemon_1.sprite, pokemon_1.position)
    screen.blit(name1, pokemon_1.position)

    screen.blit(pokemon_2.sprite, pokemon_2.position)
    screen.blit(name2, pokemon_2.position)

    screen.blit(pokemon_3.sprite, pokemon_3.position)
    screen.blit(name3, pokemon_3.position)

    screen.blit(pokemon_4.sprite, pokemon_4.position)
    screen.blit(name4, pokemon_4.position)

    pygame.display.flip()

    mouse = tuple(pygame.mouse.get_pos())
      

pygame.quit()

