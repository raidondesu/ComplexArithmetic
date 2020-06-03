from testing import exercise
from typing import Tuple

import math

Complex = Tuple[float, float]
Polar = Tuple[float, float]

# Imaginary Numbers
# x^2 = -1 (X has no solution among real numbers)
# i^2 = -1 (So instead we say there exists some number that solves that equation) (An imaginary unit)
# i + i = 2i, i - i = 0, (-1)(i) = -i, (-i)^2 = -1
#
# Powers of i
# Input : an even integer n
# Goal : Return the nth power of i, or i^n
@exercise
def imaginary_power(n : int) -> int:
    # If n is divisible by 4
    if n % 4 == 0:
        return 1
    else:
        return -1 