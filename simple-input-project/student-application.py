### Student Application ###
# Objective: Get student's first & last name, age, and hobby and display it on screen.
#            Check to see if their info is correct

# Input: Student's first & last name, age, and hobby
# Process: Check whether or not their info is correct
# Output: Display their correct info

# Example
#def greet_student():
#    first_name = input("First name: ")
#    last_name = input("Last name: ")
#    print(f"Hello, {first_name} {last_name}")

#greet_student()
##########################################################

## Input ##
#name = True

#while name:
first_name = input("First name: ")
last_name = input("Last name: ")
age = input("Age: ")
hobby = input("Hobby: ")

student_info = (first_name, last_name, age, hobby)

## Process ##
def get_personal_info(*args):
    return first_name, last_name, age, hobby
get_personal_info(student_info)

## Output ##
def student_personal_info(*args):
    for i in args:
        validate = input("Is the information correct? (y/n): ")
        if validate == "y":
            print(f"{first_name} {last_name} is {age} years old, \n"
                f"on their free time, they like to {hobby}.")
            return

        else:
            print("Try again")

student_personal_info(student_info)
