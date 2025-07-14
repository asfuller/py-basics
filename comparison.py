## Comparison Operators ##
# 10 > 3 - greater than
# 10 < 3 - less than
# 10 <= 20 - less than or equal to
# 10 >= 20 - greater than or equal to
# 10 == 10 - equal to
# 10 != 10 - is not equal to

## Conditional Statements ##
print("Conditional Statements: ")
temperature = 15

if temperature > 30:
    print("Temperature is greater than 30")
    print("It is warm")
elif temperature > 20:
    print("It's nice")
else:
    print("It's cold")

print("Done")

## Ternary Operator ##
# How to write better/cleaner code
#Let's say we are building an application for a school to check the eligibility of students

age = 22
if age >= 18:
    #print("Eligible")
    message = "Eligible" #this makes it cleaner
else:
    #print("Not eligible")
    message = "Not eligible"
print(message)

# Can also assign a storage value to message
message = "Eligible" if age >= 18 else "Not eligible" #this is the same as the logic above (ternary operator)
print(message)

## Logical Operators ##
#and, or, not
high_income = False
good_credit = True
student = False

# And example
if high_income and good_credit:
    print("Eligible")
else:
    print("Not eligible")

# Or example
if high_income or good_credit:
    print("Eligible")
else:
    print("Not eligible")

# Not example
if not student:
    print("Eligible")  # if student = False
else:
    print("Not eligible")  # if student = True

# Example including everything
if(high_income or good_credit) and not student:
    print("Eligible")
else:
    print("Not eligible")
# Short-circuit Evaluations
# the evaluation of a boolean expression stops as soon as the result is determined
# Logical operators are short-circuit

## Chaining Comparison Operators ##
age = 22
if age >= 18 and age < 65:
    print("Eligible")

#how to write the above in math form
#18 <= age < 65
if 18 <= age < 65:
    print("Eligible")
    