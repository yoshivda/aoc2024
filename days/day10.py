import time
from functools import cache

from lib import load_input


def solve(data):
    # return part_one(data.splitlines())
    return part_two(data.splitlines())


def part_one(data):
    res = 0
    for x, y in ((x, y) for x in range(len(data[0])) for y in range(len(data)) if data[y][x] == '0'):
        todo = [(x, y, 0)]
        ends = set()
        while todo:
            x, y, v = todo.pop()
            if v == 9:
                ends.add((x, y))
            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                if (0 <= x + dx < len(data[0]) and 0 <= y + dy < len(data)
                        and (new_v := data[y + dy][x + dx]).isnumeric() and int(new_v) == v + 1):
                    todo.append((x + dx, y + dy, int(new_v)))
        res += len(ends)
    return res


def part_two(data):
    @cache
    def can_find_path_from(start):
        x, y = start
        v = int(data[y][x])
        if v == 9:
            return 1
        return sum(can_find_path_from((x + dx, y + dy)) for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1))
                   if (0 <= x + dx < len(data[0]) and 0 <= y + dy < len(data)
                       and (new_v := data[y + dy][x + dx]).isnumeric() and int(new_v) == v + 1))

    return sum(can_find_path_from((x, y)) for x in range(len(data[0])) for y in range(len(data)) if data[y][x] == '0')


if __name__ == '__main__':
    # print(solve(load_input('small')))
    print(solve(load_input('small_pt2')))
    print(solve(load_input('medium')))
    start = time.time()
    print(solve(load_input()))
    print(time.time() - start)
