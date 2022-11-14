#were gonna make a killer multiplayer tic tac toe game wooo
instructions = input("Welcome to tic-tac-toe! Would you like instructions? Yes or No?:").lower()
if instructions == "yes":
    print('''Here's how it works. 
The board will look like this...
---
---
---
Spaces are assigned numbers 1-9 like so...
1 2 3 
4 5 6 
7 8 9
Player one ("x") types in the number corresponding to a spot. Then player two ("o") does the same.
Players take turns until a someone creates a horizontal, vertical, or diagonal line.

Let's begin!''')
else:
    print("Ok. Let's begin!")

board = ["-","-","-","-","-","-","-","-","-"]

#create a function to print game board
def gameboard():
    x = 0
    while x < 9:
        print(board[x]+board[x + 1]+board[x + 2])
        x += 3
gameboard()

y = 0
#users take a total of 9 turns unless there is a winner
while y < 9:
    #HERE IS THE QUESTION AREA im not sure ahhhhh
    if board[0]=="x" and board[1]=="x" and board[2]=="x":
        print("congrats user 1! ")
        break
    elif y % 2 == 0:
        move1= int(input("user 1: choose an \"x\" position (1-9)"))
        if board[move1-1] == "-":
            board[move1-1] = "x"
            gameboard()
            y += 1
        else:
            gameboard()
            print("invalid input. try again.")
    else:
        move1 = int(input("user 2: choose an \"o\" position (1-9)"))
        if board[move1-1] == "-":
            board[move1-1] = "o"
            gameboard()
            y += 1
        else:
            gameboard()
            print("invalid input. try again.")

print("game over!")
