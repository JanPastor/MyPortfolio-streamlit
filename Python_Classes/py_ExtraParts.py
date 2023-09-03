class Monster:
    # Create doc_string
    '''A monster that has some attributes, attack and move methods'''
    def __init__(self, health, energy):
        self.health = health
        self.energy = energy
        # Private attributes
        self._id = 5
    # Methods
    def attack(self, amount):
        print('The monster has attacked!')
        print(f'{amount} damage was dealt')
        self.energy -= 20

    def move(self, speed):
        print('The monster has moved')
        print(f'It has a speed of {speed}')

monster = Monster(health= 20, energy= 10)

# Private attributes
# These are special attributes that are inside of a class and cannot be 
# influenced externally
print(monster._id)
# hasattr and setattr (Check and set attributes)
print(hasattr(monster, 'health')) # Returns boolean value
if hasattr(monster, 'health'):
    print(f'The monster has {monster.health} health')
# hasattr is useful for debugging

# setattr provides an efficient way of adding new attributes to an existing class
setattr(monster, 'weapon', 'Sword')
print(monster.weapon)
# Typically when creataing a class, we define the attributes that we want from the beginning 
# inside of the class instead of setting new attributes. 
new_attributes = (['weapon', 'Axe'], ['armor', 'Shield'], ['potion','mana'])
for attr, value in new_attributes:
    setattr(monster, attr, value)
print(vars(monster))

# doc string for classes
# The doc string is used for explaining code blocks and classes
print(monster.__doc__)