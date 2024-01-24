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
        (user_move == "rock" and computer_move == "scissor") or
        (user_move == "paper" and computer_move == "rock") or
        (user_move == "scissor" and computer_move == "paper")
    ):
        return "win"
    else:
        return "lose"


def save_scores(scores, filename):
    with open(filename, "w") as file:
        scores = json.dump(scores, file)


def load_scores(filename):
    try:
        with open(filename, "r") as file:
            scores = json.load(file)
        return scores

    except FileNotFoundError:
        return {"user": 0, "computer": 0}


def main():
    scores = load_scores("scores.json")
    round_count = 0

    while round_count < 10:
        print("\nrock paper scissor list:")
        print("one >>> play roand")
        print("two >>> viwe scores")
        print("three >>> save scores")
        print("four >>> exite")

        choice = input("choice between one to four :")

        if choice == "one".lower():
            result = play_round()
            if result == "win":
                scores["user"] += 1
            elif result == "lose":
                scores["computer"] += 1
            elif result == "tie":
                print("tie!")
            round_count += 1

        elif choice == "two".lower():
            print(F"user : {scores['user']} - computer : {scores['computer']}")

        elif choice == "three".lower():
            save_scores(scores, "scores.json")
            print("scores saved")

        elif choice == "four".lower():
            save_scores(scores, "score.json")
            print("game over.")
            break
        else:
            print("the request not finded")

        if round_count == 10:
            print("\nGame Over!")
            if scores['user'] > scores['computer']:
                print("You win!")
            elif scores['user'] < scores['computer']:
                print("Computer wins!")
            else:
                print("It's a tie!")


if __name__ == "__main__":
    main()
