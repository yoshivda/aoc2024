import time
from lib import load_input


def solve(data):
    # return part_one(data.splitlines())
    return part_two(data.splitlines())


def part_one(data):
    return sum(total
               for total, nums in [(int(line.split(':')[0]), tuple(int(x) for x in line.split()[1:])) for line in data]
               if can_sum_to(nums, total))


def part_two(data):
    return sum(total
               for total, nums in [(int(line.split(':')[0]), tuple(int(x) for x in line.split()[1:])) for line in data]
               if can_sum_to(nums, total, 0, True))


def can_sum_to(nums, total, acc=0, pt2=False):
    if acc > total:
        return False
    if len(nums) == 0:
        return acc == total
    return (can_sum_to(nums[1:], total, acc + nums[0], pt2)
            or can_sum_to(nums[1:], total, acc * nums[0], pt2)
            or (pt2 and can_sum_to(nums[1:], total, int(str(acc) + str(nums[0])), pt2)))


if __name__ == '__main__':
    print(solve(load_input('small')))
    start = time.time()
    print(solve(load_input()))
    print(time.time() - start)
