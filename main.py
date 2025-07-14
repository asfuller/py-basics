import math  # imports the math module to unlock more math functions

#if __name__ == '__types__':
# Printing/Displaying
print("Pycharm is awesome!")
    # print("*" * 10)

## Variables ##
# stores data in the computer's memory
students_count = 1000 #this is an integer
print(students_count)

# Primitive types - can numbers, strings, and booleans
rating = 4.99 # this is a float
is_published = False # boolean value (can be yes/no)
course_name = "Python Learning" # string
course_message = "Welcome to"

## Working with Strings ##
# How to print strings
print(course_message, course_name)
print(len(course_name)) # a function to get the number of characters in a string (the length of a string)
print(course_name[0]) # prints the first character in the string
print(course_name[0:3]) # slices the string. Returns the first 3 characters in the string
print(course_name[:3]) # Does the same as above
print(course_name[3:6]) # displays the 3rd to 6th characters
print(course_name[0:]) # Does the same as the first example
print(course_name[:]) # Does the same as above

# \" - adds a double quote
# \' - adds a single quote
# \\ - includes a backslash in a string
# \n - new line

#Formated String
first_name = "Alex"
last_name = "Fuller"
# full_name = first_name + " " + last_name ## old way ##
full_name = f"{first_name} {last_name}"
print(full_name)

## String Methods ##
# course_name.upper() - uppercases the string
# course_name.lower() - lowercases the string
# course_name.title() - uppercases the first letter of every word
# course_name.strip() - trim any whitespace at the beginning or ending of the string (good for inputs)
# course_name.lstrip() - left strip
# course_name.rstrip() - right strip
# course_name.find("") - gets the index of a character/a sequence of characters in a string
# course_name.replace("old", "new") - replace a character or a sequence of characters
# print("Lea" in course_name) - checks for the existence of a character or a sequence of characters (is boolean)
# print("Swift" in course_name) - checks if it's not in a character or sequence of characters

print(course_name.upper())
print(course_name.find("Lea"))
print("Lea" in course_name)
print("swift" in course_name) # The "not" operator

## Numbers ##
# Complex numbers
# x 1 + 2j #

#Operations
print(10 + 1)
print(10 - 1)
print(10 * 2)
print(10 / 2) # shows a floating point number
print(10 // 2) # shows the integer point number
print(10 % 2) # remainder of a division (modulus)
print(10 ** 2) # left to the power of right (exponent)

x = 10
x = x + 3 # or x += 3

## Working with numbers ##
# round() - rounds a number
# abs() absolute value
# math module for complex math (import math)

print(round(2.9))
print(abs(-2.9))