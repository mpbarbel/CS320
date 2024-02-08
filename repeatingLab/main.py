# Determine if a list is made up of a repeating pattern

import math  # Optional and you can delete this line if not useful


# Subroutines if any, go here


# Fill in repeat


def repeat(list):

    if list is None:
        return None
    elif len(list) == 0:
        return None
    elif len(list) == 1:
        return None

    elif len(list) > 1:
        pattern_length = math.floor(len(list) / 2)
        pattern = list[0:pattern_length]
        i = pattern_length

        while True:

            if pattern == list[i:i + pattern_length] and i < len(list) - pattern_length:
                i = i + pattern_length
                continue

            elif pattern == list[i:i + pattern_length] and pattern_length == (len(list) - i):
                return pattern

            else:
                pattern = pattern[0:pattern_length - 1]
                pattern_length = pattern_length - 1
                i = pattern_length
                if pattern_length < 1:
                    return None


