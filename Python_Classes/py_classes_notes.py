# What is an object?
# An object in programming is a container for variables and functions.
# i.e. An npc object might contain the following variables and functions
# Variables: Health, energy, stamina, damage..
# Functions: Attack, movement, animations...

# Terminology
# Variables inside of an object are called "attributes"
# Functions inside of an object are called "methods"
# Classes are blueprints for the Objects
# Classes can also inherit from another class. 
# Resulting objects will have attributes
# and methods from both classes

# Pros:
# Organize complex code and created code can be reusable. Ubiqituous.
# Some modules in Python require the use of classes 
# Scope is easier to manage with classes
# It is still possible to write code without classes, but only for simpler applications.
# Classes are needed when the complexity of code increases.

# Use snake_case and CamelCase when working with classes

# What are dunder methods?
# A Dunder method is a method that is not called by the user
# It is called by Python when an event occurs
#  __init__ (a type of dunder method) is called when an object is created
#  __len__ is called when the obect is passed into a len() function
# _-abs__ is called when the object is passed into the abs() function

# Shocking: Everything in Python is an object! 
# This includes inbuilt strings, integers, etc...

# Difference between a method and a function?
# A method belongs to an object, i.e. 'test.upper()'
# A function, i.e. len('test') can accept multiple data types
# while a method can only accept a specific type of data type

# Classes and Scope
# Every method has a reference to the class. So, it is simple to get and change
# class attributes
# Because of that, methods rely much less on parameters, global, and return
# You may still use them!
# Objects can be influenced/altered from the outside and from the a local scope of
# a function! Woah! 

# Inheritance
# Inheritcane: A class recieves class attribures and methods from another class or 
# group of classes

# One class can inherit from multiple parent classes
# One class can transfer multiple attributes and methods to numerous classes
# i.e. One parent class in which multiple subsequent child-classes inherit from the one paraent class

# Complex inheritance:
# Scenario: There are two parent classes, Parent Class 1 and Parent Class 2.
# There exists one child class, Child Class 1. How does Child Class 1 inherit from 
# the two Parent classes?

# Extra Parts