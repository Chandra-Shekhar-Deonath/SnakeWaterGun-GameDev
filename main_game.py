# Game Development:- Snake Water Gun game
import random

print("SNAKE WATER GUN\n"
      "Rules:- "
      "\n1. Select among three choices:"
      "     \n\tSnake - s"
      "     \n\tWater - w"
      "     \n\tGun - g"
      "\n2. You will get only 10 chances"
      "\n3. Snake drinks water, gun sinks in water but the gun kills snake\n")

draw = 0
win = 0
lost = 0

while (draw + win + lost) < 10:
    ans = input("Enter your choice: ")
    list1 = ["snake", "water", "gun"]
    computer = random.choice(list1)

    # if player chooses snake
    if ans == "s":
        print("Your choice: snake")
        print("Computer: ", computer)
        if computer == "snake":
            print("Draw!")
            draw += 1
        elif computer == "water":
            print("You won")
            win += 1
        elif computer == "gun":
            print("You lost")
            lost += 1
        print()

    # if player chooses water
    elif ans == "w":
        print("Your choice: water")
        print("Computer: ", computer)
        if computer == "water":
            print("Draw!")
            draw += 1
        elif computer == "gun":
            print("You won")
            win += 1
        elif computer == "snake":
            print("You lost")
            lost += 1
        print()

    # if player chooses gun
    elif ans == "g":
        print("Your choice: gun")
        print("Computer: ", computer)
        if computer == "gun":
            print("Draw!")
            draw += 1
        elif computer == "snake":
            print("You won")
            win += 1
        elif computer == "water":
            print("You lost")
            lost += 1
        print()

    # if player types invalid choice
    else:
        print("\nWarning! Invalid choice.\nPlease choose among [s/w/g]\n")

print("Draw: ", draw, "\tWin: ", win, "\tLost: ", lost)
print()

# winner
if win > lost and win > draw:
    print("Winner! You won the game")
elif lost > win and lost >= draw:
    print("Sorry, you lost the game. Computer wins!")
elif win == draw and win == lost:
    print("It's draw!")
