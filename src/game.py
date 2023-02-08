from dataclass import Pokemon
from utils import TestRequirements, tuple_checker, generate_pokemon, get_pokemon, tuple_subtraction
from utils import color_dark, color, color_light
import threading
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

hollow_font = pygame.font.Font('Fonts/PokemonHollow.ttf',25)
solid_font = pygame.font.Font('Fonts/PokemonSolid.ttf',25)

pygame.mixer.music.load("Music.mp3")
pygame.mixer.music.play(loops=-1)
pygame.display.set_caption("Footprint game!")
clock = pygame.time.Clock()
# Set up the drawing window
SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 900
screen = pygame.display.set_mode([1600, 900])
bg = pygame.image.load(os.path.join('Images', 'Background.png')).convert()
bg2 = pygame.image.load(os.path.join('Images', 'Background_3.png')).convert()
BG_WIDTH = (SCREEN_WIDTH/2)
BG_HEIGHT = SCREEN_HEIGHT
BG_center = (
    (SCREEN_WIDTH-BG_WIDTH/2-100),
    (SCREEN_HEIGHT-BG_HEIGHT/2-150))
background = pygame.transform.scale(bg, (BG_WIDTH, BG_HEIGHT))
background_2 = pygame.transform.scale(bg2, (BG_WIDTH, BG_HEIGHT/2))
pokemon_boxes = [(0,0), (SCREEN_WIDTH/4,0), (0,SCREEN_HEIGHT/4), (SCREEN_WIDTH/4,SCREEN_HEIGHT/4)]

# Pokemon footprint definition
footprint = random.choice(get_pokemon())
print(footprint)
footprint_image = pygame.image.load(os.path.join('Sprites', str(footprint)+'.png')).convert()
footprint_image = pygame.transform.scale(footprint_image, (200, 200))

# Pokemon sprites and names
pokemon_1, pokemon_2, pokemon_3, pokemon_4 = generate_pokemon(footprint)
name1 = solid_font.render(pokemon_1.name, None, color_dark)
name2 = solid_font.render(pokemon_2.name, True, color_dark)
name3 = solid_font.render(pokemon_3.name, True, color_dark)
name4 = solid_font.render(pokemon_4.name, True, color_dark)
pokemon_1.footprint = pygame.transform.scale(pokemon_1.footprint, (100, 100))
pokemon_2.footprint = pygame.transform.scale(pokemon_2.footprint, (100, 100))
pokemon_3.footprint = pygame.transform.scale(pokemon_3.footprint, (100, 100))
pokemon_4.footprint = pygame.transform.scale(pokemon_4.footprint, (100, 100))
pokemon_box = pygame.image.load(os.path.join('Images', 'Card.png')).convert()
pokemon_box = pygame.transform.scale(pokemon_box, (SCREEN_WIDTH/4, SCREEN_HEIGHT/4))

# Collision detection
pokemon_box_rect_1 = pokemon_box.get_rect(center = (SCREEN_WIDTH/8, SCREEN_HEIGHT/8))
pokemon_box_rect_2 = pokemon_box.get_rect(center = (3*SCREEN_WIDTH/8, SCREEN_HEIGHT/8))
pokemon_box_rect_3 = pokemon_box.get_rect(center = (SCREEN_WIDTH/8, 3*SCREEN_HEIGHT/8))
pokemon_box_rect_4 = pokemon_box.get_rect(center = (3*SCREEN_WIDTH/8, 3*SCREEN_HEIGHT/8))

collision_boxes = [
    pokemon_box_rect_1,
    pokemon_box_rect_2,
    pokemon_box_rect_3,
    pokemon_box_rect_4
]

# Determine which pokemon is in which box
positions = [pokemon_1.position, pokemon_2.position, pokemon_3.position, pokemon_4.position]
pokemon_in_boxes = []

for i in positions: 
    pokemon_in_boxes.append(*[index for index, p, in enumerate(collision_boxes) if p.collidepoint(i)])

###

pokemon_list = [pokemon_1, pokemon_2, pokemon_3, pokemon_4] # List of pokemon generated, in order 
width = screen.get_width()
height = screen.get_height()
  
running = True
while running:
    clock.tick(60)
    mouse = tuple(pygame.mouse.get_pos())

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False

        #checks if a mouse is clicked
        if event.type == pygame.MOUSEBUTTONDOWN:
            screen.fill((0,0,0))
            
            pos = pygame.mouse.get_pos()

            clicked_sprites = [index for index, p, in enumerate(collision_boxes) if p.collidepoint(pos)] # See which box was clicked
            pokemon_clicked = pokemon_in_boxes.index(*clicked_sprites) # Reverse engineer which pokemon was clicked from box number

            pokemon_list[pokemon_clicked].pressed = True # Allow footprint to appear

            if pokemon_list[pokemon_clicked].correct == True:
                print("Correct!")
            else:
                print("Wrong")

    screen.blit(background, (SCREEN_WIDTH-BG_WIDTH ,0))
    screen.blit(background_2, (0, SCREEN_HEIGHT/2))
    screen.blit(footprint_image, BG_center)
    pygame.display.flip()

    screen.blit(pokemon_box, pokemon_boxes[0])
    screen.blit(pokemon_box, pokemon_boxes[1])
    screen.blit(pokemon_box, pokemon_boxes[2])
    screen.blit(pokemon_box, pokemon_boxes[3])

    screen.blit(pokemon_1.sprite, pokemon_1.position)
    name_1_rect = name1.get_rect(center = tuple_subtraction(pokemon_1.position, (-30, -120)))
    screen.blit(name1, name_1_rect)

    if pokemon_1.pressed == True:
        footprint_rect = pokemon_1.footprint.get_rect(center = tuple_subtraction(pokemon_1.position, (-220, -50)))
        screen.blit(pokemon_1.footprint, footprint_rect)

    screen.blit(pokemon_2.sprite, pokemon_2.position)
    name_2_rect = name2.get_rect(center = tuple_subtraction(pokemon_2.position, (-30, -120)))
    screen.blit(name2, name_2_rect)

    if pokemon_2.pressed == True:
        footprint_rect = pokemon_2.footprint.get_rect(center = tuple_subtraction(pokemon_2.position, (-220, -50)))
        screen.blit(pokemon_2.footprint, footprint_rect)

    screen.blit(pokemon_3.sprite, pokemon_3.position)
    name_3_rect = name3.get_rect(center = tuple_subtraction(pokemon_3.position, (-30, -120)))
    screen.blit(name3, name_3_rect)

    if pokemon_3.pressed == True:
        footprint_rect = pokemon_3.footprint.get_rect(center = tuple_subtraction(pokemon_3.position, (-220, -50)))
        screen.blit(pokemon_3.footprint, footprint_rect)

    screen.blit(pokemon_4.sprite, pokemon_4.position)
    name_4_rect = name4.get_rect(center = tuple_subtraction(pokemon_4.position, (-30, -120)))
    screen.blit(name4, name_4_rect)
    if pokemon_4.pressed == True:
        footprint_rect = pokemon_4.footprint.get_rect(center = tuple_subtraction(pokemon_4.position, (-220, -50)))
        screen.blit(pokemon_4.footprint, footprint_rect)

    pygame.display.flip()

pygame.quit()
