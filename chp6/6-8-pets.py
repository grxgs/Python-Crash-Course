# Exercise 6-8 

tony = {'kind': 'dog', 'owner': 'Jerry'}
cherry = {'kind': 'cat', 'owner': 'Cindy'}
nigel = {'kind': 'bird', 'owner': 'Mack'}

pets = [tony, cherry, nigel]

for pet in pets:
    print("Kind: " + pet['kind'])
    print("Owner: " + pet['owner'] + "\n")
