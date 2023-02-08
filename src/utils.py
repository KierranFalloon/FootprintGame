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

SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 900
pokemon_boxes = [(0,0), (SCREEN_WIDTH/4,0), (0,SCREEN_HEIGHT/4), (SCREEN_WIDTH/4,SCREEN_HEIGHT/4)]

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
    return list_of_files()

def tuple_subtraction(tuple1, tuple2):
    return tuple(map(lambda i, j: i - j, tuple1, tuple2))

def surf_from_url(other_pokemon):
    image_url = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon" # Open source pokemon sprites
    image_files = []
    for i in range(4):
        image_str = urlopen(os.path.join(image_url, str(other_pokemon[i])+'.png')).read()
        # create a file object (stream)
        image_files.append(io.BytesIO(image_str))
    pokemon_1 = pygame.image.load(image_files[0])
    pokemon_2 = pygame.image.load(image_files[1])
    pokemon_3 = pygame.image.load(image_files[2])
    chosen_pokemon = pygame.image.load(image_files[3])

    return pokemon_1, pokemon_2, pokemon_3, chosen_pokemon

def name_from_api(number) -> str:
    pokemon_api = "https://pokeapi.co/api/v2/pokemon/{}".format(number)
    return str(requests.get(pokemon_api).json()["name"])

def tuple_checker(coordinates, box) -> bool: 

    return all([(a > b) for a, b in zip(coordinates, box)])

def generate_pokemon(footprint):

    # Pokemon sprites and names
    other_pokemon = random.sample(get_pokemon(), 3)
    other_pokemon.append(footprint) # initially 4th pokemon in the list is the correct one

    # Get pokemon names and footprints
    pokemon_1_name = name_from_api(other_pokemon[0])
    pokemon_1_footprint = pygame.image.load(os.path.join('Sprites', str(other_pokemon[0])+'.png')).convert()

    pokemon_2_name = name_from_api(other_pokemon[1])
    pokemon_2_footprint = pygame.image.load(os.path.join('Sprites', str(other_pokemon[1])+'.png')).convert()

    pokemon_3_name = name_from_api(other_pokemon[2])
    pokemon_3_footprint = pygame.image.load(os.path.join('Sprites', str(other_pokemon[2])+'.png')).convert()

    pokemon_4_name = name_from_api(other_pokemon[3])
    pokemon_4_footprint = pygame.image.load(os.path.join('Sprites', str(other_pokemon[3])+'.png')).convert()

    pokemon_1_sprite, pokemon_2_sprite, pokemon_3_sprite, pokemon_4_sprite = surf_from_url(other_pokemon) #sprites

    v_offset = 70
    h_offset = 75
    positions = [(h_offset, v_offset), (SCREEN_WIDTH/4 + h_offset, v_offset), (h_offset, SCREEN_HEIGHT/4 + v_offset), (SCREEN_WIDTH/4 + h_offset,SCREEN_HEIGHT/4 + v_offset)]
    
    rand_pokemon_positions = random.sample(positions, 4)
    pokemon_1_position = rand_pokemon_positions[0]
    pokemon_2_position = rand_pokemon_positions[1]
    pokemon_3_position = rand_pokemon_positions[2]
    pokemon_4_position = rand_pokemon_positions[3]

    pokemon_1 = Pokemon(pokemon_1_name, pokemon_1_position, pokemon_1_sprite, pokemon_1_footprint, False, False)
    pokemon_2 = Pokemon(pokemon_2_name, pokemon_2_position, pokemon_2_sprite, pokemon_2_footprint, False, False)
    pokemon_3 = Pokemon(pokemon_3_name, pokemon_3_position, pokemon_3_sprite, pokemon_3_footprint, False, False)
    pokemon_4 = Pokemon(pokemon_4_name, pokemon_4_position, pokemon_4_sprite, pokemon_4_footprint, True, False)

    return pokemon_1, pokemon_2, pokemon_3, pokemon_4