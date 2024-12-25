import time
from collections import deque
from symbol import if_stmt

from lib import load_input


def solve(data):
    # return part_one(data.splitlines())
    return part_two(data.splitlines())


def part_one(data):
    is_example = len(data) == 25
    return run(data[:12 if is_example else 1024], is_example)

def run(data, is_example):
    max_len = 6 if is_example else 70
    q = deque([(0, 0, 0)])
    visited = set()
    walls = {tuple(map(int, line.split(','))) for line in data}
    while q:
        x, y, dist = q.popleft()
        if x == max_len and y == max_len:
            return dist
        if (x, y) in visited:
            continue
        visited.add((x, y))
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if ((x + dx, y + dy) not in visited
                    and (x + dx, y + dy) not in walls
                    and 0 <= x + dx <= max_len and 0 <= y + dy <= max_len):
                q.append((x + dx, y + dy, dist + 1))
    return -1


def part_two(data):
    is_example = len(data) == 25
    l = 0
    h = len(data)
    while l < h:
        m = (h + l) // 2 + 1
        if run(data[:m], is_example) == -1:
            h = m - 1
        else:
            l = m
    return data[l]

if __name__ == '__main__':
    print(solve(load_input('small')))
    start = time.time()
    print(solve(load_input()))
    print(time.time() - start)
