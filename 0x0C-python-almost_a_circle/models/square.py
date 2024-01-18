#!/usr/bin/python3

"""
A square class
"""

from rectangle import Rectangle


class Square(Rectangle):
    """
    A square.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializing a new square

        Args:
            size (int): The new square' size
            x (int): The new square's x coordinate
            y (int): The new square's y coordinate
            id (int): The new square's id
        """

        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Sets the square's size
        """

        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Updating the square

        Args:
            *args (ints): New attribute values
                - Arg #1 is for id attribute
                - Arg #2 is for size attribute
                - Arg #3 is for x attribute
                - Arg #4 is for y attribute
            **kwargs (dict): New key:value pairs of attributes
        """

        if args and len(args) != 0:
            b = 0
            for arg in args:
                if b == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif b == 1:
                    self.size = arg
                elif b == 2:
                    self.x = arg
                elif b == 3:
                    self.y = arg
                b += 1

        elif kwargs and len(kwargs) != 0:
            for i, j in kwargs.items():
                if i == "id":
                    if j is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = j
                elif i == "size":
                    self.size = j
                elif i == "x":
                    self.x = j
                elif i == "y":
                    self.y = j

    def to_dictionary(self):
        """
        Dictionary's representation of the square
        """

        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """
        print() and str() representation of a square
        """

        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
