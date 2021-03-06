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

# Complex Division
# The next use for the conjugate is complex division
# Lets take two complex numbers
# 1. x = a + bi
# 2. y = c + di != 0
############################
#
# 1 represented as a tuple (a, b)
# 2 represented as a tuple (c, d)
# Goal : Return the result of the division x/y = g + hi
#
############################
@exercise
def complex_div(x: Complex, y : Complex) -> Complex:
    (a, b) = x
    (c, d) = y

    denominator = (c ** 2) + (d ** 2)
    
    real = ((a * c) + (b * d)) / denominator
    imaginary = ((a * (-d)) + (c * b)) / denominator

    return (real, imaginary)

# Modulus - generalizes the absolute value operator on real numbers to the complex plane
# Abosolute value - The distance of a value from zero on a number line
# The modulus of a complex number is its distance from 0 + 0i
############################
# Input : A complex number (x = a + bi) represented as a tuple (a, b)
# Goal : Return the modulus of this number | x |
# Solution : | x | = sqrt(a ** 2 + b ** 2)
# Solve using the pythagorean theorem
############################
@exercise
def modulus(x : Complex) -> float: 
    return math.sqrt(x[0] ** 2 + x[1] ** 2)

# Complex Exponents
# Input : A complex number (x = a + bi) represented by a tuple (a, b)
# Goal : Return the complex number (e ** x =  e ** a + bi) = g + hi represented as a tuple (g, h)
# Eulers constant e is available in the math library, as are pythons trigonometric fuctions
#############################
# (e ** a + bi) = (e ** a)(e ** bi) 
# (e ** a) = real number
# (e ** bi) == (e ** i(theta)) = cos(theta) + i(sin(theta))
# Then subsitute into our expression (e ** a)(cosb + isinb) = (e ** a)(cosb) + (e ** a)(sinbi)
@exercise
def complex_exp(x : Complex) -> Complex:

    (a, b) = x

    expa = math.e ** a
    real = expa * math.cos(b)
    imaginary = expa * math.sin(b)

    return (real, imaginary)

# Complex Powers of real numbers
# Inputs : 
# 1. A non- negative real number (r)
# 2. A complex number (x = a + bi) represented as a tuple (a, b)
# Goal: Return the complex number (r ** x) = (r ** a + bi) = g + hi
@exercise
def complex_exp_real(r : float, x : Complex) -> Complex:
    #Since ln(r) is only defined for positive numbers, we check for this special case.
    #If r = 0, raising it to any power will give 0
    #Calling return before the end of the function will not execute the rest of the function
    if (r == 0):
        return (0, 0)
    
    (a, b) = x

    #Raise r to the power of a
    ra  = r ** a

    # Natural logarithm of r
    lnr = math.log(r)

    real = ra * math.cos(b * lnr)
    imaginary = ra * math.sin(b * lnr)

    return (real, imaginary)

#Cartesian to polar conversion
# Input : A complex number x = a + bi , represented as a tuple (a , b)
# Goal : Return the polar representation of x = (re ** i(theta))
##############################################################
# r should be non-negative : r >= 0
# theta should be between -pi and pi : -pi < theta <= pi
##############################################################
@exercise 
def polar_convert(x : Complex) -> Polar:
    (a, b) = x

    r = math.sqrt(a ** 2 + b ** 2)
    theta = math.atan2(b, a)

    return (r, theta)
##############################################################
##############################################################
# Polar to Cartesian Conversion
# Input : A complex number x = (r ** i(theta)) represented in polar form as a tuple (r, theta)
# Goal : Return the cartesian representation of x = a + bi, represented as a tuple (a, b)
@exercise
def cartesian_convert(x : Polar) -> Complex:
    (r, theta) = x

    real = r * math.cos(theta)
    imaginary = r * math.sin(theta)

    return (real, imaginary)

# Polar Multiplication
# Inputs :
# 1. A complex number x = (r1)(e ** i(theta1)) represented in polar form as a tuple (r1, theta1)
# 2. A complex number y = (r2)(e ** i(theta2)) represented in polar form as a tuple (r2, theta2)
# Goal : Return the result of the multiplication (x)(y) = z = (r3)(e ** i(theta3)) represented in polar form as a tuple (r3, theta3)
# r3 should be non-negative : r3 >= 0
# theta3 should be between -pi and pi: -pi < theta3 <= pi
# Try to avoid converting the numbers into cartesian form
##############################################################
@exercise
def polar_mult(x : Polar, y : Polar) -> Polar:
    (r1, theta1) = x
    (r2, theta2) = y
    
    radius = r1 * r2
    angle = theta1 + theta2

    #If the calculated angle is larger than pi, we will subtract 2pi
    if (angle > math.pi):
        # Reassign the value for angle
        angle = angle - 2.0 * math.pi

    #If the calculated angle is smaller than -pi, we will add 2pi
    elif (angle <= -math.pi):
        angle = angle + 2.0 * math.pi
    
    return (radius, angle)

# Arbitrary complex exponents
# 1. A complex number x = a + bi, represented as a tuple (a, b)
# 2. A complex number y = c + di, represented as a tuple (c, d)
# Goal : Return the result of raising x to the power of y
# (x ** y) = (a + bi) ** (c + di) = z = g + hi represented as a tuple (g, h)
@exercise
def complex_exp_arbitrary(x : Complex, y : Complex) -> Complex: 
    (a, b) = x
    (c, d) = y

    # Convert x to polar form
    r = math.sqrt(a ** 2 + b ** 2)
    theta = math.atan2(b, a)

    # Special case for r = 0
    if (r == 0):
        return (0, 0)
    
    lnr = math.log(r)

    exponent = math.exp(lnr * c - d * theta)

    real = exponent * (math.cos(lnr * d + theta * c))
    imaginary = exponent * (math.sin(lnr * d + theta * c))

    return (real, imaginary)