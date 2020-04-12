coordinates = (1, 2, 3)
coordinates[0] * coordinates[1] * coordinates[2]
# This is long, store in different variables
x = coordinates[0]
y = coordinates[1]
z = coordinates[2]

x * y * z

# By unpacking one can do the same with less code

x, y, z = coordinates

print(x)

# Not limited to tuples, can be lists (created with [] rather than ())