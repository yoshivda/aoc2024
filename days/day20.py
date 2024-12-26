import time
from collections import deque

from lib import load_input


def solve(data):
    # return part_one(data.splitlines())
    return part_two(data.splitlines())


def part_one(data):
    start = next(((x, y) for x in range(len(data[0])) for y in range(len(data)) if data[y][x] == 'S'))
    end = next(((x, y) for x in range(len(data[0])) for y in range(len(data)) if data[y][x] == 'E'))
    dist_from_start = bfs(data, *start)
    dist_from_end = bfs(data, *end)
    min_dist = dist_from_end[start]

    return sum(find_cheat(dist, dist_from_end, 2, x, y, min_dist if len(data) == 15 else min_dist - 99)
               for (x, y), dist in dist_from_start.items())

def bfs(data, x, y):
    dists = dict()
    seen = set()
    q = deque([(x, y, 0)])
    while q:
        x, y, dist = q.popleft()
        if (x, y) in seen:
            continue
        seen.add((x, y))
        dists[(x, y)] = dist
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if data[ny][nx] != '#' and (nx, ny) not in seen:
                q.append((nx, ny, dist + 1))
    return dists


def find_cheat(cur_dist, dist_from_end, num_cheats, x, y, min_dist):
    return sum((ndist := abs(nx - x) + abs(ny - y)) <= num_cheats and cur_dist + ndist + dist < min_dist for (nx, ny), dist in dist_from_end.items())


def part_two(data):
    start = next(((x, y) for x in range(len(data[0])) for y in range(len(data)) if data[y][x] == 'S'))
    end = next(((x, y) for x in range(len(data[0])) for y in range(len(data)) if data[y][x] == 'E'))
    dist_from_start = bfs(data, *start)
    dist_from_end = bfs(data, *end)
    min_dist = dist_from_end[start]

    return sum(find_cheat(dist, dist_from_end, 20, x, y, min_dist - 49 if len(data) == 15 else min_dist - 99)
               for (x, y), dist in dist_from_start.items())

if __name__ == '__main__':
    print(solve(load_input('small')))
    start = time.time()
    print(solve(load_input()))
    print(time.time() - start)
