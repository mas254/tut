def greet_user_full(first_name, last_name):
    print(f'Hi there {first_name, last_name}!')
    print('Welcome abroad')


def square(number):
    return number * number


result = square(3)
print(result)

print(square(3))

# If no return statement

def square(number):
    print(number * number)

print(square(3))

# If not return statement, None is returned

# By default all functions return None
# Can fix this by coding a return function