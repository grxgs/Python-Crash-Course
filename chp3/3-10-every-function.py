# Exercise 3-10

streets = ['Broadway', 'Martin Luther King Dr', 'Main St']

print("Append")
streets.append('Hollywood Ave')
print(streets)

print("Insert")
streets.insert(0, "Home St")
print(streets)

print("Delete")
del streets[0]

print("Temp Sort")
print(sorted(streets))

print("Perm Sort")
streets.sort()
print(streets)

print("Reverse Sort")
streets.reverse()
print(streets)

print("Length of List")
print(len(streets))
