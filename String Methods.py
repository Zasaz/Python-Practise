course = "  Python Programming"
print(course.upper())
print(course.lower())

# This will capatilize the every first letter of the word.
print(course.title())

# if we have any spaces in a string, in the beginning or ending then it will be
# removed through this:
print(course.strip())

# for Left side
print(course.lstrip())

# for Right side
print(course.rstrip())

# if we want to find the index of a character then:
print(course.find("gramm"))

# if we want to replace some characters then:
print(course.replace("P","j"))

# if we want to find the existance of a character then:
print("Pro" in course)
print("Jyro" in course)
