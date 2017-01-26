# Exercise 5-10

current_users = ['Al', 'Steve', 'Bob', 'George', 'Tom']
new_users = ['Al', 'Steve', 'Henry', 'Eli', 'Walter']

for new_user in new_users:
    if new_user in current_users:
        print(new_user + " is not an available username. Please choose a new one")
    else:
        print(new_user + " is available.")

