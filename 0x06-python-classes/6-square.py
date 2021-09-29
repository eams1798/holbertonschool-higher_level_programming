def evaluate_size(value):
    if not(type(value) is int):
        raise TypeError("size must be an integer")
    elif value < 0:
        raise ValueError("size must be >= 0")
    else:
        return value
def evaluate_position(value):
    if type(value) is tuple and len(value) == 2:
        return value
    else:
        raise TypeError("position must be a tuple of 2 positive integers")

class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.__size = evaluate_size(size)
        self.__position = evaluate_position(position)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = evaluate_size(value)

    @property
    def position(self):
        return self.__position

    @size.setter
    def position(self, value):
        self.__position = evaluate_position(value)

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for a in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for b in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print()
