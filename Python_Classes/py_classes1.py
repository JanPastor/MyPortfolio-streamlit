class Monster():
    # attributes
    health = 90
    energy = 40 

    # methods (funtions that do stuff)
    def attack(self, amount):
        print('The monster has attacked!')
        print(f'{amount} damage was dealt')
        # monster.energy -= 20
        # print(monster.energy)
    # Exercise 7/24/23
    # Create a Move method inside of the monster that accepts
    # one argument for the speed. Inside of the Move method, create a 
    # print statement indicating the monster has moved at a certain speed
    def move(self, amount):
        print(f'The monster has a speed of {amount}')
        print(f'The monster has moved!')
        monster.energy -= 5
        print(monster.energy)
    

# Convert the class into an object and calls it using ()
monster = Monster() 
monster1 = Monster() 
monster2 = Monster() 
monster3 = Monster() 

# Notice that variable names are in snake_case and class names are 
# in CamelCase. Subtle, but it makes a huge difference. Naming convention...
print(monster.health) # It is important to add the .health or .energy to the monster variable
print(monster.energy)
# These attributes exist only within the local scope of the class Monster.
# It is not global unless specified.
monster.attack(40) 
monster.move(25)
# Whe calling any method, a reference to the actual class as the first parameter 
# is always REQUIRED. Python operates by passing a reference to the argument of 
# any method that is being called, such as the monster.attack() method
# The 'monster' variable contains the object Monster() and the .attack() method 
# inside the object is being specifically called to output something.