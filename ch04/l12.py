class Unit:
    def __init__(self, name: str, pos_x: int, pos_y: int):
        
        self.name = name
        self.pos_x = pos_x
        self.pos_y = pos_y

    def in_area(self, x_1: int, y_1: int, x_2: int, y_2: int) -> bool:
        
        if (self.pos_x in range(x_1, x_2) and
            self.pos_y in range(y_1, y_2)
            ): return True
        return False


class Dragon(Unit):
    def __init__(self, name: str, pos_x: int, pos_y: int, fire_range: int):
        
        super().__init__(name, pos_x, pos_y)
        self.__fire_range = fire_range

    def breathe_fire(self, x: int, y: int, units: list) -> list:
        fire_area = [ # x_2, y_2 incremented by 1 to be inclusive in range
            x - self.__fire_range,      # [0] x_1
            y - self.__fire_range,      # [1] y_1
            x + self.__fire_range + 1,  # [2] x_2
            y + self.__fire_range + 1   # [3] y_2
        ]
        units_hit = []
        for unit in units:
            
            if unit.in_area(
                fire_area[0],
                fire_area[1],
                fire_area[2],
                fire_area[3]
            ): units_hit.append(unit)
            
        return units_hit

run_cases = [
    (
        [Unit("Cian", 3, 3), Unit("Andrew", -1, 4), Unit("Baran", -6, 5)],
        Dragon("Draco", 2, 2, 3),
        2,
        3,
        ["Cian", "Andrew"],
    ),
]

""" TEST CASES
submit_cases = run_cases + [
    (
        [
            Unit("Carbry", 2, 1),
            Unit("Yvor", 1, 0),
            Unit("Eoin", 2, 0),
            Unit("Edwin", 10, 10),
        ],
        Dragon("Fafnir", 1, 1, 1),
        1,
        1,
        ["Carbry", "Yvor", "Eoin"],
    ),
    (
        [Unit("Nicholas", 0, 1), Unit("Andrew", -1, 4), Unit("Baran", -6, 5)],
        Dragon("Hydra", 0, 0, 2),
        0,
        1,
        ["Nicholas"],
    ),
    (
        [
            Unit("Yvor", 1, 0),
            Unit("Nicholas", 0, 1),
            Unit("Eoin", 2, 0),
            Unit("Cian", 3, 3),
            Unit("Andrew", -1, 4),
            Unit("Baran", -6, 5),
            Unit("Carbry", 2, 1),
        ],
        Dragon("Smaug", 6, 6, 2),
        1,
        1,
        ["Yvor", "Nicholas", "Eoin", "Cian", "Carbry"],
    ),
]


def test(units, dragon, x_target, y_target, expected_hit_units):
    print("---------------------------------")
    print(f"Testing Dragon {dragon.name} at ({dragon.pos_x}, {dragon.pos_y})")
    for unit in units:
        print(f"Unit {unit.name} at ({unit.pos_x}, {unit.pos_y})")
    print(f"Breathing fire at ({x_target}, {y_target})")
    print(f"Expecting hit units: {expected_hit_units}")
    hit_units = dragon.breathe_fire(x_target, y_target, units)
    hit_unit_names = [unit.name for unit in hit_units]
    print(f"Actual hit units: {hit_unit_names}")
    if set(hit_unit_names) == set(expected_hit_units):
        print("Pass")
        return True
    else:
        print("Fail")
        return False


def main():
    passed = 0
    failed = 0
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main() """