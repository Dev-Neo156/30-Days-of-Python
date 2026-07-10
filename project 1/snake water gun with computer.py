import random

def compare(player1_choice, player2_choice):
    if player1_choice == player2_choice:
        return "It's a tie!"
    elif (player1_choice == 'snake' and player2_choice == 'water') or (player1_choice == 'water' and player2_choice == 'gun') or (player1_choice == 'gun' and player2_choice == 'snake'):
        return "Player 1 wins!"
    else:
        return "Computer wins!"
    
random_number = random.choice(['snake', 'water', 'gun'])
computer_choice = random_number
player1_choice = input("Player 1, enter your choice (snake, water, gun): ")


result = compare(player1_choice, computer_choice)
print(f"Computer chose: {computer_choice}")
print(f"You chose: {player1_choice}")
print(result)