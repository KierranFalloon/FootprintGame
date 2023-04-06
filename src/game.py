import cython_utils.c_utils as c
from utils import TestRequirements, generate_pokemon, tuple_subtraction
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

    w, t, r = c.read_stats()

    def new_pokemon() -> None:
        """ Generates new random Pokémon choices, rendering their names and sprites from API.

        Returns:
            pokemon_1 pokemon_2, pokemon_3, pokemon_4 : Pokemon class containing all info of chosen Pokemon
            name1, name2, name3, name4 : Rendered names of pokemon 1, 2, 3 and 4 respectively
            footprint_image : Rendered footprint sprite
            pokemon_in_boxes : List of box indexes which Pokemon are in
            pokemon_list : List of Pokemon
        """

        global pokemon_1, pokemon_2, pokemon_3, pokemon_4, name1, name2, name3, name4, footprint_image, pokemon_in_boxes, pokemon_list

        # Pokemon sprites and names
        pokemon_1, pokemon_2, pokemon_3, pokemon_4 = generate_pokemon()

        # Pokemon footprint definition
        footprint_image = pygame.transform.scale(pokemon_4.footprint, (200, 200))
        name1 = solid_font.render(pokemon_1.name, None, color)
        name2 = solid_font.render(pokemon_2.name, None, color)
        name3 = solid_font.render(pokemon_3.name, None, color)
        name4 = solid_font.render(pokemon_4.name, None, color)
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

    def update_screen() -> None:

        """ Updates the screen in parts, rather than updating entire screen each time something is changed or rendered
        """

        screen.blit(pokemon_1.sprite, pokemon_1.position)
        name_1_rect = name1.get_rect(center = tuple_subtraction(pokemon_1.position, (-50,-200)))
        screen.blit(name1, name_1_rect)

        if pokemon_1.pressed is True:
            footprint_rect = pokemon_1.footprint.get_rect(center = tuple_subtraction(pokemon_1.position, (-275, -110)))
            screen.blit(pokemon_1.footprint, footprint_rect)

        screen.blit(pokemon_2.sprite, pokemon_2.position)
        name_2_rect = name2.get_rect(center = tuple_subtraction(pokemon_2.position, (-50,-200)))
        screen.blit(name2, name_2_rect)

        if pokemon_2.pressed is True:
            footprint_rect = pokemon_2.footprint.get_rect(center = tuple_subtraction(pokemon_2.position, (-275, -110)))
            screen.blit(pokemon_2.footprint, footprint_rect)

        screen.blit(pokemon_3.sprite, pokemon_3.position)
        name_3_rect = name3.get_rect(center = tuple_subtraction(pokemon_3.position, (-50, -200)))
        screen.blit(name3, name_3_rect)

        if pokemon_3.pressed is True:
            footprint_rect = pokemon_3.footprint.get_rect(center = tuple_subtraction(pokemon_3.position, (-275, -110)))
            screen.blit(pokemon_3.footprint, footprint_rect)

        screen.blit(pokemon_4.sprite, pokemon_4.position)
        name_4_rect = name4.get_rect(center = tuple_subtraction(pokemon_4.position, (-50, -200)))
        screen.blit(name4, name_4_rect)
        if pokemon_4.pressed is True:
            footprint_rect = pokemon_4.footprint.get_rect(center = tuple_subtraction(pokemon_4.position, (-275, -110)))
            screen.blit(pokemon_4.footprint, footprint_rect)

        if mouse_in_boxes != []:
            screen.blit(pokemon_box_highlight, collision_boxes[mouse_in_boxes[0]])

        pygame.display.update(foot_zone)
        pygame.display.update(boxes)

    def make_text(text) -> list:
        """ Create an array of text for multi-line rendering

        Args:
            text (str): Text you wish to render

        Returns:
            label (list): List of text, rendered to pygame text
        """

        label = []
        for line in text: 
            label.append(text_font.render(line, True, color))

        return label

    def change_text(label) -> None:
        """ Adds to the screen each instance of text within 'label', generated from make_text

        Args:
            label (list): List of text, rendered to pygame text (output of make_text())
        """
 
        screen.blit(text_box, (SCREEN_WIDTH/2, 3*SCREEN_HEIGHT/4))

        position = [SCREEN_WIDTH/2+50, 3*SCREEN_HEIGHT/4+50]

        for index, line in enumerate(label):
            screen.blit(label[index],(position[0],position[1]+(index*fontsize)+(15*index)))
    
    pygame.mixer.pre_init()
    pygame.mixer.init()
    pygame.init()
    clock = pygame.time.Clock()

    solid_font = pygame.font.Font('Fonts/PokemonSolid.ttf',25)
    fontsize = 50
    text_font = pygame.font.Font('Fonts/PKMN-Mystery-Dungeon.ttf', fontsize)

    pygame.mixer.music.load("Sounds/Music.mp3")
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(loops=-1, fade_ms=500)

    pokemon_box_highlight_sound = pygame.mixer.Sound('Sounds/5.wav')
    correct_sound = pygame.mixer.Sound('Sounds/7.wav')
    incorrect_sound = pygame.mixer.Sound('Sounds/3.wav')

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

    # Background utils
    bg = pygame.image.load(os.path.join('Images', 'Background.png')).convert()
    bg2 = pygame.image.load(os.path.join('Images', 'Background_2.png')).convert()

    BG_WIDTH = (SCREEN_WIDTH/2)
    BG_HEIGHT = 0.75 * SCREEN_HEIGHT

    background = pygame.transform.scale(bg, (BG_WIDTH, BG_HEIGHT))
    ratio = (background.get_size()[0]/bg.get_size()[0], background.get_size()[1]/bg.get_size()[1])
    BG_center = ((SCREEN_WIDTH - (BG_WIDTH/2) - 100),  (SCREEN_HEIGHT - (BG_HEIGHT) - 50))

    background_2 = pygame.transform.smoothscale(bg2, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
    pokemon_boxes = [(0,0), (SCREEN_WIDTH/4,0), (0,SCREEN_HEIGHT/4), (SCREEN_WIDTH/4,SCREEN_HEIGHT/4)]
    text_box = pygame.image.load(os.path.join('Images', 'text_box_blank.png')).convert_alpha()
    text_box = pygame.transform.smoothscale(text_box, (SCREEN_WIDTH/2, SCREEN_HEIGHT/4))

    # Timer screen utils
    red_timer = pygame.image.load(os.path.join('Images', 'Red_timer.png')).convert_alpha()
    red_timer = pygame.transform.smoothscale(red_timer, (red_timer.get_size()[0]*ratio[0], red_timer.get_size()[1]*ratio[1]))
    green_timer = pygame.image.load(os.path.join('Images', 'Green_timer.png')).convert_alpha()
    green_timer = pygame.transform.smoothscale(green_timer, (green_timer.get_size()[0]*ratio[0], green_timer.get_size()[1]*ratio[1]))
    timer_positions = [(1300 + i * 50, 775) for i in range(10)]

    # Pokemon box utils
    pokemon_box = pygame.image.load(os.path.join('Images', 'Card.png')).convert_alpha()
    pokemon_box = pygame.transform.smoothscale(pokemon_box, (SCREEN_WIDTH/4, SCREEN_HEIGHT/4))

    pokemon_box_highlight = pygame.image.load(os.path.join('Images', 'Highlight.png')).convert_alpha()
    pokemon_box_highlight = pygame.transform.smoothscale(pokemon_box_highlight, (SCREEN_WIDTH/4, SCREEN_HEIGHT/4))

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

    new_pokemon() # Generate initial Pokemon

    game_text_correct_strings = [
        ["KF: .... Yep! Looks like you're right to me!"],
        ["KF: Heard ya! Come on in, visitor!"]
    ]
    
    game_text_incorrect_strings = [
        ["KF: .... Huh?! Looks wrong to me!"],
        ["KF: Huh? I don't think so. Try again!"],
    ]

    running = True 
    delay = False # Text based delay
    delay_time = 1000
    win = False # win condition, used for resetting pokemon
    lose = False
    temp = [] # temporary box tracker to check if mouse switches between box
    count = 0
    timer_event = pygame.USEREVENT
    pygame.time.set_timer(timer_event, 3000)
    ### Game running
    while running:
        clock.tick(30)
        mouse = tuple(pygame.mouse.get_pos())
        mouse_in_boxes = [index for index, p, in enumerate(collision_boxes) if p.collidepoint(mouse)]

        event = pygame.event.poll()

        if event.type == pygame.QUIT or event.type == pygame.K_ESCAPE:

            c.add_stats(w, t)
            running = False
            pygame.quit()

        if mouse_in_boxes == []: # If not hovering a pokemon choice
            if temp != []:
                pygame.mixer.Channel(0).play(pokemon_box_highlight_sound, loops = 0)
                temp = []

            text_string = ["KF: Here comes a Pokémon! Check out it's footprint",
                            "and tell me what species is!"]

        #checks if a mouse is clicked INSIDE of a box
        if mouse_in_boxes != []:
            if mouse_in_boxes[0] != temp:
                pygame.mixer.Channel(0).play(pokemon_box_highlight_sound, loops = 0)
                temp = mouse_in_boxes[0]

            pokemon_hovering = pokemon_list[pokemon_in_boxes.index(mouse_in_boxes[0])].name
            text_string = ["KF: Is this pokemon {}?".format(str(pokemon_hovering))]

            if event.type == pygame.MOUSEBUTTONDOWN:
                clicked_sprites = [index for index, p, in enumerate(collision_boxes) if p.collidepoint(mouse)] # See which box was clicked
                pokemon_clicked = pokemon_in_boxes.index(*clicked_sprites) # Reverse engineer which pokemon was clicked from box number

                text_string = ["The footprint is {}'s!".format(str(pokemon_list[pokemon_clicked].name)),
                                "The footprint is {}'s!".format(str(pokemon_list[pokemon_clicked].name))]
                delay = True
                update_screen()

                pokemon_list[pokemon_clicked].pressed = True # Allow footprint to appear

                if pokemon_list[pokemon_clicked].correct is True: # If correct pokemon
                    multi = threading.Thread(target=new_pokemon)
                    multi.start()
                    pygame.mixer.Channel(1).play(correct_sound)
                    text_string = random.choice(game_text_correct_strings)
                    delay = True
                    win = True
                    w += 1
                    t += 1
                    pokemon_list[pokemon_clicked].pressed = True
                    pygame.display.update(boxes)
                    c.add_stats(w, t)
                
                else:

                    pygame.mixer.Channel(2).play(incorrect_sound)
                    text_string = random.choice(game_text_incorrect_strings)
                    delay = True
                    t += 1
                    c.add_stats(w, t)
                    pokemon_list[pokemon_clicked].pressed = True
    

        game_text_out_of_time_strings = [
            ["KF: Out of time! Pick up the pace!"], 
            ["The correct answer is {}!".format(*[i.name for i in pokemon_list if i.correct is True]),
            "Buck up and snap out of it!"]]

        stats_text = "P: {}, T: {}, {}".format(w, t, str(round(float(w)/float(t)*100, 1)))
        stats_rendered = solid_font.render(stats_text, True, color_light)

        if count is 10:
            text_string = random.choice(game_text_out_of_time_strings)
            multi = threading.Thread(target=new_pokemon)
            multi.start()
            lose = True
            delay_time = 2000
            delay = True

        screen.blit(background, (SCREEN_WIDTH-BG_WIDTH, 0))
        screen.blit(background_2, (0, SCREEN_HEIGHT/2))
        screen.blit(footprint_image, BG_center)
        screen.blit(stats_rendered, (1700, 100))
        #screen.blit(clock_img, (1000, 650))

        for index, coordinate in enumerate(timer_positions[0:10-count]):
            screen.blit(green_timer, coordinate)
        for index2, coordinate2 in enumerate(timer_positions[10-count:10]):
            screen.blit(red_timer, coordinate2)
        if event.type == timer_event and count < 10:
            count += 1
        
        pygame.display.update(foot_zone)

        screen.blit(pokemon_box, pokemon_boxes[0])
        screen.blit(pokemon_box, pokemon_boxes[1])
        screen.blit(pokemon_box, pokemon_boxes[2])
        screen.blit(pokemon_box, pokemon_boxes[3])

        if delay is False:
            label = make_text(text_string)
            change_text(label)
            update_screen()
        
        if delay is True:
            init_time = pygame.time.get_ticks()
            while not pygame.time.get_ticks() > delay_time + init_time:
                label = make_text(text_string)
                change_text(label)
                update_screen()
            delay = False
            if win is True:
                count = 0
                update_screen() # See above - New pokemon are generated in a parallel thread once the correct box is pressed
                win = False
            if lose is True:
                count = 0
                lose = False
                update_screen()
            
    pygame.quit()

main()
