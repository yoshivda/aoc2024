import math
import re
import time
from re import match

from lib import load_input


def solve(data):
    # return part_one(data.split('\n\n'))
    return part_two(data.split('\n\n'))


def part_one(data):
    a, b, c = map(int, re.findall('\d+', data[0]))
    program = list(map(int, re.findall('\d+', data[1])))
    return ','.join(map(str, run(a, b, c, program)))

def run(a, b, c, program):
    i = 0
    output = []

    def get_combo(x):
        if 0 <= x <= 3:
            return x
        if x == 4:
            return a
        if x == 5:
            return b
        if x == 6:
            return c
        print('nope')

    def adv(op):
        nonlocal a
        op = get_combo(op)
        a = a // 2 ** op

    def bxl(op):
        nonlocal b
        b = b ^ op

    def bst(op):
        nonlocal b
        b = get_combo(op) % 8

    def jnz(op):
        nonlocal i
        if a != 0:
            i = op - 2

    def bxc(op):
        nonlocal b
        b = b ^ c

    def out(op):
        output.append(get_combo(op) % 8)

    def bdv(op):
        nonlocal b
        b = a // 2 ** get_combo(op)

    def cdv(op):
        nonlocal c
        c = a // 2 ** get_combo(op)

    ops = [adv, bxl, bst, jnz, bxc, out, bdv, cdv]

    while i < len(program):
        opcode, operand = program[i], program[i + 1]
        ops[opcode](operand)
        i += 2
    return output

def part_two(data):
    a, b, c = map(int, re.findall('\d+', data[0]))
    program = list(map(int, re.findall('\d+', data[1])))

    ans = math.inf
    todo = [(0, 0)]
    while todo:
        i, res = todo.pop()
        if i == len(program):
            continue
        for x in range(8):
            a = res * 8 + x
            run_res = run(a, b, c, program)
            if len(run_res) == i + 1 and run_res[0] == program[-i-1]:
                if i == len(program) - 1:
                    ans = min(ans, a)
                todo.append((i + 1, res * 8 + x))
    return ans


if __name__ == '__main__':
    # print(solve(load_input('small')))
    print(solve(load_input('small2')))
    start = time.time()
    print(solve(load_input()))
    print(time.time() - start)
