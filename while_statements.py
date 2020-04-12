i = 1
while i >= 5:
    print('*' * i )
    i = i + 1
print("Done")

s_no = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input('Guess: '))
    guess_count += 1
    if guess == s_no:
        print("You win!")
        break
else:
    print("Nope")

# Goes to else if there is no break activated from code