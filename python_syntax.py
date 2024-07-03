# Python syntax
"""some comment here"""

name = "John"
age = 25
is_student = True
salary = 10000.12
team = None

print(name)
print(age)
print(is_student)
print(team)

print(type(name))
print(type(age))
print(type(salary))
print(int(salary))

print(len(name))
print(name.upper())
print(name[0:2])
print(name[::-1])

my_list = list()
my_list.append(1)
my_list.append(2)
print(my_list)
print(len(my_list))
print(max(my_list))
print(sum(my_list))

my_dict = {"key1": 1, "key2": 2}
print(my_dict["key1"])
print(my_dict.get("key1"))
my_dict["key3"] = 3
print(my_dict.keys())
my_dict = dict(a=1, b=2, c=3)
print(my_dict)

my_set = set()
my_set.add(1)
print(my_set)
print(len(my_set))
print(list(my_set))

number = 10
if number > 0:
  print("positive")
elif number < 0:
  print("negative")
else:
  print("zero")

for i in range(3):
  print(i)

def greet(name, age):
  print(f"Hello {name}, you are {age} years old")

greet("John", 25)
greet(name="Mike", age=20)

numbers = [1, 2, 3]
squared_numbers = list(map(lambda number: number ** 2, numbers))
print(squared_numbers)

import math

class Circle:
  pi = math.pi
  def __init__(self, radius):
    self.radius = radius

  @classmethod
  def create_circle(cls, radius):
    return Circle(radius)
  
  def get_area(self):
    return Circle.pi * self.radius ** 2

  def get_circumference(self):
    return 2 * Circle.pi * self.radius

circle1 = Circle(5)
circle2 = Circle.create_circle(10)
print(circle1.get_circumference())
print(circle2.get_area())
