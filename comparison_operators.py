# Compare variable with value

temperature = 35
if temperature >= 30:
    print("It's a hot day")
else:
    print("It's not a hot day")

name = 'given'

if len(name) < 3:
    print("Name must be at least 3 characters long")
elif len(name) > 50:
    print("Name be must a maximum of 50 characters long")
else:
    print("Name looks good!")
