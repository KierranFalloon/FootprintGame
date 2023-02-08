"""Test availability of required packages."""

import unittest
from pathlib import Path
import pkg_resources
import os
import io
from urllib.request import urlopen
import pygame
import requests

_REQUIREMENTS_PATH = Path(__file__).parent.with_name("requirements.txt")

# white color
color = (255,255,255)
  
# light shade of the button
color_light = (170,170,170)
  
# dark shade of the button
color_dark = (100,100,100)

class TestRequirements(unittest.TestCase):
    """Test availability of required packages."""

    def test_requirements(self):
        """Test that each required package is available."""
        requirements = pkg_resources.parse_requirements(_REQUIREMENTS_PATH.open())
        for requirement in requirements:
            requirement = str(requirement)
            with self.subTest(requirement=requirement):
                pkg_resources.require(requirement)

def list_of_files():
    pokemon_list = []
    path = os.path.join(os.getcwd(), 'Sprites')
    files = [int(f.split('.')[0]) for f in os.listdir(path)]
    return files

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

    return all([(a > b) for a, b in zip(coordinates,box)])