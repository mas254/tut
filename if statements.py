# if it's hot
    # it's a hot day
    # drink plenty of water
# otherwise if it's cold
    # it's a cold day
    # wear warm clothers
# otherwise
    # it's a lovely day

is_hot = False

if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
print("Enjoy your day")

is_hot = True

if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
else:
    print("It's a cold day")
    print("Wear warm clothes")
print("Enjoy your day")

is_hot = False
is_cold = True

if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes")
else:
    print("It's a lovely day")
print("Enjoy your day")

good = True

if good:
    print("10% off!")
    print("Price is:")
    print(1000000 * 0.1)
else:
    print("Uh oh")
    print("Price is:")
    print(1000000 * 0.2)

price = 1000000
good = True

if good:
    down = 0.1 * price
else:
    down = 0.2 * price
print(f"Down payment: ${down}")