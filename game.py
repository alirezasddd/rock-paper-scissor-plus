import json
import random


def play_round():
    moves = ["rock", 'paper', 'scissors']

    user_move = input("enter your move(rock/paper/scissor:)").lower()
    if user_move not in moves:
        print("invalid move! please choose(rock/paper/scissor)")
        return None
    
    computer_move = random.choice(moves)
    print(f"computer's move: {computer_move}")
    
    if user_move == computer_move:
        return "tie"
    elif ( 
        ( user_move == "rock" and computer_move == "scissor") or
        ( user_move == "paper" and computer_move == "rock") or
        ( user_move == "scissor" and computer_move == "paper")
    ):
        return "win"
    else:
        return "lose"

def save_scores(scores , filename):
    with open(filename, "w") as file:
        scores = json.dump(scores, file)

def load_scores(filename):
    try:
        with open(filename, "r") as file:
            scores = json.load(file)
        return scores

    except FileNotFoundError:
        return {"user" : 0, "computer" : 0}
    
