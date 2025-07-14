### LOOPS ###

## For Loops ##
#number = int
#range() = Create and return a new object
#for number in range(3):
    #print("Attempt", number + 1, (number + 1) * ".")

# Same as above
#for number in range(1, 4):
    #print("Attempt", number + 1, (number + 1) * ".")

# Add a 3rd argument as a step
#for number in range(1, 10, 2):
    #print("Attempt", number + 1, (number + 1) * ".")

## For Else ##
#successful = True
#for number in range(3):
#    print("Attempt")
#    if successful:
#        print("Successful")
#        break #stops the loop

#if after 3 attempts, show an error
#sucessful = False
#for number in range(3):
#    print("Attempt")
#    if sucessful:
#        print("Successful")
#        break
#else: #if it doesn't break out of the loop statement
#    print("Attempted 3 times and failed")

## Nested Loop ##
#for x in range(5): # outer loop
#    for y in range(3): #inner loop
#        print(f"({x},{y})")

## Iterables ##
# you can iterate something (any object)
#for x in "Python":
#    print(x)

# you can also create your own object and iterate the values there
#for item in shopping_cart:
#    print(item)

## While Loops ##
#repeats something as long as something is true

#number = 100
#while number > 0:
#    print(number)
#    number //= 2

#Example 2
#command = ""
#while command != "quit" and command != "QUIT": #this is a poor way to check quit command
#    command = input(">")
#    print("ECHO: ", command)

#Example 3: with better quit command
#command = ""
#while command.lower() != "quit":
#    command = input(">")
#    print("ECHO: ", command)

## Infinite Loops ##
# a loop that runs forever (ALWAYS HAVE A WAY TO BREAK OUT OF IT)
while True:
    command = input(">")
    print("ECHO: ", command)
    if command.lower() != "quit":
        break