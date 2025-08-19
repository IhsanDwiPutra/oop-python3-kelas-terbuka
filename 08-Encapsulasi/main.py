"""
+ Encapsulasi
   Buat semua variabel private
   - Getter = mengambil variable
   - Setter = menseting variabel
"""

class Hero:
   
   def __init__(self,name,health,power):
      self.__name = name
      self.__health = health
      self.__power = power
   
   # getter 
   def getName(self):
      return self.__name
   
   def getHealth(self):
      return self.__health
   
   # setter
   def diserang(self, power):
      self.__health -= power
   
   def setPower(self, power_baru):
      self.__power = power_baru

# awal dari game
bambang = Hero("Bambang", 75, 10)
print(bambang.__dict__)

# game berjalan
print(bambang.getName())
print(bambang.__dict__)

bambang.diserang(20)
print(bambang.getHealth())
