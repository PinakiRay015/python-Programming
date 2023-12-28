# normal function with no parameters
def greet1():
    print("Good morning")


# functions with parameters (parameterized functions)
def greet2(name, department):
    print("welcome " + name)
    print("You are a part of " + department)


def areaOfRectangle(length, breadth):
    return str(length * breadth)


greet1()
greet2("Rohan", "CSE")
print("The area of rectangle is " + areaOfRectangle(10, 5))
