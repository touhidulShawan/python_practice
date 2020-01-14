#  Rock Paper Scissors Advanced version
from random import randint

print(
    """
---------------------
|  <-- Rock -->     |
|  <-- Paper -->    |
|  <-- Scissors --> |
---------------------
"""
)

computer_score = 0
user_score = 0
remaining_move = 3

# Show Current scoreboard


def show_score_list():
    print("--------------------------")
    print(f" Computer Score -> {computer_score}")
    print(f" User Score -> {user_score}")
    print("--------------------------")
    print(f" You have only {remaining_move} turn")
    print("-------------------------")

# Show Final Score


def show_final_result():
    if computer_score == user_score:
        print("""
|*************************|    
|        Game Draw        |
|*************************|
""")
    elif computer_score > user_score:
        print("""
|------------------------|    
| Sorry! Computer Wins!! |   
|------------------------|    
    """)
    else:
        print("""
|=======================|    
|     Yoo!! You Win     |
|=======================|
""")


# Game Logic
while True:
    random_num = randint(1, 3)
    # make computer choice
    if random_num == 1:
        computer_choice = "rock"
    elif random_num == 2:
        computer_choice = "paper"
    elif random_num == 3:
        computer_choice = "scissors"

    user_choice = input("Make your move --> ").lower()

    if user_choice == computer_choice:
        print(f"Computer choose {computer_choice}")
        print("It`s a tie!!")
        show_score_list()
    elif user_choice == "rock":
        if computer_choice == "paper":
            computer_score += 1
            remaining_move -= 1
        elif computer_choice == "scissors":
            user_score += 1
            remaining_move -= 1
        print(f"Computer choose {computer_choice}")
        show_score_list()
    elif user_choice == "paper":
        if computer_choice == "scissors":
            computer_score += 1
            remaining_move -= 1
        elif computer_choice == "rock":
            user_score += 1
            remaining_move -= 1
        print(f"Computer choose {computer_choice}")
        show_score_list()
    elif user_choice == "scissors":
        if computer_choice == "rock":
            computer_score += 1
            remaining_move -= 1
        elif computer_choice == "paper":
            user_score += 1
            remaining_move -= 1
        print(f"Computer choose {computer_choice}")
        show_score_list()
    else:
        print("Please enter a valid move")
    if remaining_move == 0:
        break
show_final_result()
