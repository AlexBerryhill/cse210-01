board = [[1,2,3],[4,5,6],[7,8,9]]
currentTurn = "X"
gameActive = True

def printBoard():
    print("{}|{}|{}".format(board[0][0],board[0][1],board[0][2]))
    print("-+-+-")
    print("{}|{}|{}".format(board[1][0],board[1][1],board[1][2]))
    print("-+-+-")
    print("{}|{}|{}".format(board[2][0],board[2][1],board[2][2]))

def getInput():
    while True:
        try:
            print("\n{}'s turn to choose a square: ".format(currentTurn))
            userInput = int(input())
            break
        except:
            print("That is not a valid option!")
    if userInput > 9 or userInput < 1:
        print("That is not a valid option!")
        userInput = getInput()
    return userInput


def playBoard(input):
    boardSpot = board[int((input-0.1)/3)][(input+2)%3]
    if boardSpot != "X" or boardSpot != "O":
        board[int((input-0.1)/3)][(input+2)%3] = currentTurn

def toggleTurn():
    global currentTurn
    if currentTurn == "X":
        currentTurn = "O"
    else:
        currentTurn = "X"

def main():
    printBoard()
    playBoard(getInput())
    toggleTurn()

while(gameActive == True):
    main()