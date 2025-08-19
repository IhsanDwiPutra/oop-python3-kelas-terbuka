# Latihan Encapsulasi

class Hero:
   # private class variabel
   __jumlah = 0
   
   def __init__(self,name,health,power,armor):
      self.__name = name
      self.__healthStandar = health
      self.__powerStandar = power
      self.__armorStandar = armor
      self.__level = 1
      self.__exp = 0
      
      self.__healthMax = self.__healthStandar * self.__level
      self.__power = self.__powerStandar * self.__level
      self.__armor = self.__armorStandar * self.__level
      
      self.__health = self.__healthMax
      
      Hero.__jumlah += 1
   
   @property
   def info(self):
      return "{} :\n\tHealth = {}/{}\n\tPower = {}\n\tArmor = {}\n\tLevel = {}".format(self.__name, self.__health, self.__healthMax, self.__power,
      self.__armor, self.__level)
   
   @property
   def gainExp(self):
      pass
   
   @gainExp.getter
   def gainExp(self,addExp):
      self.__exp = addExp
      if (self.__exp >= 100):
         print(self.__name, "level up")
         self.__level += 1 
         self.__exp -= 100
         
         
   

agus = Hero("Agus", 100, 5, 10)
print(agus.info)
