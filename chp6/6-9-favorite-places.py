# Exercise 6-9

favorite_places = {'Jessica': ['Tahiti', 'New York'], 'John': ['Chicago'], 'Nancy':['Tokyo', 'Manila', 'Paris']}

for k, v in favorite_places.items():
    print("\n" + k.title() + "'s" + " favorite places are below: ")
    for place in v:
        print(place.title())


