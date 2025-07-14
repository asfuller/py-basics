### Display even numbers between 1-10 ###
# It should look like this:
# 2
# 4
# 6
# 8
# We have 4 even numbers

## My work
#numbers = 9
#even = ""

#while numbers < 9:
#    for x in range(1, numbers, 2):
#        x += 1
#        print(x)
#        even = str(x)
#        print(f"We have: {len(even)} even numbers")
#    break

#Result
count = 0
for x in range(1, 10):
    if x % 2 == 0:
        count += 1
        print(x)
print(f"We have {count} even numbers")


