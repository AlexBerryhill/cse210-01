'''
Tic-Tac-Toe
Author: Alex Berryhill
'''
board = [[1,2,3],[4,5,6],[7,8,9]]
currentTurn = "X"
gameActive = True

def main():
    while(gameActive == True):
        print_board()
        play_board(get_input())
        check_win()
        toggle_turn()

def print_board():
    print("{}|{}|{}".format(board[0][0],board[0][1],board[0][2]))
    print("-+-+-")
    print("{}|{}|{}".format(board[1][0],board[1][1],board[1][2]))
    print("-+-+-")
    print("{}|{}|{}".format(board[2][0],board[2][1],board[2][2]))

def get_input():
    while True:
        try:
            print("\n{}'s turn to choose a square (1-9): ".format(currentTurn))
            userInput = int(input())
            break
        except:
            print("That is not a valid option!")
    if userInput > 9 or userInput < 1:
        print("That is not a valid option!")
        userInput = get_input()
    return userInput


def play_board(input):
    boardSpot = board[int((input-0.1)/3)][(input+2)%3]
    if boardSpot != "X" or boardSpot != "O":
        board[int((input-0.1)/3)][(input+2)%3] = currentTurn

def win(draw=False):
    global gameActive
    print_board()
    if(draw):
        print("It is a draw!")
    else:
        print(f"{currentTurn} wins!")
    gameActive = False

def check_draw():
    for i in range(3):
        for j in range(3):
            if board[i][j] != "X" and board[i][j] != "O":
                print(f"[{i}][{j}]")
                return
    win(True)
    return

def check_win():
    if board[0][0] == board[0][1]== board[0][2]:
        win()
    elif board[1][0]==currentTurn and board[1][1]==currentTurn and board[1][2]==currentTurn:
        win()
    elif board[2][0]==currentTurn and board[2][1]==currentTurn and board[2][2]==currentTurn:
        win()
    elif board[0][0]==currentTurn and board[1][0]==currentTurn and board[2][0]==currentTurn:
        win()
    elif board[0][1]==currentTurn and board[1][1]==currentTurn and board[2][1]==currentTurn:
        win()
    elif board[0][2]==currentTurn and board[1][2]==currentTurn and board[2][2]==currentTurn:
        win()
    elif board[0][0]==currentTurn and board[1][1]==currentTurn and board[2][2]==currentTurn:
        win()
    elif board[0][2]==currentTurn and board[1][1]==currentTurn and board[2][0]==currentTurn:
        win()
    else:
        check_draw()


def toggle_turn():
    global currentTurn
    if currentTurn == "X":
        currentTurn = "O"
    else:
        currentTurn = "X"

if __name__ == "__main__":
    main()
