from dataclasses import dataclass

from breakout_game.const import Const

class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

@dataclass
class Score(metaclass=Singleton):
    current_score: int = 0

    def reset(self):
        self.current_score = 0
    
    def add_score(self, increment):
        self.current_score += increment
    
    def is_win(self):
        return self.current_score == Const.max_score