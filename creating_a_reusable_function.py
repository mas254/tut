message = input('>')
words = message.split(' ')
emojis = {
    ':)': 'smiley',
    ':(': 'frowney'
}
output = ''
for word in words:
    output += emojis.get(word, word) + ' '
print(output)

def emojis(message):
    words = message.split(' ')
    emojis = {
        ':)': 'smiley',
        ':(': 'frowney'
    }
    output = ''
    for word in words:
        output += emojis.get(word, word) + ' '
    return output


message = input('>')
result = emojis(message)
print(result)

# An explanation: add the def at the start. The parameter is what we've called message, which is what
# the user inputs (taken from previous code). You don't include the first or last lines (the ones which
# ask for or print input) into your function). Add return output into the function as the function has to
# return a value, which can then be stored into a separate variable.

message = input('>')
print(emojis(message))

# Can make it shorter like so.