from dataclasses import dataclass

@dataclass
class Pokemon:
    """
        Object hierarchy representation of a Pokemon
    """
    name : str
    position : tuple
    sprite : None
    footprint : None
    correct : bool
    pressed : bool

