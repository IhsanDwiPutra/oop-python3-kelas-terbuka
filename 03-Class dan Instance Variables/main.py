# Class dan Instance Variables

class Hero: # template
   # Class variabel
   jumlah = 0
   list_anggota = []
   
   def __init__(self, input_name, input_health, input_power, input_armor):
      # Instance variabel
      self.name = input_name
      self.health = input_health
      self.power = input_power
      self.armor = input_armor
      Hero.jumlah += 1
      Hero.list_anggota.append(input_name)
      print("Membuat Hero dengan nama " + input_name)
      

hero1 = Hero("Agus", 1000, 500, 300)
hero2 = Hero("Haya", 100, 20, 40)
hero3 = Hero("Alucard", 200, 20, 40)

print("Jumlah Hero = " + str(Hero.jumlah))
print("Anggota Hero = " + str(Hero.list_anggota))