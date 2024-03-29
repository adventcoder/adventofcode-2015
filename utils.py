from dataclasses import dataclass
import re

def get_input(day):
    with open(f'inputs/day{day}.txt', 'r') as file:
        return file.read()

def ints(s):
    return map(int, re.findall(r'-?[0-9]+', s))

@dataclass(frozen=True)
class Interval:
    min: int
    max: int

    def __len__(self):
        return self.max - self.min + 1 if self.min <= self.max else 0

    def __add__(self, n):
        return Interval(self.min + n, self.max + n)

    def __sub__(self, n):
        return Interval(self.min - n, self.max - n)

    def __or__(self, other):
        return Interval(min(self.min, other.min), max(self.max, other.max))

    def __and__(self, other):
        return Interval(max(self.min, other.min), min(self.max, other.max))
