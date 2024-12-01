import time
from collections import Counter

from lib import load_input


def solve(data):
    # return part_one(data.splitlines())
    return part_two(data.splitlines())


def part_one(data):
    return sum(abs(t[0] - t[1]) for t in zip(*(sorted(int(line.split()[i]) for line in data) for i in (0, 1))))


def part_two(data):
    return sum(n * Counter([int(line.split()[1]) for line in data])[n] for n in (int(line.split()[0]) for line in data))


if __name__ == '__main__':
    print(solve(load_input('small')))
    start = time.time()
    print(solve(load_input()))
    print(time.time() - start)
