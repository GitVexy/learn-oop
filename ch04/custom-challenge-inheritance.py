class Weapon:
    
    def __init__(self, damage=0):
        self.__damage = damage
        
    def get_damage(self):
        return self.__damage
    
class SiegeWeapon(Weapon):
    
    def __init__(self, damage, crew_size):
        super().__init__(damage)
        self.__crew_size = crew_size
        
    def fire(self):
        print(f"Firing with {self.get_damage()} damage")
    
    def crew_report(self):
        print(f"Crew size: {self.__crew_size}")
        return self.__crew_size
    
class FlamingSiegeWeapon(SiegeWeapon):
    
    def __init__(self, damage, crew_size):
        super().__init__(damage, crew_size)
    
    def fire(self):
        print(f"Firing with {self.get_damage()} damage and flaming munitions")

print("\n")
flamer = FlamingSiegeWeapon(damage=200, crew_size=5)
print("Made a flaming siege weapon:")
flamer.fire()
#SiegeWeapon.fire(flamer) # Inherited function applied. Don't do this tho
flamer.crew_report()
print("\n")
siege = SiegeWeapon(damage=150, crew_size=4)
print("Made a siege weapon:")
siege.fire()
siege.crew_report()