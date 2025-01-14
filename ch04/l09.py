# Comment to test how they look

class Hero:
    def __init__(self, name: str, health: int):
        self.__name = name
        self.__health = health

    def get_name(self) -> str:
        return self.__name

    def get_health(self) -> int:
        return self.__health

    def take_damage(self, damage: int):
        self.__health -= damage


class Archer(Hero):
    def __init__(self, name: str, health: int, num_arrows: int):
        super().__init__(name, health)
        self.__num_arrows = num_arrows

    def shoot(self, target: Hero):
        if self.__num_arrows <= 0:
            raise Exception("not enough arrows")
        self.__num_arrows -= 1
        target.take_damage(10)


class Wizard(Hero):
    def __init__(self, name: str, health: int, mana: int):
        super().__init__(name, health)
        self.__mana = mana
        
    def cast(self, target: Hero):
        if self.__mana < 25:
            raise Exception("not enough mana")
        self.__mana -= 25
        target.take_damage(25)
