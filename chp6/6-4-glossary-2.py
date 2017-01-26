# Exercise 6-4

glossary = {
    'list': 'an object for holding other things such as variables, lists, dictionaries, etc',
    'variable': 'is where you store values for later retrieval and use',
    'tuple': 'an object for storing items that is immutable',
    'immutable': 'cannot be changed', 
    'mutable': 'can be changed',
    }

for term, meaning in sorted(glossary.items()):
    print(term.title() + ": " + meaning + ".\n")


