import random

def play():
    player = input("Whats your choice? rock is 'r', paper is 'p', and scissors is 's'. ")
    computer = random.choice(['r', 'p', 's'])

    if computer == player:
        return "It's a tie!"
    
    if is_win(player, computer):
        return f"You Won! computer choice was {computer}"
    
    return f"You Lost! computer choice was {computer}"
    

def is_win(player, opponent):
    if (player == 'p' and opponent == 'r') or (player == 's' and opponent == 'p') or (player == 'r' and opponent == 's'):
        return True
    
print(play())