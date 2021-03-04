# Method 1
for number in range(3):
    print("First Method ")

# Method 2
for number in range(3):
    print("Second Method", number)

# Third Method
for number in range(0, 4):
    print("Third Method", number + 1)

# Fourth Method
# Here 2 is a step, which defines a gap between two numbers
for number in range(1, 10, 2):
    print("Fourth Method", number, number * ".")

print("\n")
# For with if statements
successful = True
for number in range(3):
    print("Attempt")
    if successful:
        print("Message Sent")
        break

print("\n")
# For loop with Else statements
message = False
for number in range(3):
    print("Tried")
    if message:
        print("Message Sent")
        break
else:
    print("Tried 3 times but failed !!!")
