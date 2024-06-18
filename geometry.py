import math

"""!
@file geometry.py
@brief This module provides basic geometric operations.
"""


def rectangle_area(length, width):
    """!
    Return the area of a rectangle.

    @param length The length of the rectangle.
    @param width The width of the rectangle.
    @return The area of the rectangle.
    """
    if length < 0 or width < 0:
        raise ValueError("A distance cannot be negative")
    return length * width

def rectangle_perimeter(length, width):
    """!
    Return the perimeter of a rectangle.

    @param length The length of the rectangle.
    @param width The width of the rectangle.
    @return The perimeter of the rectangle.
    """
    if length < 0 or width < 0:
        raise ValueError("A distance cannot be negative")
    return 2 * (length + width)

def circle_area(radius):
    """!
    Return the area of a circle.

    @param radius The radius of the circle.
    @return The area of the circle.
    """
    if radius < 0:
        raise ValueError("A distance cannot be negative")
    return math.pi * radius * radius

def circle_circumference(radius):
    """!
    Return the circumference( of a circle.

    @param radius The radius of the circle.
    @return The circumference( of the circle.
    """
    if radius < 0:
        raise ValueError("A distance cannot be negative")
    return 2 * math.pi * radius