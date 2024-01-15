from utils import get_input
from functools import cache
from math import inf

def subset_sum(nums, target):
    @cache
    def recur(n, s):
        # Returns the minimum size subset as well as the minimum entanglement within, of all the subsets of nums[:n] that sum to s.
        if s == 0:
            return 1, 0 # empty subset
        elif n == 0:
            return inf, inf # no subsets found
        else:
            # subsets without nums[n-1]
            res = recur(n - 1, s)
            if nums[n - 1] <= s:
                # subsets with nums[n-1]
                res = merge(*res, add(*recur(n - 1, s - nums[n - 1]), nums[n-1]))
            return res
    return recur(len(nums), target)[0]

def add(entanglement, size, num):
    return entanglement * num, size +  1

def merge(entanglement1, size1, entanglement2, size2):
    if size1 < size2:
        return entanglement1, size1
    if size2 < size1:
        return entanglement2, size2
    # min size subsets are the same so get the minimum entanglement from either
    return min(entanglement1, entanglement2), size1 # == size2

nums = list(map(int, get_input(24).splitlines()))
total = sum(nums)
print('1.', subset_sum(nums, total // 3))
print('2.', subset_sum(nums, total // 4))
