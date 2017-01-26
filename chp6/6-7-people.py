# Exercise 6-7

person = {'first_name': 'Tom', 'last_name': 'Jones', 'age': 29, 'city': 'New York'}
person_1 = {'first_name': 'Jessica', 'last_name': 'Jones', 'age': 26, 'city': 'New York'}
person_2 = {'first_name': 'Terry', 'last_name': 'Hamilton', 'age': 45, 'city': 'San Antonio'}

people = [person, person_1, person_2]

for person in people:
    print("First Name: " + person['first_name'].title())
    print("Last Name: " + person['last_name'].title())
    print("Age: " + str(person['age']))
    print("City: " + person['city'] + "\n")


