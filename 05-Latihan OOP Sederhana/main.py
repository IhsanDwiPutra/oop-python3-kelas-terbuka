"""
# Latihan OOP Sederhana
- Method:
   menyerang
   diserang/bertahan
   
"""
class Hero: # template
   # class variabel
   
   def __init__(self, name_input, health_input, power_input, armor_input):
      self.name = name_input
      self.health = health_input
      self.power = power_input
      self.armor = armor_input
   
   def serang(self, enemy):
      print(f"{self.name} menyerang {enemy.name}")
      enemy.diserang(self, self.power)
   
   def diserang(self, enemy, attack_power):
      print(f"{self.name} diserang {enemy.name}")
      attack_diterima = attack_power / self.armor
      print(f"Serangan terasa: {attack_diterima}")
      self.health -= attack_diterima
      print(f"darah {self.name} tersisa {self.health}\n")
   
   def display(self):
      print(f"\nName\t: {self.name}\nHealth\t: {self.health}\nPower\t: {self.power}\nArmor\t: {self.armor}")

haya = Hero("Haya", 100, 10, 20)
lance = Hero("Lance", 100, 30, 10)

haya.serang(lance)
lance.serang(haya)