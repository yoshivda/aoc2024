import re
import time
from math import prod

from lib import load_input


def solve(data):
    # return part_one(data)
    return part_two(data)


def part_one(data):
    return sum(prod(int(x) for x in match.groups()) for match in (re.finditer(r'mul\((\d+),(\d+)\)', data)))


def part_two(data):
    return sum(prod(int(x) for x in match.groups()) for match in
               (re.finditer(r'mul\((\d+),(\d+)\)',
                            re.sub(r'don\'t\(\).*$', '',
                                   re.sub(r'don\'t\(\).*?do\(\)', '',
                                          re.sub('\n', '', data))))))


if __name__ == '__main__':
    print(solve(load_input('small')))
    print(solve(load_input('small2')))
    start = time.time()
    print(solve(load_input()))
    print(time.time() - start)
