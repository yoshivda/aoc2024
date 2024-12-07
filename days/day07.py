import time
from lib import load_input


def solve(data):
    # return part_one(data.splitlines())
    return part_two(data.splitlines())


def part_one(data):
    return sum(total
               for total, nums in [(int(line.split(':')[0]), tuple(int(x) for x in line.split()[:0:-1])) for line in data]
               if can_sum_to(nums, total))


def part_two(data):
    return sum(total
               for total, nums in [(int(line.split(':')[0]), tuple(int(x) for x in line.split()[:0:-1])) for line in data][::-1]
               if can_sum_to(nums, total, True))


def can_sum_to(nums, total, pt2=False):
    print(nums, total)
    if total < 0:
        return False
    if len(nums) == 1:
        return nums[0] == total
    return (can_sum_to(nums[1:], total - nums[0], pt2)
            or (total % nums[0] == 0 and can_sum_to(nums[1:], total // nums[0], pt2))
            or (pt2 and str(total).endswith(str(nums[0])) and can_sum_to(nums[1:], int(str(total)[:-len(str(nums[0]))] or '0'), pt2)))


if __name__ == '__main__':
    print(solve(load_input('small')))
    start = time.time()
    print(solve(load_input()))
    print(time.time() - start)
