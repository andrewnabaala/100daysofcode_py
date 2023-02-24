# Computer program to play rock paper scissors.

import random

print("Hello, welcome to our rock, paper and scissors game.")
choice = input("Choose \n 1 for rock \n 2 for paper \n 3 for scissors")

computer_choice = random.randint(1, 3)
print(f"Computer choses {computer_choice}")

if choice == computer_choice:
    print("Draw")
elif choice == 1 and computer_choice == 2:
    print("Computer wins")
elif choice == 1 and computer_choice == 3:
    print("You win")
elif choice == 2 and computer_choice == 1:
    print("You win")
elif choice == 2 and computer_choice == 3:
    print("Computer wins")
elif choice == 3 and computer_choice == 1:
    print("Computer wins")
else:
    print("You win")
