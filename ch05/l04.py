class Unit:
    def __init__(self, name, pos_x, pos_y):
        self.name = name
        self.pos_x = pos_x
        self.pos_y = pos_y

    def in_area(self, x1, y1, x2, y2) -> bool: # type: ignore
        pass


class Dragon(Unit):
    def __init__(self, name, pos_x, pos_y, height, width, fire_range):
        super().__init__(name, pos_x, pos_y)
        self.fire_range = fire_range
        self.height = height
        self.width = width
        self.__hit_box = Rectangle(
            self.pos_x - (width / 2),
            self.pos_y + (height / 2),
            self.pos_x + (width / 2),
            self.pos_y - (height / 2)
        )

    def in_area(self, x1, y1, x2, y2) -> bool:
        area = Rectangle(x1, y1, x2, y2)
        return area.overlaps(self.__hit_box)


# Don't touch below this line


class Rectangle:
    def overlaps(self, rect) -> bool:
        return (
            self.get_left_x() <= rect.get_right_x()
            and self.get_right_x() >= rect.get_left_x()
            and self.get_top_y() >= rect.get_bottom_y()
            and self.get_bottom_y() <= rect.get_top_y()
        )

    def __init__(self, x1: int, y1: int, x2: int, y2: int):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

    def get_left_x(self) -> int:
        if self.__x1 < self.__x2:
            return self.__x1
        return self.__x2

    def get_right_x(self) -> int:
        if self.__x1 > self.__x2:
            return self.__x1
        return self.__x2

    def get_top_y(self) -> int:
        if self.__y1 > self.__y2:
            return self.__y1
        return self.__y2

    def get_bottom_y(self) -> int:
        if self.__y1 < self.__y2:
            return self.__y1
        return self.__y2
