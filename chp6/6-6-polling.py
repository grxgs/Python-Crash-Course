# Exercise 6-6

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    'jessica': 'julia',
    'nicole': 'javascript',
    }

poll_takers = ['jen', 'sarah', 'hilary', 'harry', 'ash']

for poll_taker in poll_takers:
    if poll_taker in favorite_languages.keys():
        print("Thanks for taking the poll")
    else: 
        print("We'd love it if you took the poll")

