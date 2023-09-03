# def add(a, b): # Creating an object that is just a function
#     return a + b

# # a = test # storing the function in a variable
# # a.another_attribute = 10 # Adds an attribute to the 'test' function
# class Test:
#     def __init__ (self, add_function):
#         # The class then saves the passed function object as an attribute
#         self.add_function = add_function

# # Creating a variable that passes a function object as an argument for a class
# test = Test(add_function= add) 
# print(test.add_function(1,2))

# Exercise 7/25/23
# Create a Monster class with a parameter called func, store this func as a parameter
# Create another class, called Attacks, that has 4 methods:
# Bite, Strike, Slash, Kick (each method just prints a statement of the attack)
# Create a monster object and give it one of the attack methods from the attack class

class Monster:
    def __init__(self, func):
        self.func = func

class Attacks:

    def Bite(self):
        print('The monster uses Bite!')
    def Strike(self):
        print('The monster uses Strike!')
    def Slash(self):
        print('The monster uses Slash!')
    def Kick(self):
        print('The monster uses Kick!')


# monster = Monster(func = Attacks().Bite)
# monster.func()

# or
# Define another variable that stores the attacks object class and then call the variable
attacks = Attacks()
monster = Monster(func = attacks.Bite)
monster.func()
# Summary: The Monster class is created with a paramater that accepts a fucntion.
# Then another class/object called Attacks contains several methods that describe the 
# particular attack moves of the monster object. These methods are then passed into the 
# Monster class (essentially allowing the Monster class to inherit and use aspects of the Attack class)
# Two variables are defined. An attack variable that stores the Attack class to be used later
# The monster variable is then created which stores the Monster Class while at the same time
# retrieving a specific method from the Attack Class.
# When the monster.func() is called, then the specific method is executed.