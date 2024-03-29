import unittest
from pathlib import Path
import pkg_resources

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
color_dark = (100, 100, 100)

def get_pokemon() -> list:
    """ Chooses 4 (pseudo) random Pokémon from the available footprint sprites to be used

    Returns:
        list: List of Pokémon used in the current game instance
    """

    # Define the base URL for the PokeAPI
    POKEAPI_BASE_URL = "https://pokeapi.co/api/v2/"

    # Fetch details for NUM_RANDOM_POKEMON random Pokemon
    random_pokemon_names = []
    for i in range(4):
        # Generate a random Pokemon ID between 1 and 898
        pokemon_id = random.randint(1, 898)

        # Make the API request to retrieve the Pokemon details
        pokemon_url = f"{POKEAPI_BASE_URL}pokemon/{pokemon_id}"
        response = requests.get(pokemon_url).json()

        # Extract the name of the default form
        name = response["species"]["url"]

        # Check if the Pokemon has any other available forms
        forms_url = response["forms"][0]["url"]
        forms_response = requests.get(forms_url).json()
        forms = [form["name"] for form in forms_response.get("forms", [])]

        # If the Pokemon has any other available forms, choose a random one
        if len(forms) > 1:
            chosen_form = random.choice(forms)
            name = chosen_form["url"]

        name = name.split("/")[-2]
        random_pokemon_names.append(str(name))

    return random_pokemon_names

    return random_pokemon_names

def surf_from_api(other_pokemon : list) -> pygame.image:
    """ Gets the Pokémon sprites from PokeAPI according to the number chosen, with a 1/4096 chance of choosing a shiny


    Args:
        other_pokemon (list): List of Pokémon chosen from get_pokemon()

    Returns:
        pygame.image: Rendered sprite classes for each chosen Pokémon
    """
    shiny_number = random.randint(1, 4096)
    
    if shiny_number == 1:

        image_url = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/{}.png"
    
    else:
        image_url = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{}.png" # Open source pokemon sprites
    image_files = []
    for i in range(4):
        image_str = urlopen(image_url.format(other_pokemon[i])).read()
        # create a file object (stream)
        image_files.append(io.BytesIO(image_str))
    pokemon_1_img = pygame.image.load(image_files[0]).convert_alpha()
    pokemon_1_img = pygame.transform.scale(pokemon_1_img, (140, 140))
    pokemon_2_img = pygame.image.load(image_files[1]).convert_alpha()
    pokemon_2_img = pygame.transform.scale(pokemon_2_img, (140, 140))
    pokemon_3_img = pygame.image.load(image_files[2]).convert_alpha()
    pokemon_3_img = pygame.transform.scale(pokemon_3_img, (140, 140))
    pokemon_4_img = pygame.image.load(image_files[3]).convert_alpha()
    pokemon_4_img = pygame.transform.scale(pokemon_4_img, (140, 140))

    return pokemon_1_img, pokemon_2_img, pokemon_3_img, pokemon_4_img

def name_from_api(number) -> str:
    """ Gets the Pokémon name from PokeAPI according to the number chosen

    Args:
        number (int): Pokémon pokedex number

    Returns:
        str: The name of the Pokémon from the PokeAPI .json
    """

    pokemon_api = "https://pokeapi.co/api/v2/pokemon/{}".format(number)

    try:
        name = str(requests.get(pokemon_api).json()["name"])
        return name
    except Exception as e:
        print(e, "\n pokemon: {}".format(number))

