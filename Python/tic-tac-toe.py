# create tic tac toe game
import random

first_player_name = input("Enter the name of the first player: ")
second_player_name = input("Enter the name of the second player: ")

players = [first_player_name, second_player_name]
random.shuffle(players)

print("\n" * 100) # clear screen
print("Welcome to Tic Tac Toe!")
print(f"{players[0]} (X) will go first.")
print(f"{players[1]} (O) will go second.")
print("\n")

board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

turn = 0

while True:

    # print board
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print(f"-----------")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("-----------")
    print(f" {board[6]} | {board[7]} | {board[8]} ")

    winner = ""

    if board[0] == board[1] == board[2] != " ":
        if (board[0] == "X"):
            winner = players[0]
        else:
            winner = players[1]
    elif board[3] == board[4] == board[5] != " ":
        if (board[3] == "X"):
            winner = players[0]
        else:
            winner = players[1]
    elif board[6] == board[7] == board[8] != " ":
        if (board[6] == "X"):
            winner = players[0]
        else:
            winner = players[1]
    elif board[0] == board[3] == board[6] != " ":
        if (board[0] == "X"):
            winner = players[0]
        else:
            winner = players[1]
    elif board[1] == board[4] == board[7] != " ":
        if (board[1] == "X"):
            winner = players[0]
        else:
            winner = players[1]
    elif board[2] == board[5] == board[8] != " ":
        if (board[2] == "X"):
            winner = players[0]
        else:
            winner = players[1]
    elif board[0] == board[4] == board[8] != " ":
        if (board[0] == "X"):
            winner = players[0]
        else:
            winner = players[1]
    elif board[2] == board[4] == board[6] != " ":
        if (board[2] == "X"):
            winner = players[0]
        else:
            winner = players[1]

    if winner == players[0]:
        print(f"{players[0]} (X) wins!")
        break
    elif winner == players[1]:
        print(f"{players[1]} (O) wins!")
        break

    is_empty = False
    for i in range(0, 9):
        if board[i] == " ":
            is_empty = True
            break
    
    if not is_empty:
        print("It's a tie!")
        break

    if turn == 0:
        player = players[0]
    else:
        player = players[1]
    
    print(f"{player}'s turn.")
    print("\n")
    
    index = int(input("Enter the index of the square (1 - 9): ")) - 1

    if (index < 0 or index > 8):
        print("Invalid index.")
        continue

    if board[index] == " ":
        if turn == 0:
            board[index] = "X"
            turn = 1
        else:
            board[index] = "O"
            turn = 0
    else:
        print("\n" * 100)
        print("That square is already taken.")
        print("\n")
        continue