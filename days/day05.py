import math
import time
from functools import cmp_to_key

from lib import load_input


def solve(data):
    # return part_one(data.split('\n\n'))
    return part_two(data.split('\n\n'))


def part_one(data):
    return sum(
        nums[len(nums) // 2]
        for line in data[1].splitlines()
        if (nums := [int(x) for x in line.split(',')])
        and not any(a in nums and b in nums and nums.index(a) > nums.index(b) for a, b in rules)
    ) if (rules := [tuple(map(int, line.split('|'))) for line in data[0].splitlines()]) else 0

def part_two(data):
    return sum(
        sorted(nums, key=cmp_to_key(lambda x, y: 1 if any(a == y and b == x for a, b in rules) else -1))[len(nums) // 2]
        for line in data[1].splitlines()
        if (nums := [int(x) for x in line.split(',')])
        and any(a in nums and b in nums and nums.index(a) > nums.index(b) for a, b in rules)
    ) if (rules := [tuple(map(int, line.split('|'))) for line in data[0].splitlines()]) else 0



if __name__ == '__main__':
    print(solve(load_input('small')))
    start = time.time()
    print(solve(load_input()))
    print(time.time() - start)
