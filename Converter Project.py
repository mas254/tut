w = input("How much do you weigh? ")
conv = input("(l)bs or (k)g: ")

l = int(w) * 0.45
k = int(w) * 2.2

if conv == 'l':
    print(f"You weigh {l}kg")
elif conv == 'k':
    print(f"You weigh {k}lbs")

# Shorter solution

w = int(input("How much do you weigh? "))
unit = input("(l)bs or (k)g: ")

if unit.lower() == 'l':
    conv = w * 0.45
    print(f"You are {conv}kg")
else:
    conv = w * 2.2
    print(f"You are {conv}lbs")