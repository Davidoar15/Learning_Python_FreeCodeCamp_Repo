from abc import ABC, abstractmethod
import random

class Player(ABC):
    def __init__(self):
        self.moves = []
        self.position = (0, 0)
        self.path = [self.position]

    def make_move(self):
        move = random.choice(self.moves)

        x, y = self.position
        dx, dy = move
        new_position = (x + dx, y + dy)

        self.position = new_position
        self.path.append(new_position)

        return self.position

    @abstractmethod
    def level_up(self):
        pass
    
class Pawn(Player):
    def __init__(self):
        super().__init__()
        self.moves = [
            (0, 1),
            (0, -1),
            (-1, 0),
            (1, 0)
        ]
    
    def level_up(self):
        diagonals = [
            (1, 1),
            (-1, 1),
            (1, -1),
            (-1, -1)
        ]

        self.moves.extend(diagonals)
