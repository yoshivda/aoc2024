import re
import time
from collections import defaultdict
from math import prod

from lib import load_input


def solve(data):
    # return part_one(data.splitlines())
    return part_two(data.splitlines())


def part_one(data):
    robots = [tuple(map(int, re.findall(r'(-?\d+)', line))) for line in data]
    positions = defaultdict(int)
    xmax = 101 if len(data) > 12 else 11
    ymax = 103 if len(data) > 12 else 7
    for x, y, dx, dy in robots:
        positions[(x + 100 * dx) % xmax, (y + 100 * dy) % ymax] += 1
    for y in range(ymax):
        for x in range(xmax):
            print(positions[(x, y)] or '.', end='')
        print()
    return prod(sum(v for (x, y), v in positions.items() if lx <= x < ux and ly <= y < uy)
                for lx, ux, ly, uy in [
                    (0,             xmax // 2,  0,              ymax // 2),
                    (0,             xmax // 2,  ymax // 2 + 1,  ymax),
                    (xmax // 2 + 1, xmax,       0,              ymax // 2),
                    (xmax // 2 + 1, xmax,       ymax // 2 + 1,  ymax),
                ])


def part_two(data):
    robots = [list(map(int, re.findall(r'(-?\d+)', line))) for line in data]
    xmax = 101 if len(data) > 12 else 11
    ymax = 103 if len(data) > 12 else 7
    i = 0
    while True:
        i += 1
        positions = set()
        for robot in robots:
            robot[0] = (robot[0] + robot[2]) % xmax
            robot[1] = (robot[1] + robot[3]) % ymax
            positions.add((robot[0], robot[1]))
        if any(len(set(pos[0] for pos in positions if pos[1] == y)) > 30 for y in range(ymax)):
            print(i)
            for y in range(ymax):
                for x in range(xmax):
                    print('#' if (x, y) in positions else '.', end='')
                print()
            input()
        if i % 1000 == 0:
            print(i)


if __name__ == '__main__':
    # print(solve(load_input('small')))
    start = time.time()
    print(solve(load_input()))
    print(time.time() - start)
