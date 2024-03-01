# This is a long comment in Python. It is intended to test how comments are displayed and if they wrap or overflow.
# Let's also test the syntax highlighting of various elements in Python.

import math
import sys

def calculate_area(radius):
    """Function to calculate the area of a circle."""
    return math.pi * radius ** 2

def greet(name):
    """Function to greet someone."""
    print(f"Hello, {name}! The area of a circle with radius 5 is {calculate_area(5):.2f}.")

class MyClass:
    def __init__(self, name):
        self.name = name

    def display_name(self):
        print(f"Name: {self.name}")

if __name__ == "__main__":
    greet("Alice")
    my_object = MyClass("Test Object")
    my_object.display_name()
    try:
        file = open("testfile.txt", "r")
        content = file.read()
        print(content)
    except FileNotFoundError:
        print("The file was not found.", file=sys.stderr)
    finally:
        file.close()
