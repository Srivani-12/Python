import random

map_size = 3


treasure_map = [["⬜️" for _ in range(map_size)] for _ in range(map_size)]


abc = ["A", "B", "C"]

def display_map(treasure_map):
    """
    Function to display the treasure map with row and column labels.
    """
    print("\n   " + "   ".join(map(str, range(1, map_size + 1))))  
    for i, row in enumerate(treasure_map):  
        print(f"{abc[i]}  " + "  ".join(row))


treasures_placed = 0
obstacles_placed = 0

for _ in range(9):
    letter = random.choice(abc)
    number = random.randint(1,map_size)
    letter_index = abc.index(letter)
    number_index = number - 1
  
    if treasure_map[letter_index][number_index] == "⬜️":
        
        if treasures_placed == 0:
            mark = " T "
            treasures_placed += 1
        elif obstacles_placed == 0:
            mark = " O "
            obstacles_placed += 1
        else:
            mark = random.choice([" T ", " O "])

        
        treasure_map[letter_index][number_index] = mark


print("Treasure Hunt Game\n")



found_treasures = 0
total_treasures = sum(row.count(" T ") for row in treasure_map)

print("Start the treasure hunt! Guess positions to find all treasures.")
print(" \nyou've only 5 chances to guess the treasure")

chances = 5
is_game_over = False
while chances:

    if found_treasures == total_treasures:
        
        break

    guess = input("Guess a position (e.g., A1): ").strip().upper()

    if len(guess) == 2 and guess[0] in abc and guess[1].isdigit():
        letter = guess[0]
        number = int(guess[1])
        letter_index = abc.index(letter)
        number_index = number - 1

        if letter_index in range(map_size) and number_index in range(map_size):
            if treasure_map[letter_index][number_index] == " T ":
                print("🎉 You found a treasure!")
                treasure_map[letter_index][number_index] = " X "
                found_treasures += 1
            elif treasure_map[letter_index][number_index] == " O  ":
                print("🚫 You hit an obstacle! Be careful.")
            elif treasure_map[letter_index][number_index] == " V ":
                print("⚠️ You've already visited this spot!")
            else:
                print("❌ No treasure here!")
                treasure_map[letter_index][number_index] = " V "
            chances -= 1
            
            
        else:
            print("Position out of bounds! Try again.")
    else:
        print("Invalid position format! Use the format A1, B2, etc.")
    
    print(f"Chances left: {chances}")
    


if found_treasures == total_treasures:
    print(f"\nCongratulations! You found all {total_treasures} treasures!")
else:
    print("\nGame Over! You've run out of chances.")
display_map(treasure_map)
