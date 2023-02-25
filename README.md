# Footprint Game
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Python based Pokémon Footprint game! This game is based on the [Sentry Duty](https://pokemon.fandom.com/wiki/Sentry_Duty) guild job present in Pokémon Mystery Dungeon Explorers of Sky and Pokémon Mystery Dungeon Explorers of Time and Darkness games. However, this is extended up to Generation VIII (8). This project has no affiliation with Nintendo or the Pokémon Company; Pokémon and Pokémon character names are trademarks of Nintendo, and Pokémon sprites within are Copyright (c) The Pokémon Company.

<img width="1280" alt="game_screenshot" src="https://user-images.githubusercontent.com/71852543/219865530-4e4e8903-0186-4c1d-a2e4-e0c51e425a88.png">



## Requirements

| Requirement | Version |
|:-----------|-------|
| Python | &ge; 3.7.16 |
| setuptools | &ge; 65.6.3 |
| pygame | &ge; 2.1.2 |
| requests | &ge; 2.28.2 |
| Cython (optional) | &ge; 0.29.33 |

## Installation

This is developed in Python 3.9.16, though theoretically it can work with any version of Python greater than 3.7, given there are no clashes for the dependencies. For this reason I recommend using a virtual environment, for instance through `conda`, to install this and avoid dependency clashing. However, if dependencies (see [*Requirements*](requirements.txt)) are already met, this can be skipped.

- To begin, create a conda environment - `conda create -n myenv python=3.9` replacing 'myenv' with the desired name of the environment. Clone or fork this repository, and `cd` to the location of the directory. **Note, if Cython is not installed on the system, a working C compiler such as `gcc` must be installed. Simply use `conda install Cython` if this causes issues.**
- From this directory, activate the environment created with `conda activate myenv`
- Run `python setup.py build_ext --inplace install`. This uses the setup.py and requirements.txt file to `pip install` the (missing) requirements and compile the Cython / C code to an importable Python module. A log file is printed to catch errors if necessary.

## Usage
Launch the game through `python src/game.py`.

## Acknowledgements

### Developer

<table>
  <tr>
    <td align="center"><a href="https://github.com/KierranFalloon"><img src="https://avatars.githubusercontent.com/u/71852543?v=4" width="100px;" alt=""/><br /><sub><b>KierranFalloon</b></sub></a><br /><a href="https://github.com/KierranFalloon/FootprintGame/commits?author=KierranFalloon" title="Code">💻</a> </td>
  </tr>
</table>

This is me! I use this project to learn and develop skills while making something fun - if you would like to support the project, see [**Contributing**](CONTRIBUTING.md).

Below is a list of sources from which I acquired some assets for the game.

| Asset | Location |
|:-----------|:-------:|
| Gen. I-V footprint sprites | [Veekun](https://veekun.com/dex/downloads) |
| Gen. VI - VIII footprint sprites | [Wolf Pokecommunity member](https://www.pokecommunity.com/member.php?u=730428) |
| Pokémon names <br /> Pokémon sprites | [PokeAPI](https://pokeapi.co/) <br /> (&copy; The Pokémon Company) |
