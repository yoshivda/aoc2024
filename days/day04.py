import time

from lib import load_input


def solve(data):
    # return part_one(data.splitlines())
    return part_two(data.splitlines())


def part_one(data):
    return sum(sum(all(data[y + dy * i][x + dx * i] == 'XMAS'[i] for i in range(4))
                   for dx, dy in [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
                   if 0 <= x + 3 * dx < len(data[0])
                   and 0 <= y + 3 * dy < len(data)) for x in range(len(data[0])) for y in range(len(data)))

def part_two(data):
    return sum(''.join(data[y + dy][x + dx] for dx, dy in [(1, 1), (-1, 1), (-1, -1), (1, -1)]) in ('MMSS', 'MSSM', 'SSMM', 'SMMS')
               for x in range(1, len(data[0]) - 1)
               for y in range(1, len(data) - 1)
               if data[y][x] == 'A')

if __name__ == '__main__':
    print(solve(load_input('small')))
    start = time.time()
    print(solve(load_input()))
    print(time.time() - start)
