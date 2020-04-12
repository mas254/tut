names = ['John', 'Bob', 'Mosh', 'Sarah', 'Max']
# Start of list
print(names[0])
# End of list
print(names[-1])
# Second from end
print(names[-2])
print(names[2:4])
# To end
print(names[2:])
# From start
print(names[:])
# Editing
names[0] = 'Jon'
print(names[0])

# Finding largest number in list
numbers = [3, 6, 2, 8, 4, 10]
# Set max to first number, then iterate to each number and if larger, set max to that number
max = numbers[0]
for no in numbers:
    if no > max:
        max = no
print(max)