
not_started = True
stopped = True

while True:
    in_ = input('>')
    if in_.lower() == 'start':
        if not_started:
            print("Car started, ready to go!")
            not_started = False
            stopped = False
        else:
            print("Car already started!")
    elif in_.lower() == 'stop':
        if stopped:
            print("Car already stopped!")
        else:
            print("Car stopped")
            stopped = True
            not_started = True
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

# Add status?
# a & b = x then status = started otherwise status = stopped
# Could just use the one started variable to save a few lines of code