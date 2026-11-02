# Question 4: Using the random module

# TODO: Import the random module
import random
random_number = random.randint(1, 100)
print(random_number)
# TODO: Create a list of colors
colors = ["red", "blue", "green", "yellow", "purple"]
print(colors)
# TODO: Use a for loop to select and print 3 random colors from the list

colors = ["red", "blue", "green", "yellow", "purple"]

for _ in range(3):
    random_color = random.choice(colors)
    print(random_color)