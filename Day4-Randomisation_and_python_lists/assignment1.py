# You are going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".
# Remember to use the random module
# Hint: Remember to import the random module here at the top of the file. 🎲

# Write the rest of your code below this line 👇
import random

random_number = random.randint(1, 2)
if random_number == 1:
    print("Heads")
else:
    print("Tails")