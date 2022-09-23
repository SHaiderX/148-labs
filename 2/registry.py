from typing import *

class Registry:
    racers: Dict[str, any]

    def __init__(self) -> None:
        self.racers = {}

    def add_racer(self, name: str, email: str, speed: int) -> None:
        pass
