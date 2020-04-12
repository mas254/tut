message = input('>')
# Create separator
message.split(' ')
# So when a user types something, the words are separated by space
words = message.split(' ')
# Showing this is the case
# print(words)
emojis = {
    ':)': 'smiley'
}
output = ''
for word in words:
    output += emojis.get(word, word) + ' '
print(output)
# If they type a word that isn't in the dictionary, the default should just be that word