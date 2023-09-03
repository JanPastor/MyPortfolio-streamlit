class Monster:
    # health = 50
    # energy = 100
    def __init__(self, health, energy):
        self.health = health
        self.energy = energy
    # Methods
    def attack(self, amount):
        print('The monster has attacked!')
        print(f'{amount} damage was dealt')
        self.energy -= 20

    def move(self, speed):
        print('The monster has moved')
        print(f'It has a speed of {speed}')

 # We add brackets to enable inheritance and pass the specific class name
 # that we want this class to inherit from
class Shark(Monster):
    def __init__(self, speed, health, energy):
        # defining the specific parent with dunder init method to inherit its 
        # specific class attributes and methods below
        # Monster.__init__(self, health, energy) # This is the older method of inheritance

        # New way to inherit from specific parent classes
        # Use of the super() dunder init method
        # Shark class now inherits health and energy attributes from Monster class
        super().__init__(health, energy) # Useful for complex inheritance networks
        # It is the most commonly used inheritance method

        # Shark class specific attributes
        self.speed = speed
    
    def bite(self):
        print('The shark uses bite!')
    # Creating the exact same namespace method called 'move' 
    # overrides the move method from the inherited class
    def move(self):
        print('The shark has moved')
        print(f'The sharks speed is {self.speed}')

# Exercise 7/26/23 (Done)
# Create a scorpion class that inherits from the Monster class
# Health and energy from the parent
# Addd new poison_damage attribute
# Overwrite the damage method to show the poison damage

class Scorpion(Monster):
    def __init__(self, poison, health, energy):
        # Inheriting health and energy from Monster parent class
        super().__init__(health, energy)
        # Class specific attributes
        self.poison = poison
    
    # Poison_damage method
    def attack(self):
        print('Scorpion uses Poison!')
        # Make use of the self.poison attribute (think of it as a variable)
        print(f'Poison damage is {self.poison}!')

# Creating shark object and calling the methods
#--------
# This is the shark object, give it values for its arguments
# shark = Shark(speed = 120, health = 50, energy = 100) 
# print(shark.speed)
# print(shark.health)
# print(shark.energy)

#---------
# Creating the Scorpion object and calling the methods
scorpion = Scorpion(poison= 15, health= 25, energy= 50)
print(scorpion.poison)
print(scorpion.health)
print(scorpion.energy)
scorpion.attack()
scorpion.move(10)