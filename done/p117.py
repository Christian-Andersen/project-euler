# Red, Green, and Blue Tiles
from functools import cache


@cache
def f(space_left: int) -> int:
    assert space_left >= 0
    if space_left <= 1:
        return 1
    if space_left == 2:
        return 2  # empty and red
    if space_left == 3:
        return 4  # empty, red left, right right, green
    return f(space_left-1) + f(space_left-2) + f(space_left-3) + f(space_left-4)


print(f(50))
