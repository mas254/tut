def greet_user_full(first_name, last_name):
    print(f'Hi there {first_name, last_name}!')
    print('Welcome abroad')


print('Start')
greet_user_full('Smith', 'John')
print('Finish')

# The above are positional arguments, if you change the order they are printed in the different order

print('Start')
greet_user_full(last_name='Smith', first_name='John')
calc_cost(50, 5, 0.1)
print('Finish')

# This is an example of a keyword argument
# Useful in the below example

print('Start')
greet_user_full(last_name='Smith', first_name='John')
calc_cost(50, 5, 0.1)
print('Finish')


print('Start')
greet_user_full(last_name='Smith', first_name='John')
calc_cost(total=50, shipping=5, discount=0.1)
print('Finish')

# Positional should come first

print('Start')
greet_user_full('Smith', first_name='John')
print('Finish')

# However this doesn't work, as the positional ones are done first so the above would be two first_name