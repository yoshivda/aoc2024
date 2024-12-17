import math
import re
import time

import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds, linprog

from lib import load_input


def solve(data):
    # return part_one(data.split('\n\n'))
    return part_two(data.split('\n\n'))


def part_one(data):
    res = 0
    for part in data:
        a1, b1, a2, b2, t1, t2 = map(int, re.findall(r'(\d+)', part.replace('\n', '')))
        c = [3, 1]
        constraints = LinearConstraint([[a1, a2], [b1, b2]], [t1, t2], [t1, t2])
        bounds = Bounds((0, 0), (101, 101))
        model = milp(c, constraints=constraints, bounds=bounds, integrality=[1, 1])
        if model.success:
            res += int(sum(np.array(model.x) * np.array([3, 1])))
    return res


# 61654664674597

def part_two(data):
    res = 0
    for part in data:
        a1, b1, a2, b2, t1, t2 = map(int, re.findall(r'(\d+)', part.replace('\n', '')))
        t1 += 10000000000000
        t2 += 10000000000000
        c = [3, 1]
        model = linprog(c, A_eq=[[float(a1), float(a2)], [float(b1), float(b2)]], b_eq=[float(t1), float(t2)], bounds=((0, None), (0, None)))
        if (model.success
                and round(model.x[0]) * a1 + round(model.x[1]) * a2 == t1
                and round(model.x[0]) * b1 + round(model.x[1]) * b2 == t2):
            res += 3 * round(model.x[0]) + round(model.x[1])
    return res


if __name__ == '__main__':
    print(solve(load_input('small')))
    start = time.time()
    print(solve(load_input()))
    print(time.time() - start)
