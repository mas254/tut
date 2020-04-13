age = int(input('Age: '))
# Need to put int to let it be known the input will be an integter
print(age)

# Exit code 1 means the programme crashed

# Here's how we should cope with this

try except

try:
    age = int(input('Age: '))
    print(age)
except ValueError:
    print('You mug')

# When this programme runs
# If there is *this* error
# print *this*, rather than crashing

# Can handle more than one type

try:
    age = int(input('Age: '))
    income = 20000
    print(age)
except ValueError:
    print('You mug')

# If 0 is entered, programme will crash as dividing by 0

try:
    age = int(input('Age: '))
    income = 20000
    print(age)
except ValueError:
    print('You mug')
except ZeroDivisionError:
    print('Are you thick')