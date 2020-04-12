# >
# start - to start the car
# stop - to stop the car
# quit - exit
# Car started, ready to go!
# Car stopped
# I don't understand that!

in_ = '>'

while in_ != 'quit':
    in_ = input('>')
    if in_.lower() == 'start':
        print("Car started, ready to go!")
    elif in_.lower() == 'stop':
        print("Car stopped")
    elif in_.lower() == 'quit':
        print("Exit")
        break
    elif in_.lower() == 'help':
        print('''
start - to start the car
stop - to stop the car
quit - exit
        ''')
    else:
        print("I don't understand that!")

# This is what he asked for

# Can also start with 'while True'

# Stopping the repetition problem on next sheet