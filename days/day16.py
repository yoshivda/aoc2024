import time
from queue import PriorityQueue

from lib import load_input


def solve(data):
    # return part_one(data.splitlines())
    return part_two(data.splitlines())


def part_one(data):
    dir = 1
    x, y = next((x, y) for y in range(len(data)) for x in range(len(data[0])) if data[y][x] == 'S')
    return dist_to_end(x, y, dir, data)[0]


def dist_to_end(x, y, dir, data, end='E'):
    q = PriorityQueue()
    q.put((0, (x, y, dir)))
    bests = dict()
    dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    while not q.empty():
        dist, (x, y, dir) = q.get()
        if (x, y, dir) in bests and bests.get((x, y, dir)) < dist:
            continue
        bests[(x, y, dir)] = dist
        if data[y][x] == end and (end == 'E' or dir == 1):
            return dist, bests
        dx, dy = dirs[dir]
        if data[y + dy][x + dx] != '#':
            npos = x + dx, y + dy, dir
            if npos not in bests or bests.get((x + dx, y + dy, dir)) > dist + 1:
                q.put((dist + 1, npos))
        for npos in [(x, y, (dir + 1) % 4), (x, y, (dir - 1) % 4)]:
            if npos not in bests or bests.get(npos) > dist + 1000:
                q.put((dist + 1000, npos))


def part_two(data):
    dir = 1
    x, y = next((x, y) for y in range(len(data)) for x in range(len(data[0])) if data[y][x] == 'S')
    total_dist, bests = dist_to_end(x, y, dir, data)
    x, y = next((x, y) for y in range(len(data)) for x in range(len(data[0])) if data[y][x] == 'E')
    reverse_bests = min((dist_to_end(x, y, i, data, end='S') for i in range(4)), key=lambda x: x[0])[1]
    tiles = set()
    for (x, y, dir), dist in bests.items():
        if dist + (reverse_bests.get((x, y, (dir + 2) % 4)) or 0) == total_dist:
            tiles.add((x, y))
    return len(tiles)


if __name__ == '__main__':
    print(solve(load_input('small')))
    print(solve(load_input('medium')))
    start = time.time()
    print(solve(load_input()))
    print(time.time() - start)
