class Siege:
    def __init__(self, max_speed: int, efficiency: int):
        self.max_speed = max_speed
        self.efficiency = efficiency

    def get_trip_cost(self, distance: int, food_price: float):
        return (distance / self.efficiency) * food_price

    def get_cargo_volume(self):
        pass


class BatteringRam(Siege):
    def __init__(self, max_speed, efficiency, load_weight, bed_area):
        self.max_speed = max_speed
        self.efficiency = efficiency
        self.load_weight = load_weight
        self.bed_area = bed_area

    def get_trip_cost(self, distance: int, food_price: float):
        return super().get_trip_cost(distance, food_price) + (self.load_weight * 0.01)

    def get_cargo_volume(self):
        return self.bed_area * 2


class Catapult(Siege):
    def __init__(self, max_speed: int, efficiency: int, cargo_volume: int):
        super().__init__(max_speed, efficiency)
        self.cargo_volume = cargo_volume

    # We ignore type here because the assignment told us not to change Siege.get_cargo_volume()
    def get_cargo_volume(self): # type: ignore
        return self.cargo_volume
