course = '''
Hi,
Here's a "test"
Fin.
'''
print(course)
print(course[0])
# This is the index of the first character, which in
# this case is a new line
print(course[-1])
# This is one less than the first, treating the
# string as a repeating line (i.e. in this instance,
# this is the final character.
print(course[0:3])
# Chooses from x to y, excluding y
print(course[:9])
# Python assumes start and end index if left blank

name = "Jennifer"
print(name[1:-1])