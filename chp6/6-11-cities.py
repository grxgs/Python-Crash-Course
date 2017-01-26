# Exercise 6-11

cities = {
    'Chicago': {
        'country': 'usa',
        'population':'2 million',
        'fact':'Chicago is located in the Midwestern region of the US'
    },
    'New York': {
        'country': 'usa',
        'population': '10 million',
        'fact': 'New York is the largest city in the US'
    },
    'Paris': {
        'country': 'France',
        'population': '2 million', 
        'fact': 'Paris is home of the Eiffel Tower'
    }
}

for k, v in cities.items():
    print("\n" + k.title() + "." + "Here are some facts: " + "\n")
    for fact in v.values():
        print(fact)


