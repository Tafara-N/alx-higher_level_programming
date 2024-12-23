#!/usr/bin/python3

"""
A class Rectangle that defines a rectangle by: (based on 7-rectangle.py)
"""


class Rectangle:
    """
    Compare rectangles

    Attributes:
        number_of_instances (int): The number of Rectangle instances.
        print_symbol (any): The symbol used for string representation.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initializing a new Rectangle

        Args:
            width (int): The new rectangle's width
            height (int): The new rectangle's height
        """

        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Sets the width of the rectangle
        """

        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Sets the height of the rectangle
        """

        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Returns the area of the rectangle
        """

        return self.__width * self.__height

    def perimeter(self):
        """
        Returns the perimeter of the rectangle
        """

        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2) -> "Rectangle":
        """
        Compares the area of two rectangles

        Arguments:
            rect_1: First rectangle
            rect_2: Second rectangle

        Raises:
            TypeError
                If rect_1 or rect_2 is not an instance of Rectangle

        Returns:
            The rectangle with the largest area, or rect_1 if the areas are equal
        """

        for rectangle, name in [(rect_1, "rect_1"), (rect_2, "rect_2")]:
            if not isinstance(rectangle, Rectangle):
                raise TypeError(f"{name} must be an instance of Rectangle")

        return rect_1 if (rect_1.area() >= rect_2.area()) else rect_2

    def __str__(self):
        """
        Returns the rectangle's printable representation

        Represents the rectangle with the #(pound) character
        """

        if self.__width == 0 or self.__height == 0:
            return ""

        rectangle = []
        for h in range(self.__height):
            [rectangle.append(str(self.print_symbol)) for w in range(self.__width)]
            if h != self.__height - 1:
                rectangle.append("\n")
        return "".join(rectangle)

    def __repr__(self):
        """
        Returns the rectangle's representation of a string
        """

        rectangle = "Rectangle(" + str(self.__width)
        rectangle += ", " + str(self.__height) + ")"
        return rectangle

    def __del__(self):
        """
        Prints a message for everytime we delete the rectangle
        """

        type(self).number_of_instances -= 1
        print("Bye rectangle...")
