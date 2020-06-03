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

#Complex Numbers
######################################################################################################
# Adding a real number to an imaginary number will be partly real and partly imaginary (Complex number)
# A complex number is simply the real part and the imaginary part being treated as a single number
######################################################################################################
# Complex numbers are generally written as the sum of their two parts
# a + bi (both a and b are real numbers)
# For example : 3 + 4i or -5 - 7i are valid complex numbers
#######################################################################################################
# Purely real or purely imaginary numbers can also be written as complex numbers 
# 2 is 2 + 0i and -3i is 0 - 3i
#######################################################################################################
# When performing operations on complex numbers it is helpful to treat them as polynomials in terms of i
#
#Excercise 2: Complex Addition
#######################################################################################################
# 1. A complex number x = a + bi, represented as a tuple (a, b)
# 2. A complex number y = c + di, represented as a tuple (c, d)
# Goal : Return the sum of these two numbers  x + y = z = g + hi, represented as tuple (g, h)

@exercise
def complex_add(x : Complex, y : Complex) -> Complex:
    # You can extract elements from a tuple like this
    a = x[0]
    b = x[1]

    c = y[0]
    d = y[1]

    #This creates a new variable and stores the real component into it
    real = a + c
    # Replace the ... with code to calculate the imaginary component
    imaginary = b + d

    # You can create a tuple like this
    ans = (real, imaginary)

    return ans

#Complex Multiplication
# 1. A complex number x = a + bi, represented as a tuple (a, b)
# 2. A complex number y = c + di, represented as a tuple (c, d)
# Goal: Return the product of these two numbers x * y = g + hi, represented as a tuple (g, h)
######################################################################################################

@exercise 
def complex_mult(x : Complex, y : Complex) -> Complex:
    (a, b) = x
    (c, d) = y

    real = (a * c) - (b *d)
    imaginary = (a * d) + (c * b)

    return (real, imaginary)

# Complex Conjugate - A complex number with an equal real part and an imaginary part equal in magnitude but opposite in sign
# The conjugate is a simple operation : Given a complex number (x = a + bi)
# Conjugate = x* = a - bi
# A complex number multiplied by its conjugate always produces a non-negative real number
# Conjugates distribuyte over both complex addition and multiplication
####
#Complex Conjugate
# Input : A complex number represented as a tuple
# Goal : Return the complex conjugate represented as a tuple

@exercise
def conjugate(x : Complex) -> Complex: 
    real = x[0]
    imaginary = - x[1]

    return (real, imaginary)