# Constructor __init__()

class Hero: # template
   
   def __init__(self, input_nama, input_health, input_power, input_armor):
      self.name = input_nama
      self.health = input_health
      self.power = input_power
      self.armor = input_armor


hero1 = Hero("Agus", 100, 15, 20)
hero2 = Hero("Alucard", 80, 25, 10)
hero3 = Hero("Agus", 2000, 500, 100)

print(hero1.__dict__)
print(hero2.__dict__)
print(hero3.__dict__)