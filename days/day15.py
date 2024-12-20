import time

from lib import load_input


def solve(data):
    # return part_one(*data.split('\n\n'))
    return part_two(*data.split('\n\n'))


def part_one(map, instructions):
    map = map.splitlines()
    walls = {(x, y) for x in range(len(map[0])) for y in range(len(map)) if map[y][x] == '#'}
    boxes = {(x, y) for x in range(len(map[0])) for y in range(len(map)) if map[y][x] == 'O'}

    def move(x, y, dx, dy):
        nonlocal boxes
        x += dx
        y += dy
        to_move = set()
        while True:
            if (x, y) in walls:
                return False
            elif (x, y) in boxes:
                to_move.add((x, y))
                x += dx
                y += dy
            else:
                boxes -= to_move
                boxes |= {(bx + dx, by + dy) for bx, by in to_move}
                return True

    x, y = next((x, y) for x in range(len(map[0])) for y in range(len(map)) if map[y][x] == '@')

    instructions = instructions.replace('\n', '')
    for c in instructions:
        dx, dy = [(0, -1), (0, 1), (-1, 0), (1, 0)]['^v<>'.index(c)]
        if move(x, y, dx, dy):
            x += dx
            y += dy
    return sum(x + 100 * y for x, y in boxes)


def part_two(map, instructions):
    map = map.replace('#', '##').replace('O', '[]').replace('.', '..').replace('@', '@.').splitlines()
    walls = {(x, y) for x in range(len(map[0])) for y in range(len(map)) if map[y][x] == '#'}
    boxes = {(x, y) for x in range(len(map[0])) for y in range(len(map)) if map[y][x] == '['}

    def move(x, y, dx, dy):
        nonlocal boxes
        to_move = set()
        to_check = [(x + dx, y + dy)]
        while to_check:
            x, y = to_check.pop()
            if (x, y) in walls:
                return False
            elif (x, y) in boxes:
                to_move.add((x, y))
                if dy:
                    to_check.append((x, y + dy))
                    to_check.append((x + 1, y + dy))
                elif dx == 1:
                    to_check.append((x + 2, y))
                else:
                    to_check.append((x - 1, y))
            elif (x - 1, y) in boxes:
                to_move.add((x - 1, y))
                if dy:
                    to_check.append((x - 1, y + dy))
                    to_check.append((x, y + dy))
                elif dx == 1:
                    to_check.append((x + 1, y))
                else:
                    to_check.append((x - 2, y))
        boxes -= to_move
        boxes |= {(bx + dx, by + dy) for bx, by in to_move}
        return True

    x, y = next((x, y) for x in range(len(map[0])) for y in range(len(map)) if map[y][x] == '@')

    instructions = instructions.replace('\n', '')
    for c in instructions:
        dx, dy = [(0, -1), (0, 1), (-1, 0), (1, 0)]['^v<>'.index(c)]
        if move(x, y, dx, dy):
            x += dx
            y += dy
    return sum(x + 100 * y for x, y in boxes)


if __name__ == '__main__':
    # print(solve(load_input('small')))
    # print(solve(load_input('small2')))
    print(solve(load_input('medium')))
    start = time.time()
    print(solve(load_input()))
    print(time.time() - start)
