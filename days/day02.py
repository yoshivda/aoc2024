import time

from lib import load_input


def solve(data):
    # return part_one(data.splitlines())
    return part_two(data.splitlines())


def part_one(data):
    return sum(all(line[i + 1] - 3 <= line[i] < line[i + 1] for i in range(len(line) - 1))
               or all(line[i + 1] + 3 >= line[i] > line[i + 1] for i in range(len(line) - 1))
       for line in mapped) \
        if (mapped := [[int(x) for x in line.split()] for line in data]) else 0


def part_two(data):
    return sum(
        any(
            all(spliced_line[i + 1] - 3 <= spliced_line[i] < spliced_line[i + 1] for i in range(len(spliced_line) - 1))
            or all(spliced_line[i + 1] + 3 >= spliced_line[i] > spliced_line[i + 1] for i in range(len(spliced_line) - 1))
            for spliced_line in [orig_line[:i] + orig_line[i + 1:] if i < len(orig_line) else [] for i in range(len(orig_line))])
        for orig_line in mapped) \
        if (mapped := [[int(x) for x in line.split()] for line in data]) else 0


if __name__ == '__main__':
    print(solve(load_input('small')))
    start = time.time()
    print(solve(load_input()))
    print(time.time() - start)
