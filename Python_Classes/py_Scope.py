# # Scope problem
def update_health(amount):
    monster.health += amount

# health = 10
# print(health)
# update_health(20)
# print(health)

# Solution to Scope problem
class Monster:
    def __init__(self, health, energy):
        self.health = health
        self.energy = energy

    def update_energy(self, amount):
        self.energy += amount

    #2.
    def get_damage(self, amount):
        self.health -= amount

# Exercise 7/25/23
    # 1. Create a hero class with 2 parameters: damage, monster
    # 2. The monster class should have a method that lowers the health --> get_damage(amount)
    # 3. The hero class hould have an attack method that calls the get_damage method from the monster
    # The amount of damage is hero.damage
    

monster = Monster(health = 100, energy = 50)
# monster.health += 20
# print(monster.health)
# update_health(20)
# print(monster.health)
# monster.update_energy(20)
# print(monster.energy)
# print(monster.energy)

# 1. 
class Hero():
    def __init__(self, damage, monster):
        self.damage = damage
        self.monster = monster

    def attack(self):
        # This attack method from inside the Hero class calls the get_damage method from
        # inside the Monster class. The damage value passed into Hero class gets passed into this
        # attack method. Consequently, this attack method triggers the get_damage method from the 
        # Monster class. Then the monster object recieves damage to its health via a subtraction of a set amt.
        self.monster.get_damage(self.damage)

hero = Hero(damage= 15, monster = monster)
print(monster.health) # 100
hero.attack()
print(monster.health) # should print 85