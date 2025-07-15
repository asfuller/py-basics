### Functions ###
#def functionname(): how you write a function
#def function(paramenter)

#def greet():
#    print("Hello, world!")
#    print("Welcome aboard")

#greet()  #calls the function

#Example 1
print("Example 1: \n")
def greet(first_name, last_name):
    print(f"Hello {first_name} {last_name}")
    print("Welcome aboard")


greet("Alex", "Fuller")
greet("John", "Smith")

## Types of Functions ##
# 1- Perform a Task (Printing to terminal)
# 2 - Return a Value (Calculate)

#Example 2
print("Example 2: \n")

def greet(name):
    print(f"Hello {name}")

def get_greeting(name):
    return f"Hi {name}"

message = get_greeting("Alex")  #we can do whatever we want with this
#with this, we can either print or use opem files

## Keyword Arguments ##
# Example 3
# we want to increment a number by a certain value
print("Example 3: \n")
def increment(number, by):
    return number + by
result = increment(2, 1)
print(result)

#To simplify this code
def increment(number, by):
    return number + by
print(increment(2, 1))

# To make it more readable
def increment(number, by):
    return number + by
print(increment(2, by=1))  # by=1 is a keyword argument
# keyword argument makes code more readable

## Default Arguments ##
# want to make by parameter optional
def increment(number, by=1):
    return number + by
print(increment(2, 5))

# optional parameters come after required parameters

## *args ##
# want to create a function that takes a variable number of arguments
#Example 4
print("Example 4: \n")
def multiply(*numbers):  #*numbers represents a collection of args
    total = 1
    for number in numbers:
        total *= number
    return total
    #return x * y
print(multiply(2, 3, 4, 5))