class Monster:
    # health = 50
    # energy = 100
    def __init__(self, health, energy, **kwargs):
        # **kwargs stores extra arguments that the Monster Class does not need
        self.health = health
        self.energy = energy
        # By MRO, we define the next inheritance with another super dunder init method
        # However, it is defined within the 1st parent class
        # Extra arguments are passed to the next Parent Class that the 
        # original object needs to inherit from
        # In this case, Shark Child Class wants to inherit speed and has_scales from Fish Class
        # Therefore, unpacking **kwargs dictionary and passing it to Parent Class 2: Fish Class 
        # via super dunder init (**kwargs) below
        super().__init__(**kwargs)

    # Methods
    def attack(self, amount):
        print('The monster has attacked!')
        print(f'{amount} damage was dealt')
        self.energy -= 20

    def move(self, speed):
        print('The monster has moved')
        print(f'It has a speed of {speed}')

class Fish:
    # Adding **kwards again in case there exists an additional parent class to inhert from
    def __init__(self, speed, has_scales, **kwargs):
        # Fish class specific attributes
        self.speed = speed
        self.has_scales = has_scales
        # If there is a third class object to inherit, then the process repeats again, but 
        # inside Parent class 2...etc.
        super().__init__(**kwargs) 

    def swim(self):
        print(f'The fish is swimming at a speed of {self.speed}')

class Shark(Monster, Fish): # Inheriting from two parents
    def __init__(self, bite_strength, health, energy, speed, has_scales):
        self.bite_strength = bite_strength
         # Because we are using **kwargs, we must use keyword arguments when parsing these arguments 
        #  for inheritance purposes
        super().__init__(health = health, 
                         energy = energy, 
                         speed = speed, 
                         has_scales = has_scales)

# MRO (Method Resolution Order)
# print(Shark.mro())

shark = Shark(bite_strength= 10, 
              health= 200, 
              energy= 100,
              speed = 120,
              has_scales = False)
print(shark.speed)
print(shark.has_scales)