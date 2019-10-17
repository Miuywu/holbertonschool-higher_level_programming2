#!/usr/bin/python3
class BaseGeometry:
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value"""

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value  <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """Rectangle inherited from BaseGeometry"""

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """area"""
           return self.__width * self.__height

    def __str__(self):
        """[Rectangle] h/w"""
        return "[Rectangle] " + "{}/{}".format(self.__width, self.__height)

class Square(Rectangle):
    """Square inherits Rectangle"""
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """area of square"""
        return self.__size * self.__size

    def __str__(self):
        """[square] s/s"""
        return "[Rectangle] " + "{}/{}".format(self.__size, self.__size)
