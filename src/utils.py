import unittest
from pathlib import Path

_REQUIREMENTS_PATH = Path(__file__).parent.with_name("requirements.txt")

class TestRequirements(unittest.TestCase):
    """Test availability of required packages."""

    def test_requirements(self):
        """Test that each required package is available."""
        requirements = pkg_resources.parse_requirements(_REQUIREMENTS_PATH.open())
        for requirement in requirements:
            requirement = str(requirement)
            with self.subTest(requirement=requirement):
                pkg_resources.require(requirement)

from dataclass import Pokemon
import pkg_resources
import os
import io
from urllib.request import urlopen
import pygame
import requests
import random

# white color
color = (255,255,255)
  
# light shade of the button
color_light = (170,170,170)
  
# dark shade of the button
color_dark = (100,100,100)

def list_of_files():
    pokemon_list = []
    path = os.path.join(os.getcwd(), 'Sprites')
    files = [int(f.split('.')[0]) for f in os.listdir(path)]
    return files

def get_pokemon():
# Setup Pokemon list
    return random.sample(list_of_files(), 4)

def tuple_subtraction(tuple1, tuple2):
    return tuple(map(lambda i, j: i - j, tuple1, tuple2))

def surf_from_url(other_pokemon):
    image_url = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon" # Open source pokemon sprites
    image_files = []
    for i in range(4):
        image_str = urlopen(os.path.join(image_url, str(other_pokemon[i])+'.png')).read()
        # create a file object (stream)
        image_files.append(io.BytesIO(image_str))
    pokemon_1_img = pygame.image.load(image_files[0]).convert_alpha()
    pokemon_1_img = pygame.transform.scale(pokemon_1_img, (150, 150))
    pokemon_2_img = pygame.image.load(image_files[1]).convert_alpha()
    pokemon_2_img = pygame.transform.scale(pokemon_2_img, (150, 150))
    pokemon_3_img = pygame.image.load(image_files[2]).convert_alpha()
    pokemon_3_img = pygame.transform.scale(pokemon_3_img, (150, 150))
    pokemon_4_img = pygame.image.load(image_files[3]).convert_alpha()
    pokemon_4_img = pygame.transform.scale(pokemon_4_img, (150, 150))


    return pokemon_1_img, pokemon_2_img, pokemon_3_img, pokemon_4_img

def name_from_api(number) -> str:
    pokemon_api = "https://pokeapi.co/api/v2/pokemon/{}".format(number)

    name = str(requests.get(pokemon_api).json()["name"])
    if "-" in name and not name == 'mime-jr.':
        name = name.split('-')[0]
    return name

def tuple_checker(coordinates, box) -> bool: 

    return all([(a > b) for a, b in zip(coordinates, box)])

def generate_pokemon():

    # Resolution sprite scaling
    infoObject = pygame.display.Info()
    # Set up the drawing window
    SCREEN_WIDTH = infoObject.current_w
    SCREEN_HEIGHT = infoObject.current_h
    pokemon_boxes = [(0,0), (SCREEN_WIDTH/4,0), (0,SCREEN_HEIGHT/4), (SCREEN_WIDTH/4,SCREEN_HEIGHT/4)]
    pokemon_box = pygame.image.load(os.path.join('Images', 'Card.png')).convert_alpha()
    pokemon_box_2 = pygame.transform.scale(pokemon_box, (SCREEN_WIDTH/4, SCREEN_HEIGHT/4))
    ratio = ((pokemon_box_2.get_size()[0] / pokemon_box.get_size()[0], pokemon_box_2.get_size()[1] / pokemon_box.get_size()[1]))

    # Pokemon sprites and names
    other_pokemon = get_pokemon() # initially 4th pokemon in the list is the correct one

    # Get pokemon names and footprints
    pokemon_1_name = name_from_api(other_pokemon[0])
    pokemon_1_footprint = pygame.image.load(os.path.join('Sprites', str(other_pokemon[0])+'.png')).convert_alpha()

    pokemon_2_name = name_from_api(other_pokemon[1])
    pokemon_2_footprint = pygame.image.load(os.path.join('Sprites', str(other_pokemon[1])+'.png')).convert_alpha()

    pokemon_3_name = name_from_api(other_pokemon[2])
    pokemon_3_footprint = pygame.image.load(os.path.join('Sprites', str(other_pokemon[2])+'.png')).convert_alpha()

    pokemon_4_name = name_from_api(other_pokemon[3])
    pokemon_4_footprint = pygame.image.load(os.path.join('Sprites', str(other_pokemon[3])+'.png')).convert_alpha()

    pokemon_1_sprite, pokemon_2_sprite, pokemon_3_sprite, pokemon_4_sprite = surf_from_url(other_pokemon) #sprites

    h_offset = 250 * ratio[0]
    v_offset = 150 * ratio[1]
    positions = [(h_offset,v_offset), ((SCREEN_WIDTH/4)+h_offset,v_offset), (h_offset,(SCREEN_HEIGHT/4)+v_offset), ((SCREEN_WIDTH/4)+h_offset,(SCREEN_HEIGHT/4)+v_offset)]
    
    rand_pokemon_positions = random.sample(positions, 4) # Positions randomised
    pokemon_1_position = rand_pokemon_positions[0]
    pokemon_2_position = rand_pokemon_positions[1]
    pokemon_3_position = rand_pokemon_positions[2]
    pokemon_4_position = rand_pokemon_positions[3]

    pokemon_1 = Pokemon(pokemon_1_name, other_pokemon[0], pokemon_1_position, pokemon_1_sprite, pokemon_1_footprint, False, False)
    pokemon_2 = Pokemon(pokemon_2_name, other_pokemon[1], pokemon_2_position, pokemon_2_sprite, pokemon_2_footprint, False, False)
    pokemon_3 = Pokemon(pokemon_3_name, other_pokemon[2], pokemon_3_position, pokemon_3_sprite, pokemon_3_footprint, False, False)
    pokemon_4 = Pokemon(pokemon_4_name, other_pokemon[3], pokemon_4_position, pokemon_4_sprite, pokemon_4_footprint, True, False) # 4th random pokemon is correct

    return pokemon_1, pokemon_2, pokemon_3, pokemon_4

def read_stats():
    try:
        with open("stats.txt", "r") as stats:
            wins = int(stats.readline())
            tries = int(stats.readline())
            ratio = float(stats.readline())
        
        return wins, tries, ratio

    except:
        w, t, r = 0, 0, 0
        with open("stats.txt", "w") as stats:
            stats.write(str(w)+"\n"+str(t)+"\n"+str(r))
        
        return w, t, r

def add_stats(w, t):
    ratio = float((int(w) / int(t)) * 100)
    with open("stats.txt", "w+") as stats:
        stats.write(str(w)+"\n"+str(t)+"\n"+str(ratio))