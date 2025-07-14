## Type Conversion ##

# input - gets input from the user
# These convert inputs into specific types:
# int(x)
# float(x)
# bool(x)
# str(x)
#print(type(x))  # displays <class 'str'>

x = input("x: ")

# y = x  + 1 this will return an error since they're two different characters
y = int(x) + 1
# print(y) - displays the value
print(f"x: {x}, y: {y}")

#For booleans
# Falsey
# ""
# None
# Anything else is True