import time
from functools import cache

from lib import load_input


def solve(data):
    # return part_one(data.split('\n\n'))
    return part_two(data.split('\n\n'))


@cache
def can_make(thing, towels):
    if thing == '':
        return True
    return any(towel == thing[:len(towel)] and can_make(thing[len(towel):], towels) for towel in towels)


def part_one(data):
    towels = frozenset(data[0].split(', '))
    return sum(can_make(line, towels) for line in data[1].splitlines())


@cache
def can_make_sum(thing, towels):
    if thing == '':
        return 1
    return sum(can_make_sum(thing[len(towel):], towels) for towel in towels if towel == thing[:len(towel)])


def part_two(data):
    towels = frozenset(data[0].split(', '))
    return sum(can_make_sum(line, towels) for line in data[1].splitlines())


if __name__ == '__main__':
    print(solve(load_input('small')))
    start = time.time()
    print(solve(load_input()))
    print(time.time() - start)
