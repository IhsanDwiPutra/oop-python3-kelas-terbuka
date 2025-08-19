class Hero: # template
   pass

hero1 = Hero() # object / instance (instansiate) 
hero2 = Hero()
hero3 = Hero()

hero1.name = "tigreal"
hero1.health = 200

hero2.name = "haya"
hero2.health = 150

hero3.name = "lance"
hero3.helath = 180

print(hero1.__dict__)
print(hero1)
print(hero1.name)