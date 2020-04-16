numbers = [10, 3, 6, 2]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)

def find_max(numbers):
    max = numbers[0]
    for number in numbers:
        if number > max:
            max = number
    return max

numbers = [10, 3, 6, 2]
print(max)

# New python file called utils (code won't work as I didn't actually create the file)

# utils:
def find_max(numbers):
    max = numbers[0]
    for number in numbers:
        if number > max:
            max = number
    return max

# here
import utils
utils.find_max()
# OR
from utils import find_max

numbers = [10, 3, 6, 2]
max = find_max(numbers)
print(max)

# warning as overwritten built-in max function

numbers = [10, 3, 6, 2]
print(max(numbers))
# above no longer works as have overwritten max function. If want to do this, call max function maximum