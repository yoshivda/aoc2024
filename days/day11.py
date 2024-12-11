import time
from collections import Counter, defaultdict

from lib import load_input


def solve(data):
    # return part_one(data.strip())
    return part_two(data.strip())


def part_one(data):
    stone_nums = [int(x) for x in data.split()]
    stones = Counter(stone_nums)
    for i in range(25):
        stones = blink(stones)
    return sum(stones.values())


def blink(stones):
    res = defaultdict(int)
    for stone, freq in stones.items():
        if stone == 0:
            res[1] += freq
        elif len(str(stone)) % 2 == 0:
            res[int(str(stone)[:len(str(stone))//2])] += freq
            res[int(str(stone)[len(str(stone))//2:])] += freq
        else:
            res[stone * 2024] += freq
    return res


def part_two(data):
    stone_nums = [int(x) for x in data.split()]
    stones = Counter(stone_nums)
    for i in range(75):
        stones = blink(stones)
    return sum(stones.values())


if __name__ == '__main__':
    # print(solve(load_input('small')))
    print(solve(load_input('medium')))
    start = time.time()
    print(solve(load_input()))
    print(time.time() - start)
