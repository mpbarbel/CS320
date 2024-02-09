import math

from main import binary_search


def test_binary_search():
    my_list = [4, 4, 6, 6, 7, 9, 10, 11, 12, 13, 14, 19, 26, 26, 27, 28, 33, 33, 35, 38, 39, 41, 47, 49, 49, 50, 53, 54, 55, 56, 57, 59, 60, 61, 67, 68, 68, 72, 78, 78, 79, 80, 82, 87, 89, 90, 92, 93, 93, 99]
    target = 5
    left = 0
    right = len(my_list)
    mid = math.floor((left + right) / 2)
    result = (binary_search(my_list, target, left, right))
    assert result == my_list.index(target)

def test_highest_high():

     my_list = [4, 4, 6, 6, 7, 9, 10, 11, 12, 13,
                  14, 19, 26, 26, 27, 28, 33, 33,
                  35, 38, 39, 41, 47, 49, 49, 50,
                  53, 54, 55, 56, 57, 59, 60, 61,
                  67, 68, 68, 72, 78, 78, 79, 80,
                  82, 87, 89, 90, 92, 93, 93, 99]

    hi = binary_search(my_list, 78, left = 0, len(my_list))





