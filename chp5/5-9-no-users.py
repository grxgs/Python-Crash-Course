# Exercise 5-9

usernames = ['admin', 'john', 'bill', 'al', 'steve']

if usernames:
    for user in usernames:
        if user == 'admin':
            print("Hello Admin. Would you like to know the current status?")
        else:
            print("Hello " + user + ", thanks for logging in. How are you?")

usernames = []

if usernames:
    print("Hello users!")
else:
    print("We need to find some users!")
