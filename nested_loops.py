for x in range(4):
    for y in range(3):
        print(f'({x}, {y})')
# Prints y till it hits 2, then the next lot for x

numbers = [5, 2, 5, 2, 2]

for item in numbers:
    print('x' * item)

for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)