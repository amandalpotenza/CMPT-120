#were gonna make a killer multiplayer tic tac toe game wooo

#asks if user wants instructions
while True:
    instructions = input("Welcome to tic-tac-toe! Would you like instructions? Yes or No?:").lower()
    if instructions == "yes" or instructions == "y":
        print('''Here's how it works. 
    The board will look like this...
    ---
    ---
    ---
    Spaces are assigned numbers 1-9 like so...
    1 2 3 
    4 5 6 
    7 8 9
    Find a friend to play with! Player one ("x") types in the number corresponding to a spot. Then player two ("o") does the same.
    Players take turns until a someone creates a horizontal, vertical, or diagonal line.
===========================
Let's begin!''')
        break
    if instructions == "no" or instructions == "n":
        print("Ok, Let's begin!")
        break

    else:
        print("Try typing \"Yes\" or \"No\"")
        continue

board = ["-","-","-","-","-","-","-","-","-"]


#create a function to print game board
def gameboard():
    x = 0
    while x < 9:
        print(board[x]+board[x + 1]+board[x + 2])
        x += 3
gameboard()


#define main
def main():
    y = 0
    #users take a total of 9 turns unless there is a winner
    while y < 9:
        #determines if user 1 is a winner and ends game
        if board[0]=="x" and board[1]=="x" and board[2]=="x" or board[3]=="x" and board[4]=="x" and board[5]=="x" or board[6]=="x" and board[7]=="x" and board[8]=="x":
            print("congrats user 1! ")
            break
        if board[0]=="x" and board[3]=="x" and board[6]=="x" or board[1]=="x" and board[4]=="x" and board[7]=="x" or board[2]=="x" and board[5]=="x" and board[8]=="x":
            print("congrats user 1! ")
            break
        if board[0]=="x" and board[4]=="x" and board[8]=="x" or board[2]=="x" and board[4]=="x" and board[6]=="x":
            print("congrats user 1! ")
            break

        # determines if user 2 is a winner and ends game
        if board[0] == "o" and board[1] == "o" and board[2] == "o" or board[3] == "o" and board[4] == "o" and board[5] == "o" or board[6] == "o" and board[7] == "o" and board[8] == "o":
            print("congrats user 2! ")
            break
        if board[0] == "o" and board[3] == "o" and board[6] == "o" or board[1] == "o" and board[4] == "o" and board[7] == "o" or board[2] == "o" and board[5] == "o" and board[8] == "o":
            print("congrats user 2! ")
            break
        if board[0] == "o" and board[4] == "o" and board[8] == "o" or board[2] == "o" and board[4] == "o" and board[6] == "o":
            print("congrats user 2! ")
            break

        #user 1 moves. If input is not an int, the program asks for a better input
        elif y % 2 == 0:
            try:
                move1= int(input("user 1: choose an \"x\" position (1-9)"))
                if board[move1-1] == "-":
                    board[move1-1] = "x"
                    gameboard()
                    y += 1
            except:
                gameboard()
                print("invalid input. try again.")

        #user 2 moves. If input is not an int, the program asks for a better input
        else:
            try:
                move1 = int(input("user 2: choose an \"o\" position (1-9)"))
                if board[move1-1] == "-":
                    board[move1-1] = "o"
                    gameboard()
                    y += 1
            except:
                gameboard()
                print("invalid input. try again.")

    #prints "game over!"
    print("game over!")

#run main
main()