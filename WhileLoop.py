number = 100
while number > 0:
    print(number)
    number //= 2

# Example 2
command = ""
while command != "quit":
    command = input(">> ")
    print("Hello ", command)

# Example 3
Message = ""
while Message.lower() != "quit":
    Message = input(">> ")
    print("Hello, ", Message)