def generate_pokemon() -> Pokemon:
    """ Uses all information gathered on the Pokémon to create a Pokémon class (from dataclass.py) for each

    Returns:
        Pokemon: Pokemon dataclass
    """

    # Resolution sprite scaling
    infoObject = pygame.display.Info()
    # Set up the drawing window
    SCREEN_WIDTH = infoObject.current_w
    SCREEN_HEIGHT = infoObject.current_h
    pokemon_box = pygame.image.load(os.path.join('Images', 'Card.png')).convert_alpha()
    pokemon_box_2 = pygame.transform.scale(pokemon_box, (SCREEN_WIDTH/4, SCREEN_HEIGHT/4))
    ratio = ((pokemon_box_2.get_size()[0] / pokemon_box.get_size()[0], pokemon_box_2.get_size()[1] / pokemon_box.get_size()[1]))

    # Pokemon sprites and names
    other_pokemon = get_pokemon() # initially 4th pokemon in the list is the correct one

    footprint_api = "https://raw.githubusercontent.com/KierranFalloon/FootprintAPI/main/Sprites/{}.png"

    feet_files = []
    for i in range(4):
        image_str = urlopen(footprint_api.format(other_pokemon[i])).read()
        # create a file object (stream)
        feet_files.append(io.BytesIO(image_str))

    footprint_api = "https://raw.githubusercontent.com/KierranFalloon/FootprintAPI/main/Sprites/{}.png"

    feet_files = []
    for i in range(4):
        image_str = urlopen(footprint_api.format(other_pokemon[i])).read()
        # create a file object (stream)
        feet_files.append(io.BytesIO(image_str))

    # Get pokemon names and footprints
    pokemon_1_name = name_from_api(other_pokemon[0])
    pokemon_1_footprint = pygame.image.load(feet_files[0]).convert_alpha()

    pokemon_2_name = name_from_api(other_pokemon[1])
    pokemon_2_footprint = pygame.image.load(feet_files[1]).convert_alpha()

    pokemon_3_name = name_from_api(other_pokemon[2])
    pokemon_3_footprint = pygame.image.load(feet_files[2]).convert_alpha()

    pokemon_4_name = name_from_api(other_pokemon[3])
    pokemon_4_footprint = pygame.image.load(feet_files[3]).convert_alpha()

    pokemon_1_sprite, pokemon_2_sprite, pokemon_3_sprite, pokemon_4_sprite = surf_from_api(other_pokemon) #sprites

    h_offset = 250 * ratio[0]
    v_offset = 175 * ratio[1]
    positions = [
        (h_offset, v_offset),
        ((SCREEN_WIDTH / 4) + h_offset, v_offset),
        (h_offset, (SCREEN_HEIGHT / 4) + v_offset),
        ((SCREEN_WIDTH / 4) + h_offset, (SCREEN_HEIGHT / 4) + v_offset),
    ]

    rand_pokemon_positions = random.sample(positions, 4)  # Positions randomised
    pokemon_1_position = rand_pokemon_positions[0]
    pokemon_2_position = rand_pokemon_positions[1]
    pokemon_3_position = rand_pokemon_positions[2]
    pokemon_4_position = rand_pokemon_positions[3]

    pokemon_1 = Pokemon(pokemon_1_name, other_pokemon[0], pokemon_1_position, pokemon_1_sprite, pokemon_1_footprint, False, False)
    pokemon_2 = Pokemon(pokemon_2_name, other_pokemon[1], pokemon_2_position, pokemon_2_sprite, pokemon_2_footprint, False, False)
    pokemon_3 = Pokemon(pokemon_3_name, other_pokemon[2], pokemon_3_position, pokemon_3_sprite, pokemon_3_footprint, False, False)
    pokemon_4 = Pokemon(pokemon_4_name, other_pokemon[3], pokemon_4_position, pokemon_4_sprite, pokemon_4_footprint, True, False) # 4th random pokemon is correct

    return pokemon_1, pokemon_2, pokemon_3, pokemon_4

def tuple_subtraction(tuple1 : tuple, tuple2 : tuple) -> tuple:
    """ Subtracts two tuples, useful for transforming sprites on the screen

    Args:
        tuple1 (tuple): Reference tuple (initial coordinates / coordinates currently) (x, y)
        tuple2 (tuple): Transformation tuple (x2, y2)

    Returns:
        tuple: New coordinates of the form (x - x2, y - y2)
    """
    return tuple(map(lambda i, j: i - j, tuple1, tuple2))
    