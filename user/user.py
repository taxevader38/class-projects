from map.map import Locations
import random

class User:
    def __init__(self, name: str, location: str = None):
        self.name = name
        self.world = Locations()

        if location is None:
            self.location = random.choice(list(self.world.map.keys()))
        else:
            self.location = location.lower()

    def get_name(self) -> str:
        return self.name
