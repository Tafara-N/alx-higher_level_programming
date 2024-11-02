#!/usr/bin/python3

"""
A class Rectangle that defines a rectangle based on 6-rectangle.py
"""


class Rectangle:
    """
    A Rectangle class
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0) -> None:
        """
        Initializing the Rectangle instance

        Arguments:
            width: The width of the rectangle
            height: The height of the rectangle

        number_of_instances:
            Incremented upon each new object creation
        """

        self.width = width
        self.height = height

        self.__class__.number_of_instances += 1

    @property
    def width(self) -> int:
        """
        Getter for the width attribute

        Returns:
            The width of the rectangle
        """

        return self.__width

    @width.setter
    def width(self, value) -> None:
        """
        Setter for the width attribute

        Arguments:
            value: The width of the rectangle

        Raises:
            TypeError
                If width is not an integer

            ValueError
                If width is less than 0
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")

        self.__width = value

    @property
    def height(self) -> int:
        """
        Getter for the height attribute

        Returns:
            The height of the rectangle
        """

        return self.__height

    @height.setter
    def height(self, value) -> None:
        """
        Setter for the height attribute

        Arguments:
            value: The height of the rectangle

        Raises:
            TypeError
                If height is not an integer

            ValueError
                If height is less than 0
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self) -> int:
        """
        Calculates the area of the rectangle

        Returns:
            The area of the rectangle
        """

        return self.__width * self.__height

    def perimeter(self) -> int:
        """
        Calculates the perimeter of the rectangle

        Returns:
            0 if the height or width is 0, else the perimeter of the rectangle
        """

        return (
            0 if self.__width == 0 or self.__height == 0
            else (self.__width * 2) + (self.__height * 2)
        )

    def __str__(self) -> str:
        """
        String representation of the rectangle

        Returns:
            An empty string if the height or width is 0, else the rectangle
               represantation using the # character
        """

        display = []

        for height in range(self.__height):
            [display.append(str(self.print_symbol)) for _ in range(self.__width)]

            # If the current height is not the last height, add a newline
            if height != self.__height - 1:
                display.append("\n")

        return (
            "" if self.__height == 0 or self.__width == 0
            else "".join(display)
        )

    def __repr__(self) -> str:
        """
        String representation of the rectangle that can be used by eval

        Returns:
            A string representation of the rectangle that can be used by eval
        """

        return f"{self.__class__.__qualname__}({self.__width}, {self.__height})"

    def __del__(self) -> None:
        """
        Print a message when an instance of Rectangle is deleted

        number_of_instances:
            Decremented upon each object deletion
        """

        self.__class__.number_of_instances -= 1

        print("Bye rectangle...")
