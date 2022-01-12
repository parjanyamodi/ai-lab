import numpy as np
import random
board = [['-','-','-'],
['-','-','-'],
['-','-','-']]

def isDraw(board) :
    for i in range(3) :
        for j in range(3) :
            if board[i][j] == '-' :
                return False
    return True

def isWon(board) :
    for i in range(3) :
        if (board[0][i] == board[1][i] and board[2][i] == board[1][i] and board[2][i]!='-') :
            return True
        if board[i][0] == board[i][1] and board[i][2] == board[i][1] and board[i][2]!='-' :
            return True
            
    if(board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[2][2]!='-') :
        return True
    
    if(board[0][2] == board[1][1] and board[2][0] == board[1][1] and board[2][0]!='-') :
        return True
        
    return False

def display(board) :
    print(np.matrix(board))
    
    
def game(board) :
    print("You are X and computer is O")
    isTurn = True
    for i in range(9) :
        display(board)
        if(isDraw(board)) :
            print("Game has ended in a draw!")
            return
        if i%2 == 0 :
            print("It is your turn : ")
            print("Enter row and column : ")
            row = int(input())
            col = int(input())
            while board[row-1][col-1] != '-' :
                print("Invalid Move! Please Enter again")
                row = int(input())
                col = int(input())
            board[row-1][col-1] = 'X'
            if isWon(board) :
                print("You Win!")
                display(board)
                return
        else :
            print("Computer's turn : ")
            row = random.randint(0,2)
            col = random.randint(0,2)
            while(board[row][col]!='-') :
                row = random.randint(0,2)
                col = random.randint(0,2)
            board[row][col]='O'
            if isWon(board) :
                print("Computer Wins!")
                display(board)
                return
game(board)
