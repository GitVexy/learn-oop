class Rectangle:
    def overlaps(self, rect):
        
        return(                                                             ###################
            self.get_left_x   ()   <= rect.get_right_x  () and #AL <= BR    # AL    AT     AR #
            self.get_right_x  ()   >= rect.get_left_x   () and #AR >= BL    #          ##############
            self.get_top_y    ()   >= rect.get_bottom_y () and #AT >= BB    #          # BL  BT  BR #
            self.get_bottom_y ()   <= rect.get_top_y    ()     #AB <= BT    # AL    AB #   AR #     #
        )                                                                   ###################     #
#                                                                                      # BL  BB  BR #
# don't touch below this line                                                          ##############

    def __init__(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

    def get_left_x(self):
        if self.__x1 < self.__x2:
            return self.__x1
        return self.__x2

    def get_right_x(self):
        if self.__x1 > self.__x2:
            return self.__x1
        return self.__x2

    def get_top_y(self):
        if self.__y1 > self.__y2:
            return self.__y1
        return self.__y2

    def get_bottom_y(self):
        if self.__y1 < self.__y2:
            return self.__y1
        return self.__y2

    def __repr__(self):
        return f"Rectangle({self.__x1}, {self.__y1}, {self.__x2}, {self.__y2})"
