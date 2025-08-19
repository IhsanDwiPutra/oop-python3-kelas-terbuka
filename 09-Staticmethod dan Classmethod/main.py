# Staticmethod dan classmethod (decorator)

class Hero:
   # private class variabel
   __jumlah = 0
   
   def __init__(self,name):
      self__name = name 
      Hero.__jumlah += 1

   # method ini hanya berlaku untuk objek
   def getJumlah1(self):
      return Hero.__jumlah
   
   # method ini tidak berlaku untuk objek tapi berlaku untuk class
   def getJumlah2():
      return Hero.__jumlah
   
   # method static (decorator)
   @staticmethod
   def getJumlah3():
      return Hero.__jumlah
   
   #
   @classmethod
   def getJumlah4(cls):
      return cls.__jumlah

bagas = Hero("bagas")
print(bagas.getJumlah1())
agus = Hero("agus")
print(Hero.getJumlah2())
ando = Hero("andi")
print(bagas.getJumlah3())
print(Hero.getJumlah3())
print(f"Menggunakan class method dengan Hero: {Hero.getJumlah4()}")
print(f"Menggunakan class method dengan Objek: {bagas.getJumlah4()}")

