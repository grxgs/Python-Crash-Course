# Exercise 4-12

pizzas = ['pepperoni', 'cheese', 'meat lovers', 'veggie']
friends_pizza = pizzas[:]
friends_pizza.append("extra cheese")

for pizza in pizzas:
    print("My favorite pizzas are: " + pizza + ".")

for pizza in friends_pizza:
    print("My friend's favorite pizzas are: " + pizza + ".")

