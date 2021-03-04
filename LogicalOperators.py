grades = True
behavior = True
age = False

if (grades or behavior) and not age:
    print("Enrolled")
else:
    print("Cancelled")
