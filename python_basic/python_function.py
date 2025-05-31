#Fuction in python 
#A function is a block of reusable code which only runs when it is called. You can pass data, which calles parameters, into a function. Function can return data as an output.


def hello():
    print(f"Hello, world!")

hello()


#parameters 
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
greet("Bob")


#Returning a Value
def add(a, b):
    return a + b

result = add(3, 5)
print(result)


#Default Parameters
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet("Alice") 
greet()         


#Variable Number of Arguments
#Sometimes, you might not know how many arguments will be passed to a function. You can use *args and **kwargs for this.
def print_numbers(*args):
    for number in args:
        print(number)

print_numbers(1, 2, 3, 4)

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=30, city="New York")



#Recursion
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5)) 



#Lambda Functions 
multiply = lambda x, y: x * y
print(multiply(3, 4))
