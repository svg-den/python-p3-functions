#!/usr/bin/env python3

def greet_programmer():

    print("Hello, programmer!")
    pass

def greet(name): 
    print("Hello, {}!".format(name))
    pass
greet("Guido")

def greet_with_default(name="programmer"):
   print("Hello, {}!".format(name))
   pass


def add(num1, num2):
  return num1 + num2

add_result = add(45, 55)
print(add_result)
pass

def halve(number):
    if not isinstance(number, (int, float)):
        return None
    
    return number / 2

print(halve(100))
print(halve(99.0))
pass
