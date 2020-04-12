# Name: John Smith
# Email: john@gmail.com
# Phone: 1234

# Curly brackets for dictionary
customer = {
    'name': 'John Smith',
    'age': 30,
    'is_verified': True
}
print(customer['name'])
# Returns value
# Key error if not found
# Case sensitive
print(customer.get('name'))
# Just returns None if not found, not key error
print(customer.get('birthdate', 'Jan 1 1980'))
# Set a default value
customer['name'] = 'JS'
print(customer['name'])
# Easy to add new key value pair

# Phone 1234
phone = input('Phone: ')
'1234'
dictionary = {
    '1': 'One',
    '2': 'Two',
    '3': 'Three',
    '4': 'Four',
    '5': 'Five'
}
output = ''
for no in phone:
    output += dictionary.get(no, '!') + ' '
print(output)

# Setting output to blank
# For no in phone
# Give the corresponding dictionary value for each number to the dictionary value, with a default value
# of ! if a number is given that is not in the dictionary, + a space at the end so the words don't
# run into one another in the output
# print output.