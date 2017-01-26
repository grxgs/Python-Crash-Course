# Exercise 6-2

fav_nums = {'Jessica': [56, 45, 87], 'Terry': [19, 63, 48], 'Felicia': [16, 40], 'Tiffany': [90, 9, 4, 2], 'Nicole': [23, 21]}

print("Here are everyone's favorite numbers")

for k, v in fav_nums.items():
    print("\n" + k.title() + "'s" + " favorite numbers are as follows: \n")
    for num in v:
        print(num)
