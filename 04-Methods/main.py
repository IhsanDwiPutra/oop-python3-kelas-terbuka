# Methods

class Hero:
   # Class variabel
   jumlah_hero = 0
   list_anggota = []
   
   def __init__(self, input_name, input_health, input_power, input_armor):
      # Instance variable
      self.name = input_name
      self.health = input_health
      self.power = input_power
      self.armor = input_armor
      Hero.jumlah_hero += 1
      Hero.list_anggota.append(input_name)
      print("Membuat Hero dengan nama " + input_name)\
   
   # void function, method tanpa return, tanpa argumen
   def display(self):
      print(f"\nName\t: {self.name}\nHealth\t: {self.health}\nPower\t: {self.power}\nArmor\t: {self.armor}")
   
   # method dengan argumen, tanpa return
   def tambah_darah(self, up):
      self.health += up
      print(f"{self.name} ngeheal {up} HP")
   
   def menyerang(self, enemy):
      print(f"{self.name} menyerang {enemy.name}")
      enemy.health = enemy.health - self.power
      if enemy.health <= 0:
         enemy.health = 0
      enemy.display()
   
   # method dengan return
   def get_health(self):
      return self.health

hero1 = Hero("Agus", 1000, 500, 200)
hero2 = Hero("Haya", 200, 300, 100)

hero1.display()
hero2.display()

hero1.menyerang(hero2)
hero2.tambah_darah(250)
hero2.display()

print(hero2.get_health())