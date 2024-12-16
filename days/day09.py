import time
from math import ceil

from lib import load_input


def solve(data):
    # return part_one(data.strip())
    return part_two(data.strip())


def part_one(data):
    length = 0
    blocks = []
    empties = []
    for i, c in enumerate(data):
        if i % 2 == 0:
            blocks.append((length, i // 2, int(c)))
        else:
            empties.append((length, int(c)))
        length += int(c)

    extras = []
    for i, l in empties:
        while l > 0:
            i2, v, l2 = blocks[-1]
            if i2 < i:
                break
            if l2 <= l:
                extras.append((i, v, l2))
                blocks.pop()
                l -= l2
                i += l2
            else:
                extras.append((i, v, l))
                blocks[-1] = (i2, v, l2 - l)
                # print(blocks)
                l = 0
    total = sorted(blocks + extras, key=lambda t: t[0])
    return sum(sum(j * int(c) for j in range(i, i + l)) for i, c, l in total)


def part_two(data):
    length = 0
    blocks = []
    empties = []
    for i, c in enumerate(data):
        if i % 2 == 0:
            blocks.append([length, i // 2, int(c)])
        else:
            empties.append([length, int(c)])
        length += int(c)

    for block in reversed(blocks):
        i, v, l = block
        for j, e in enumerate(empties):
            e_i, e_l = e
            if e_i > i:
                break
            if l <= e_l:
                e[0] += l
                e[1] -= l
                block[0] = e_i
                break

    total = sorted(blocks, key=lambda t: t[0])
    return sum(sum(j * int(c) for j in range(i, i + l)) for i, c, l in total)

if __name__ == '__main__':
    print(solve(load_input('small')))
    print(solve(load_input('small2')))
    start = time.time()
    print(solve(load_input()))
    print(time.time() - start)
