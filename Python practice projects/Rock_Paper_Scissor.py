"""
Workflow of project:
1-Input from user (Rock,Paper,Scissor)
2-Computer choice (Computer will choose randomly not conditionsllay)
3-Result print

Cases A:
Rock - Rock = Tie
Rock - Paper = Paper win
Rock - Scissor = Rock win

Cases B:
Paper - Paper = Tie
Paper - Rock = Paper win
Paper - Scissor = Scissor win

Cases C:
Scissor - Scissor = Tie
Scissor - Rock = Rock win
Scissor - Paper = Scissor win
"""

import random
item_list = ["Rock","Paper","Scissor"]

user_choice = input("Enter your move = Rock, Paprer, Scissor =")
comp_choice = random.choice(item_list)

print(f"User Choice {user_choice}, Computer Choice {comp_choice}")

if user_choice == comp_choice:
    print("Both chose same = Match Tie")

elif user_choice == "Rock":
    if comp_choice == "Paper":
        print("Paper covers Rock, Computer win")
    else:
        print("Rock smashes scissor, You win")


elif user_choice == "Paper":
    if comp_choice == "Scissor":
        print("Scissor cuts Paper, Computer win")
    else:
        print("Paper covers Rock, You win")


elif user_choice == "Scissor":
    if comp_choice == "Rock":
        print("Rock break Scissor, Computer win")
    else:
        print("Scissor cuts paper, You win")