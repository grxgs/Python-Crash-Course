# Exercise 4-10

cubes = []
for num in range(1, 11):
    cubes.append(num**3)

print(cubes)

print("The first three cubes in the list are: ")
print(cubes[0:3])

print("Three items from the middle of the list are: ")
print(cubes[4:7])

print("The last three items in the list are: ")
print(cubes[-3:])
