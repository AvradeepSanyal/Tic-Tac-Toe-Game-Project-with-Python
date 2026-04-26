import random

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
currentplayer = "X" #very game first will be X
winner = None
gamerunning = True


def printboard(board):
    print(board[0] + " | " + board[1] + " | " + board[2] + " | ")
    print("-----------")
    print(board[3] + " | " + board[4] + " | " + board[5] + " | ")
    print("-----------")
    print(board[6] + " | " + board[7] + " | " + board[8] + " | ")



def playerInput(board):
    inp = int(input("Enter a number 1-9: "))
    if inp >= 1 and inp <= 9 and board[inp-1] == "-":
        board[inp-1] = currentplayer
    else:
        print("Oops player already in that spot!")


def checkhorizontal(board):
    global winner
    if (board[0] == board[1] == board[2] and board[0] != "-") or (board[3] == board[4] == board[5] and board[3] != "-") or (board[6] == board[7] == board[8] and board[6] != "-"):
        winner = currentplayer
        return True


def checkrow(board):
    global winner
    if (board[0] == board[3] == board[6] and board[0] != "-") or (board[1] == board[4] == board[7] and board[1] != "-") or (board[2] == board[5] == board[8] and board[2] != "-"):
        winner = currentplayer
        return True
    
def checkDiagonal(board):
    global winner
    if (board[0] == board[4] == board[5] and board[0] != "-") or (board[2] == board[4] == board[6] and board[2] != "-"):
        winner = currentplayer
        return True
    
def checkTie(board):
    global gameRunning
    if "-" not in board:
        printboard(board)
        print("Its a tie")
        gameRunning = False
        

def checkwin():
    if checkDiagonal(board) or checkhorizontal(board) or checkrow(board):
        print(f"The winner is {winner}")


def switchplayer():
    global currentplayer
    if currentplayer == "X":
        currentplayer = "O"
    else:
        currentplayer = "X"


def computer(board):
    while currentplayer == "0":
        position = random.randint(0, 8)
        if board[position] == "-":
            board[position] = "0"
            switchplayer()

while gamerunning:
    printboard(board)
    playerInput(board)
    checkwin()
    checkTie(board)
    switchplayer()
    computer(board)
    checkwin()
    checkTie(board)