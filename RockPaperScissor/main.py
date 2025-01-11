import random
from art import rock,paper,scissors

game_images = [rock,paper,scissors]

user_choice = int(input("What do you choose? type 0 for Rock 1, 1 for Paper or 2 for Scissors"))
print(game_images[user_choice])

computer_choice=random.randint(0,2)

print(f"computer choose {computer_choice}")
print(game_images[computer_choice])     

if user_choice >=3 or user_choice <0:
    print("you entered a invalid number, you lose!")
elif user_choice == 0 and computer_choice==2:
    print("You Win!")
elif user_choice == 2 and computer_choice == 0:
    print("You Lose")
elif user_choice > computer_choice:
    print("you Win!")
elif computer_choice > user_choice:
    print("You Lose!")
elif computer_choice == user_choice:
    print("You Draw!")