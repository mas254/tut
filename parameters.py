def greet_user(name):
    print(f'Hi there {name}!')
    print('Welcome abroad')


print('Start')
greet_user('John')
greet_user('Mary')
print('Finish')

# Have to give value for parameter (in this case, name)
# Argument the info in a parameter

# shift + f6 to change

def greet_user_full(first_name, last_name):
    print(f'Hi there {first_name, last_name}!')
    print('Welcome abroad')


print('Start')
greet_user_full('John', 'Smith')
print('Finish')