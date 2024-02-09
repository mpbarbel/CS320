# extract values from a sorted list

import math  # optional and you can delete this line if not useful


# subroutines if any, go here

def binary_search(list, target, left, right):
    if left > right:
        return left
    mid = math.floor((left + right) / 2)
    if list[mid] == target:
        return mid
    elif target > list[mid]:
        left = mid + 1
        return binary_search(list, target, left, right)
    elif target < list[mid]:
        right = mid - 1
        return binary_search(list, target, left, right)


def find_highest_index(list, hi):
    if hi > len(list) - 1:
        hi = hi - 1
    if hi == len(list) - 1:
        return hi
    while list[hi] == list[hi + 1]:
        hi = hi + 1
        if hi == len(list) - 1:
            return hi
    return hi


def find_lowest_index(list, lo_index):
    if lo_index == 0:
        return lo_index
    while lo_index > 0 and [lo_index] == list[lo_index - 1]:
        lo_index = lo_index - 1
    return lo_index


def check_high_index(list_s, hi, high_index):
    while high_index > 0 and hi < list_s[high_index]:
        high_index = high_index - 1
    if high_index == 0 and hi < list_s[high_index]:
        return -1
    return high_index


def check_low_index(list_s, lo, lo_index):
    if lo_index == len(list_s):
        lo_index = lo_index - 1
    while lo_index < len(list_s) - 1 and lo > list_s[lo_index]:
        lo_index = lo_index + 1
    if lo_index == len(list_s) - 1 and lo > list_s[lo_index]:
        return -1
    return lo_index


def assign_range_list(list, lo, hi):
    range_list = list[lo: hi + 1]
    return range_list


def assign_target_range_low_index(list, lo):
    low = binary_search(list, lo, left=0, right=len(list) - 1)
    lowest_index = find_lowest_index(list, low)
    lowest_index = check_low_index(list, lo, lowest_index)
    return lowest_index


def assign_target_range_high_index(list, hi):
    high = binary_search(list, hi, left=0, right=len(list) - 1)
    highest_index = find_highest_index(list, high)
    highest_index = check_high_index(list, hi, highest_index)
    return highest_index


# your subroutine goes here
def extract(list_s, lo, hi):
    if hi is None and lo is None:
        return list_s
    elif list_s is None:
        return None
    elif lo is None:
        lo = list_s[0]
    elif hi is None:
        hi = list_s[len(list_s) - 1]
    elif lo > hi:
        return None
    elif len(list_s) == 0:
        return list_s
    elif len(list_s) == 1:
        if lo <= list_s[0] and hi < list_s[0]:
            return []
    low_index = assign_target_range_low_index(list_s, lo)
    if low_index == -1:
        return []
    high_index = assign_target_range_high_index(list_s, hi)
    if high_index == -1:
        return []
    range_list = assign_range_list(list_s, low_index, high_index)
    return range_list
