# You are going to write a program that will select a random name from a list of names. The person selected will have
# to pay for everybody's food bill.

# Important: You are not allowed to use the choice() function.

# Line 11 splits the string names_string into individual names and puts them inside a List called names. For this to
# work, you must enter all the names as names followed by comma then space. e.g. name, name, name

# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
names_length = len(names) - 1
random_number = random.randint(0, names_length)
random_person = names[random_number]
print(f"{random_person} is going to buy the meal today!")
