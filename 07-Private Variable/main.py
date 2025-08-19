# Private variable

class Hero: # template
   # class variable
   jumlah_hero = 0
   
   def __init__(self,name,health):
      self.name = name
      self.health = health
      
      # variabel instance private 
      self.__privatebos = "private Nih Bos"
      
      # variabel instance protected
      self._protected = "protected"
      

agus = Hero("Agus",100)

print(agus.__dict__)
print(agus.__dict__)
