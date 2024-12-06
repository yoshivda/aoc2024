import time

from lib import load_input


def solve(data):
    # return part_one(data.splitlines())
    return part_two(data.splitlines())


def part_one(data):
    obst = {(x, y) for x in range(len(data[0])) for y in range(len(data)) if data[y][x] == '#'}
    y = next(i for i in range(len(data)) if '^' in data[i])
    x = next(i for i in range(len(data[0])) if data[y][i] == '^')
    return len(walk(obst, (x, y), len(data[0]), len(data)))


def part_two(data):
    obst = {(x, y) for x in range(len(data[0])) for y in range(len(data)) if data[y][x] == '#'}
    y = next(i for i in range(len(data)) if '^' in data[i])
    x = next(i for i in range(len(data[0])) if data[y][i] == '^')
    seen = walk(obst, (x, y), len(data[0]), len(data))

    res = 0
    for cx, cy in seen - {(x, y)}:
        new_obst = obst | {(cx, cy)}
        if walk(new_obst, (x, y), len(data[0]), len(data), True):
            res += 1
    return res


def walk(obst, start, max_x, max_y, check_loops=False):
    x, y = start
    dir = 0
    dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    seen = set()
    while 0 <= x < max_x and 0 <= y < max_y:
        if check_loops and (x, y, dir) in seen:
            return True
        seen.add((x, y, dir))
        new_x, new_y = x + dirs[dir][0], y + dirs[dir][1]
        while (new_x, new_y) in obst:
            dir = (dir + 1) % 4
            new_x, new_y = x + dirs[dir][0], y + dirs[dir][1]
        x, y = new_x, new_y
    if check_loops:
        return False
    return {(x, y) for (x, y, _) in seen}

if __name__ == '__main__':
    print(solve(load_input('small')))
    start = time.time()
    print(solve(load_input()))
    print(time.time() - start)
