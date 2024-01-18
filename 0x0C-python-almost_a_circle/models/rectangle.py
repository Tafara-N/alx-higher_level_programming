#!/usr/bin/python3

"""
A rectangle class
"""

from base import Base


class Rectangle(Base):
    """
    Represent a rectangle
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize a new Rectangle.

        Args:
            width (int): The new rectangle's width
            height (int): The new rectangle's height
            x (int): The new square's x coordinate
            y (int): The new square's y coordinate
            id (int): The new square's id

        Raises:
            TypeError: If either the height or width is not an int
            ValueError: If either height or width <= 0.
            TypeError: If either x or y are not ints
            ValueError: If either x or y < 0.
        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """
        Sets width of the rectangle
        """

        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Sets height of the rectangle
        """

        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        Sets x coordinate of the rectangle
        """

        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        Sets y coordinate of the rectangle
        """

        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Returns the rectangle's area
        """

        return self.width * self.height

    def display(self):
        """
        Prints a rectangle using the `#`(pound) character.
        """

        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

    def update(self, *args, **kwargs):
        """
        Update the Rectangle.

        Args:
            *args (ints): New attribute values.
                - Arg #1 is for id attribute
                - Arg #2 is for width attribute
                - Arg #3 is for height attribute
                - Arg #4 is for x attribute
                - Arg #5 is for y attribute
            **kwargs (dict): New key:value pairs of the attributes
        """

        if args and len(args) != 0:
            b = 0
            for arg in args:
                if b == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif b == 1:
                    self.width = arg
                elif b == 2:
                    self.height = arg
                elif b == 3:
                    self.x = arg
                elif b == 4:
                    self.y = arg
                b += 1

        elif kwargs and len(kwargs) != 0:
            for i, j in kwargs.items():
                if i == "id":
                    if j is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = j
                elif i == "width":
                    self.width = j
                elif i == "height":
                    self.height = j
                elif i == "x":
                    self.x = j
                elif i == "y":
                    self.y = j

    def to_dictionary(self):
        """
        Dictionary's representation of a rectangle
        """

        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """
        print() and str() representation of the rectangle
        """

        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)
