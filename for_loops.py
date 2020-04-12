for item in 'Python':
    print(item)

for item in ['Mark', 'Sam']:
    print(item)

for item in range(10):
    print('i' * item)

# Begins with 0 as Python always bloody does

for item in range(5, 10):
    print(item)

for item in range(5, 10, 2):
    print(item)

# Steps of 2

prices = [10, 20, 30]

total = 0
for item in prices:
    total = total + item
    print(f"Total: {total}")

# Shows cumulative total next to each sum (10, 30, 60)

total = 0
for price in prices:
    total += price
print(f"Total: {total}")