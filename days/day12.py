import time
from collections import deque, defaultdict

from lib import load_input


def solve(data):
    # return part_one(data.splitlines())
    return part_two(data.splitlines())


def part_one(data):
    seen = set()
    res = 0
    grid = defaultdict(lambda: '-', {(x, y): data[y][x] for x in range(len(data[0])) for y in range(len(data))})
    for (x, y) in list(grid.keys()):
        if (x, y) not in seen:
            res += bfs(x, y, grid, seen)
    return res


def bfs(x, y, grid, seen):
    q = deque([(x, y)])
    letter = grid[(x, y)]
    surface = 0
    perimeter = 0
    while q:
        x, y = q.pop()
        if (x, y) in seen:
            continue
        seen.add((x, y))
        surface += 1
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if grid[(nx, ny)] == letter:
                if (nx, ny) not in seen:
                    q.append((nx, ny))
            else:
                perimeter += 1
    return surface * perimeter


def part_two(data):
    seen = set()
    res = 0
    grid = defaultdict(lambda: '-', {(x, y): data[y][x] for x in range(len(data[0])) for y in range(len(data))})
    for (x, y) in list(grid.keys()):
        if (x, y) not in seen:
            res += bfs2(x, y, grid, seen)
    return res


def bfs2(x, y, grid, seen):
    q = deque([(x, y)])
    letter = grid[(x, y)]
    surface = 0
    corners = 0
    while q:
        x, y = q.pop()
        if (x, y) in seen:
            continue
        seen.add((x, y))
        surface += 1
        corners += sum([
            int(grid[hn] == letter and grid[vn] == letter and grid[dn] != letter)  # inside corner
            + int(grid[hn] != letter and grid[vn] != letter)  # outside corner
        for hn, vn, dn in [
                ((x - 1, y), (x, y - 1), (x - 1, y - 1)),
                ((x + 1, y), (x, y - 1), (x + 1, y - 1)),
                ((x + 1, y), (x, y + 1), (x + 1, y + 1)),
                ((x - 1, y), (x, y + 1), (x - 1, y + 1)),
            ]])
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if grid[(nx, ny)] == letter and (nx, ny) not in seen:
                    q.append((nx, ny))
    return surface * corners

if __name__ == '__main__':
    print(solve(load_input('small')))
    print(solve(load_input('e')))
    start = time.time()
    print(solve(load_input()))
    print(time.time() - start)
