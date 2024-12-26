import time
from collections import defaultdict
from zipimport import MAX_COMMENT_LEN

from lib import load_input


def solve(data):
    # return part_one(data.splitlines())
    return part_two(data.splitlines())


def part_one(data):
    neighbours = defaultdict(set)
    for line in data:
        a, b = line.split('-')
        neighbours[a].add(b)
        neighbours[b].add(a)

    triplets = set()
    for a, nb in neighbours.items():
        for b in nb:
            for c in nb.intersection(neighbours[b]):
                if a.startswith('t') or b.startswith('t') or c.startswith('t'):
                    triplets.add(tuple(sorted((a, b, c))))
    return len(triplets)


def part_two(data):
    neighbours = defaultdict(set)
    for line in data:
        a, b = line.split('-')
        neighbours[a].add(b)
        neighbours[b].add(a)

    triplets = set()
    for a, nb in neighbours.items():
        for b in nb:
            for c in nb.intersection(neighbours[b]):
                    triplets.add(frozenset([a, b, c]))

    groups = triplets.copy()
    seen = set()
    ress = set()
    while groups:
        group = groups.pop()
        found_bigger = False
        for a in neighbours.keys():
            if a not in group and all(a in neighbours[b] for b in group) and (new_group := frozenset(group | {a})) not in seen:
                found_bigger = True
                groups.add(new_group)
                seen.add(new_group)
        if not found_bigger:
            ress.add(group)

    return ','.join(sorted(max(ress, key=len)))


if __name__ == '__main__':
    # print(solve(load_input('small')))
    print(solve(load_input('small2')))
    start = time.time()
    print(solve(load_input()))
    print(time.time() - start)
