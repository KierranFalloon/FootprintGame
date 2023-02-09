from dataclass import Pokemon
from utils import TestRequirements, tuple_checker, generate_pokemon, get_pokemon, tuple_subtraction, read_stats, add_stats
from utils import color_dark, color, color_light
import threading
try:
    TestRequirements().test_requirements()
except Exception as e:
    print(e)
    exit()

import pygame
from pygame.locals import *
import os
import random
import threading

def main():

    w, t, r = read_stats()
    def new_pokemon():
        global pokemon_1, pokemon_2, pokemon_3, pokemon_4, name1, name2, name3, name4, footprint_image, pokemon_in_boxes, pokemon_list

        # Pokemon sprites and names
        pokemon_1, pokemon_2, pokemon_3, pokemon_4 = generate_pokemon()

        # Pokemon footprint definition
        footprint_image = pygame.transform.scale(pokemon_4.footprint, (200, 200))
        name1 = solid_font.render(pokemon_1.name, None, color_dark)
        name2 = solid_font.render(pokemon_2.name, None, color_dark)
        name3 = solid_font.render(pokemon_3.name, None, color_dark)
        name4 = solid_font.render(pokemon_4.name, None, color_dark)
        pokemon_1.footprint = pygame.transform.scale(pokemon_1.footprint, (100, 100))
        pokemon_2.footprint = pygame.transform.scale(pokemon_2.footprint, (100, 100))
        pokemon_3.footprint = pygame.transform.scale(pokemon_3.footprint, (100, 100))
        pokemon_4.footprint = pygame.transform.scale(pokemon_4.footprint, (100, 100))

        # Determine which pokemon is in which box
        positions = [pokemon_1.position, pokemon_2.position, pokemon_3.position, pokemon_4.position]
        pokemon_in_boxes = []

        for i in positions: 
            pokemon_in_boxes.append(*[index for index, p, in enumerate(collision_boxes) if p.collidepoint(i)])

        ###

        pokemon_list = [pokemon_1, pokemon_2, pokemon_3, pokemon_4] # List of pokemon generated, in order 

    def update_screen():
        screen.blit(pokemon_1.sprite, pokemon_1.position)
        name_1_rect = name1.get_rect(center = tuple_subtraction(pokemon_1.position, (0, -200)))
        screen.blit(name1, name_1_rect)

        if pokemon_1.pressed == True:
            footprint_rect = pokemon_1.footprint.get_rect(center = tuple_subtraction(pokemon_1.position, (-250, -100)))
            screen.blit(pokemon_1.footprint, footprint_rect)

        screen.blit(pokemon_2.sprite, pokemon_2.position)
        name_2_rect = name2.get_rect(center = tuple_subtraction(pokemon_2.position, (0, -200)))
        screen.blit(name2, name_2_rect)

        if pokemon_2.pressed == True:
            footprint_rect = pokemon_2.footprint.get_rect(center = tuple_subtraction(pokemon_2.position, (-250, -100)))
            screen.blit(pokemon_2.footprint, footprint_rect)

        screen.blit(pokemon_3.sprite, pokemon_3.position)
        name_3_rect = name3.get_rect(center = tuple_subtraction(pokemon_3.position, (0, -200)))
        screen.blit(name3, name_3_rect)

        if pokemon_3.pressed == True:
            footprint_rect = pokemon_3.footprint.get_rect(center = tuple_subtraction(pokemon_3.position, (-250, -100)))
            screen.blit(pokemon_3.footprint, footprint_rect)

        screen.blit(pokemon_4.sprite, pokemon_4.position)
        name_4_rect = name4.get_rect(center = tuple_subtraction(pokemon_4.position, (0, -200)))
        screen.blit(name4, name_4_rect)
        if pokemon_4.pressed == True:
            footprint_rect = pokemon_4.footprint.get_rect(center = tuple_subtraction(pokemon_4.position, (-250, -100)))
            screen.blit(pokemon_4.footprint, footprint_rect)

        if mouse_in_boxes != []:
            screen.blit(pokemon_box_highlight, collision_boxes[mouse_in_boxes[0]])

        pygame.display.update(foot_zone)
        pygame.display.update(boxes)

    def make_text():

        global text_change
        text_change = text_font.render(text_string, True, color)

    def change_text():
 
        screen.blit(text_box, (SCREEN_WIDTH/2, 3*SCREEN_HEIGHT/4))
        screen.blit(text_change, (SCREEN_WIDTH/2+50, 3*SCREEN_HEIGHT/4+50))
    
    pygame.mixer.init()
    pygame.init()
    clock = pygame.time.Clock()

    hollow_font = pygame.font.Font('Fonts/PokemonHollow.ttf',25)
    solid_font = pygame.font.Font('Fonts/PokemonSolid.ttf',25)
    text_font = pygame.font.Font('Fonts/PKMN-Mystery-Dungeon.ttf', 50)

    pygame.mixer.music.load("Music.mp3")
    pygame.mixer.music.play(loops=-1)
    pygame.display.set_caption("Footprint game!")
    clock = pygame.time.Clock()

    infoObject = pygame.display.Info()
    # Set up the drawing window
    SCREEN_WIDTH = infoObject.current_w
    SCREEN_HEIGHT = infoObject.current_h

    flags =  DOUBLEBUF | RESIZABLE
    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT], flags, 16)

    foot_zone = pygame.Rect(SCREEN_WIDTH/2, 0, SCREEN_WIDTH/2, SCREEN_HEIGHT)
    boxes = pygame.Rect(0, 0, SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    bg = pygame.image.load(os.path.join('Images', 'Background.png')).convert_alpha()
    bg2 = pygame.image.load(os.path.join('Images', 'Background_2.png')).convert_alpha()

    BG_WIDTH = (SCREEN_WIDTH/2)
    BG_HEIGHT = 0.75 * SCREEN_HEIGHT

    background = pygame.transform.scale(bg, (BG_WIDTH, BG_HEIGHT))
    BG_center = ((SCREEN_WIDTH - (BG_WIDTH/2) - 100),  (SCREEN_HEIGHT - (BG_HEIGHT) - 50))

    background_2 = pygame.transform.scale(bg2, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
    pokemon_boxes = [(0,0), (SCREEN_WIDTH/4,0), (0,SCREEN_HEIGHT/4), (SCREEN_WIDTH/4,SCREEN_HEIGHT/4)]
    text_box = pygame.image.load(os.path.join('Images', 'text_box_blank.png')).convert_alpha()
    text_box = pygame.transform.scale(text_box, (SCREEN_WIDTH/2, SCREEN_HEIGHT/4))
    #text_box_size = text_box.get_rect(center = other_center)

    pokemon_box = pygame.image.load(os.path.join('Images', 'Card.png')).convert_alpha()
    pokemon_box = pygame.transform.scale(pokemon_box, (SCREEN_WIDTH/4, SCREEN_HEIGHT/4))

    pokemon_box_highlight = pygame.image.load(os.path.join('Images', 'Highlight.png')).convert_alpha()
    pokemon_box_highlight = pygame.transform.scale(pokemon_box_highlight, (SCREEN_WIDTH/4, SCREEN_HEIGHT/4))

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

    new_pokemon()

    game_text_correct_strings = [
        "KF: .... Yep! Looks like you're right to me!",
        "KF: Heard ya! Come on in, visitor!"

    ]
    
    game_text_incorrect_strings = [
        "KF: .... Huh?! Looks wrong to me!",
        "KF: Huh? I don't think so. Try again!",
    ]
    running = True
    delay = False
    win = False
    while running:
        clock.tick(30)
        mouse = tuple(pygame.mouse.get_pos())
        mouse_in_boxes = [index for index, p, in enumerate(collision_boxes) if p.collidepoint(mouse)]

        event = pygame.event.poll()

        if event.type == pygame.QUIT or event.type == pygame.K_ESCAPE:

            add_stats(w, t)
            running = False
            pygame.quit()

        if mouse_in_boxes == []: # If not hovering a pokemon choice
            text_string = "KF: Here comes a Pokémon! Check its footprint and tell me what it is!"
            name_text = text_font.render(text_string, True, color)

        #checks if a mouse is clicked INSIDE of a box
        if mouse_in_boxes != []:

            pokemon_hovering = pokemon_list[pokemon_in_boxes.index(mouse_in_boxes[0])].name
            text_string = "KF: Is this pokemon {}?".format(str(pokemon_hovering))

            if event.type == pygame.MOUSEBUTTONDOWN:
                clicked_sprites = [index for index, p, in enumerate(collision_boxes) if p.collidepoint(mouse)] # See which box was clicked
                pokemon_clicked = pokemon_in_boxes.index(*clicked_sprites) # Reverse engineer which pokemon was clicked from box number

                text_string = "The footprint is {}'s! The footprint is {}'s!".format(str(pokemon_list[pokemon_clicked].name), str(pokemon_list[pokemon_clicked].name))
                delay = True
                update_screen()

                pokemon_list[pokemon_clicked].pressed = True # Allow footprint to appear

                if pokemon_list[pokemon_clicked].correct == True: # If correct pokemon

                    text_string = random.choice(game_text_correct_strings)
                    delay = True
                    win = True
                    w += 1
                    t += 1
                    pokemon_list[pokemon_clicked].pressed = True
                    pygame.display.update(boxes)
                    add_stats(w, t)
                
                else:

                    text_string = random.choice(game_text_incorrect_strings)
                    delay = True

                    t += 1
                    add_stats(w, t)
                    pokemon_list[pokemon_clicked].pressed = True
        
        screen.blit(background, (SCREEN_WIDTH-BG_WIDTH, 0))
        screen.blit(background_2, (0, SCREEN_HEIGHT/2))
        screen.blit(footprint_image, BG_center)
        pygame.display.update(foot_zone)

        screen.blit(pokemon_box, pokemon_boxes[0])
        screen.blit(pokemon_box, pokemon_boxes[1])
        screen.blit(pokemon_box, pokemon_boxes[2])
        screen.blit(pokemon_box, pokemon_boxes[3])

        if delay == False:
            make_text()
            change_text()
            update_screen()
        
        if delay == True:
            init_time = pygame.time.get_ticks()
            while not pygame.time.get_ticks() > 5000 + init_time:
                make_text()
                change_text()
                update_screen()
            delay = False
            if win == True:
                new_pokemon()
                update_screen()
                win = False

    pygame.quit()

main()