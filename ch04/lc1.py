class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    def get_area(self) -> int:
        return self.length * self.width

    def get_perimeter(self) -> int:
        return (self.length * 2) + self.width * 2


class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)
