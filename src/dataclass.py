from dataclasses import dataclass
import pygame
@dataclass
class Pokemon:
    """
        Object hierarchy representation of a Pokemon
    """
    name : str
    position : tuple
    sprite : pygame.surface.Surface
    footprint : pygame.surface.Surface
    correct : bool
    pressed : bool

