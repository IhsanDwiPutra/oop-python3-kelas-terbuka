# Getter dan Setter

class Hero:
   
   def __init__(self,name,health,armor):
      self.name = name
      self.__health = health
      self.__armor = armor
      # self.__info = "name\t: {}\nhealth\t: {}".format(self.name,self.__health)
   
   @property
   def info(self):
      return "name\t: {}\nhealth\t: {}".format(self.name,self.__health)
   
   @property
   def armor(self):
      pass
   
   @armor.getter 
   def armor(self):
      return self.__armor
   
   @armor.setter
   def armor(self, inputArmor):
      self.__armor = inputArmor
   
   @armor.deleter
   def armor(self):
      print("armor di delete bang")
      self.__armor = None

agus = Hero("agus",100, 20)
print(agus.info)
print(agus.__dict__)
agus.name = "bagas"
print(agus.info)

print("\ngetter dan setter untuk __armor")
print("hasil getter: {}".format(agus.armor))
agus.armor = 50
print(f"hasil setter armor: {agus.armor}")
print(agus.__dict__)

print("\ndelete armor")
del agus.armor 
print(agus.__dict__)
