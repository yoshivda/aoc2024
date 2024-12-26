import time

from mpmath import diffs
from requests.utils import set_environ
from sympy.stats.sampling.sample_numpy import numpy

from lib import load_input


def solve(data):
    # return part_one(data.splitlines())
    return part_two(data.splitlines())


def part_one(data):
    res = 0
    for line in data:
        num = int(line)
        for _ in range(2000):
            num = process(num)
        res += num
    return res


def process(num):
    x = num * 64
    num ^= x
    num %= 16777216

    x = num // 32
    num ^= x
    num %= 16777216

    x = num * 2048
    num ^= x
    num %= 16777216
    return num


def part_two(data):
    states = dict()
    for i, line in enumerate(data):
        states[i] = dict()
        diffs = tuple()
        num = int(line)
        for _ in range(2000):
            new_num = process(num)
            diff = new_num % 10 - num % 10
            if len(diffs) == 4:
                diffs = diffs[1:] + (diff,)
                if diffs not in states[i]:
                    states[i][diffs] = new_num % 10
            else:
                diffs = diffs + (diff,)
            num = new_num
    res = 0
    for state in set.union(*(set(v.keys()) for v in states.values())):
        res = max(res, sum(v.get(state) or 0 for v in states.values()))
    return res


if __name__ == '__main__':
    # print(solve(load_input('small')))
    print(solve(load_input('small2')))
    start = time.time()
    print(solve(load_input()))
    print(time.time() - start)
