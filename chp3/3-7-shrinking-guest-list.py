# Exercise 3-4

guest_list = ['Albert A', 'John K', 'Alexander G']
print(guest_list[0] + ", Please join me for dinner.")
print(guest_list[1] + ", Please join me for dinner.")
print(guest_list[2] + ", Please join me for dinner.")
print("We have found more space. We will invite some new people")
guest_list.insert(0, 'Bill C')
guest_list.insert(2, 'Kanye W')
guest_list.append('Bill M')
print(guest_list[0] + ", Please join me for dinner.")
print(guest_list[1] + ", Please join me for dinner.")
print(guest_list[2] + ", Please join me for dinner.")
print(guest_list[3] + ", Please join me for dinner.")
print(guest_list[4] + ", Please join me for dinner.")
print(guest_list[5] + ", Please join me for dinner.")

print("The new table won't arrive in time. I can only invite 2 guests")

print(guest_list.pop() + ", I'm sorry but I can't invite you to dinner")
print(guest_list.pop() + ", I'm sorry but I can't invite you to dinner")
print(guest_list.pop() + ", I'm sorry but I can't invite you to dinner")
print(guest_list.pop() + ", I'm sorry but I can't invite you to dinner")

print(guest_list[0] + " and " + guest_list[1] + " you are still invited.")
del guest_list[1]
del guest_list[0]

print(guest_list)
