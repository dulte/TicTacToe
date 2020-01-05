import numpy as np
import sys,os


class TicTacToe:
    def __init__(self, printMesseges = False):

        self.printMesseges = printMesseges
        self.board = np.zeros(9)
        self.playerToMove = 0
        self.playerOne = []
        self.playerTwo = []

        self.playerMoves = {0:self.playerOne,1:self.playerTwo}


    def copy(self):
        new_obj = TicTacToe()
        new_obj.board = self.board
        new_obj.playerToMove = self.playerToMove
        new_obj.playerOne = self.playerOne
        new_obj.playerTwo = self.playerTwo
        new_obj.playerMoves = self.playerMoves

        return new_obj

    def pack(self):
        return np.copy([self.board, self.playerToMove, self.playerOne, self.playerTwo, self.playerMoves])

    def unpack(self, pack):
        self.board = pack[0]
        self.playerToMove = pack[1]
        self.playerOne = pack[2]
        self.playerTwo = pack[3]
        self.playerMoves = pack[4]

        

    def isMovesIsLegal(self,move):

        try:
            if self.board[int(move)] != 0:
                if self.printMesseges:
                    print("There is another player there!")
                return False
            else:
                return True
        except ValueError:
            if self.printMesseges:
                print("Move did not make sense!")
            return False
        except IndexError:
            if self.printMesseges:
                print("Move not inside the board!")
            return False


    def getLegalMoves(self):
        moves = []
        for i in range(9):
            if self.board[i] == 0:
                moves.append(i)

        return moves

    def updateBoard(self):

        self.board = np.zeros(9)
        for key in self.playerMoves:
            for moves in self.playerMoves[key]:
                if moves != None:
                    self.board[moves] = key + 1


    def makeMove(self,move,checkWinner = False):
        
        try:
            if len(self.playerMoves[self.playerToMove]) > 2:
                self.playerMoves[self.playerToMove].pop(0)
        except:
            pass

        if not self.isMovesIsLegal(move):
            return False

        self.playerMoves[self.playerToMove].append(int(move))

        self.playerToMove = (self.playerToMove + 1)%2

        self.updateBoard()

        return True

        if checkWinner:
            self.checkWinner()

    def checkWinner(self):
        board = np.reshape(self.board.copy(),(3,3))

        if board[0][0] != 0:
            if (board[0][0] == board[1][0] and board[0][0] == board[2][0]):
                return(board[0][0])
            if (board[0][0] == board[0][1] and board[0][0] == board[0][2]):
                return(board[0][0])
            if (board[0][0] == board[1][1] and board[0][0] == board[2][2]):
                return(board[0][0])

        if board[1][1] != 0:
            if (board[1][1] == board[1][0] and board[1][1] == board[1][2]):
                return(board[1][1])
            if (board[1][1] == board[0][1] and board[1][1] == board[2][1]):
                return(board[1][1])
            if (board[1][1] == board[0][2] and board[1][1] == board[2][0]):
                return(board[1][1])

        if board[2][2] != 0:
            if (board[2][2] == board[1][2] and board[2][2] == board[0][2]):
                return(board[2][2])
            if (board[2][2] == board[2][1] and board[2][2] == board[2][0]):
                return(board[2][2])

        return 0
    
    def getLastPlay(self):
        return self.playerMoves[self.playerMoves][0]


    def drawBoard(self, clearScreen = False):
        if clearScreen:
            os.system("cls")


        squareBoard = np.reshape(self.board.copy(),(3,3))
        print(squareBoard)

    def getBoard(self,square=False):
        if square:
            return np.reshape(self.board.copy(),(3,3))
        else:
            return self.board


if __name__ == "__main__":
    game = TicTacToe()
    while True:
        move = input("Make move")
        if move == "q":
            break
        game.makeMove(move)
        game.drawBoard()
        winner = game.checkWinner()
        if winner:
            print("Player %s won" %(int(winner)))
            break
