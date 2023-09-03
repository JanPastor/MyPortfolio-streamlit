class Monster():
    # Conventionally. Class attributes are created within a dunder __init__ method
    def __init__(self, health, energy):
        # print('The monster object was created')
        self.health = health
        self.energy = energy

    # More dunder methods
    def __len__(self):
        # return 5
        return self.health
    
    def __abs__(self):
        return self.energy
    
    def __call__(self): # Turns the object into a function...
        return 'The monster was called'
    
    def __add__(self, other):
        return self.health + other
    # Exercise: 7/24/23 Research the __str__ dunder method and use it
    def __str__(self): # Typically used to return a string/text. Has debugging uses.
        # print('A monster')
        return (f'A monster with health {self.health} and energy {self.energy}!')

    # methods (funtions that do stuff)
    def attack(self, amount):
        print('The monster has attacked!')
        print(f'{amount} damage was dealt')
        monster.energy -= 20
        print(self.monster.energy)
    # Exercise 7/24/23
    # Create a Move method inside of the monster that accepts
    # one argument for the speed. Inside of the Move method, create a 
    # print statement indicating the monster has moved at a certain speed
    def move(self, amount):
        print(f'The monster has a speed of {amount}')
        print(f'The monster has moved!')
        monster.energy -= 5
        print(self.monster.energy)
    

# Convert the class into an object and calls it using ()
monster = Monster(90, 40) 
# monster1 = Monster(10, 20) 
# monster2 = Monster(50, 100) 
# monster3 = Monster(300, 250) 

# Notice that variable names are in snake_case and class names are 
# in CamelCase. Subtle, but it makes a huge difference. Naming convention...
# print(monster.health) # It is important to add the .health or .energy to the monster variable
# print(monster.energy)
# print(monster1.health)
# print(monster2.health)
print(monster()) # Notice how the class-object must now be called as a Function? '()'
print(len(monster))
print(abs(monster))
# print(dir(monster))
print(monster.__dict__) # Prints all the attributes inside of a class as a dictionary.
# Recall: Dictionaries have key-value pairs.
print(monster + 10) # Calling the __add__ dunder method to change the health of the monster
print(str(monster))
print((monster))


# These attributes exist only within the local scope of the class Monster.
# It is not global unless specified.
# monster.attack(40) 
# monster.move(25)
# Whe calling any method, a reference to the actual class as the first parameter 
# is always REQUIRED. Python operates by passing a reference to the argument of 
# any method that is being called, such as the monster.attack() method
# The 'monster' variable contains the object Monster() and the .attack() method 
# inside the object is being specifically called to output something.