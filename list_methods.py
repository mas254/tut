numbers = [5, 2, 1, 7, 4]
# Add to end
numbers.append(20)
print(numbers)
# Add to certain position (position, insert)
numbers.insert(0, 10)
numbers.remove(5)
# numbers.clear()
# Removes last
numbers.pop()
# Index of first occurrence
numbers.index(2)
# If not on list it returns error
print(50 in numbers)
numbers2 = [5, 2, 1, 7, 4, 5]
print(numbers.count(5))
print(numbers.sort())
# None answer shows no value
numbers.sort()
print(numbers)
numbers.reverse()
numbers3 = numbers.copy()
numbers.append(10)
print(numbers3)
# Adding to first list after copying doesn't add to second

uniques = []
for no in numbers2:
    if no not in uniques:
        uniques.append(no)
print(uniques)

# If number not in uniques list, add it (that's the append bit)