import random

keyword = ["rock", "paper", "scissors"]

def who_wins(user, pc):
    if user == pc:
        return f"You chose {keyword[user]} and the computer chose {keyword[pc]}. No one wins."
    elif (user == 0 and pc == 2) or (user == 1 and pc == 0) or (user == 2 and pc == 1):
        return f"You chose {keyword[user]} and the computer chose {keyword[pc]}. You win!"
    else:
        return f"You chose {keyword[user]} and the computer chose {keyword[pc]}. The computer wins."

def play_again():
    play = input("Want to play again? Type Yes/No: ").lower()
    while True:
        if play== "yes":
            return True
        else:
            print("Thank You For Playing")
            return False



while True:
    number = int(input("For rock type 0, for paper type 1 & for scissor type 2: "))
    computer = random.choice([0,1,2])
    print(who_wins(number, computer))

    if not play_again():
        break






