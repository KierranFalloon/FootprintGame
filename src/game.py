from utils import TestRequirements, list_of_files, surf_from_url, name_from_api, tuple_checker
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

def get_pokemon():
# Setup Pokemon list
    return list_of_files()

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
other_pokemon = random.sample(get_pokemon(), 3)
other_pokemon.append(footprint)
name_list = [name_from_api(other_pokemon[0]),name_from_api(other_pokemon[1]), name_from_api(other_pokemon[2]), name_from_api(other_pokemon[3])]
name_1, name_2, name_3, name_4 = solid_font.render(name_list[0], True, color_dark), solid_font.render(name_list[1], True, color_dark), solid_font.render(name_list[2], True, color_dark), solid_font.render(name_list[3], True, color_dark)
pokemon_1, pokemon_2, pokemon_3, chosen_pokemon = surf_from_url(other_pokemon)
v_offset = 70
h_offset = 75
positions = [(h_offset, v_offset), (SCREEN_WIDTH/4 + h_offset, v_offset), (h_offset, SCREEN_HEIGHT/4 + v_offset), (SCREEN_WIDTH/4 + h_offset,SCREEN_HEIGHT/4 + v_offset)]
rand_pokemon_positions = random.sample(positions, 4)

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
                if tuple_checker(rand_pokemon_positions[3], pokemon_boxes[0]) == True:
                    print('Correct!')
                else:
                    print("WRONG LOL")

            if tuple_checker(mouse, pokemon_boxes[1]) == True:
                print("BOX 2")
                if tuple_checker(rand_pokemon_positions[3], pokemon_boxes[1]) == True:
                    print('Correct!')
                else:
                    print("WRONG LOL")

            if tuple_checker(mouse, pokemon_boxes[2]) == True:
                print("BOX 3")
                if tuple_checker(rand_pokemon_positions[3], pokemon_boxes[2]) == True:
                    print('Correct!')
                else:
                    print("WRONG LOL")

            if tuple_checker(mouse, pokemon_boxes[3]) == True:
                print("BOX 4")
                if tuple_checker(rand_pokemon_positions[3], pokemon_boxes[3]) == True:
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

    screen.blit(pokemon_1, rand_pokemon_positions[0])
    screen.blit(name_1, rand_pokemon_positions[0])
    screen.blit(pokemon_2, rand_pokemon_positions[1])
    screen.blit(name_2, rand_pokemon_positions[1])
    screen.blit(pokemon_3, rand_pokemon_positions[2])
    screen.blit(name_3, rand_pokemon_positions[2])
    screen.blit(chosen_pokemon, rand_pokemon_positions[3]) # rand_pokemon_positions[3] is always the position of the pokemon
    screen.blit(name_4, rand_pokemon_positions[3])
    pygame.display.flip()

    mouse = tuple(pygame.mouse.get_pos())
      

pygame.quit()

