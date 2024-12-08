import time
from itertools import combinations

from lib import load_input


def solve(data):
    # return part_one(data.splitlines())
    return part_two(data.splitlines())


def part_one(data):
    return len({(x1 + i * dx, y1 + i * dy)
                for i in (-1, 2)
                for coords in ants.values()
                for (x1, y1), (x2, y2) in combinations(coords, 2)
                if (dx := x2 - x1) and (dy := y2 - y1)
                and 0 <= x1 + i * dx < len(data[0]) and 0 <= y1 + i * dy < len(data)}) \
        if (ants := {letter: [(x, y) for x in range(len(data[0])) for y in range(len(data))
                              if data[y][x] == letter]
                     for letter in set(''.join(data)) - {'.'}}) \
        else 0


def part_two(data):
    return len({(x1 - i * dx, y1 - i * dy)
                for i in range(-35, 35)
                for coords in ants.values()
                for (x1, y1), (x2, y2) in combinations(coords, 2)
                if (dx := x2 - x1) and (dy := y2 - y1)
                and 0 <= x1 - i * dx < len(data[0]) and 0 <= y1 - i * dy < len(data)}) \
        if (ants := {letter: [(x, y) for x in range(len(data[0])) for y in range(len(data))
                              if data[y][x] == letter]
                     for letter in set(''.join(data)) - {'.'}}) \
        else 0


if __name__ == '__main__':
    print(solve(load_input('small')))
    start = time.time()
    print(solve(load_input()))
    print(time.time() - start)
