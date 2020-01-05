from TicTacToe import TicTacToe
from copy import copy, deepcopy
import numpy as np

import sys
sys.setrecursionlimit(100)

class Minimax:
    def __init__(self):
        pass

    def checkMove(self, obj: TicTacToe, player: int, turn: int, maxRec: int) -> list:
        legal_moves = obj.getLegalMoves() 
        moves = np.ones(9)*(0)
        if len(legal_moves) > 0 and maxRec > 0:
            for move in legal_moves:
                pack = deepcopy(obj.pack())
                obj.makeMove(move)

                winner = obj.checkWinner()

                if winner == 0:
                    r = self.checkMove(obj, player,(turn)%2 + 1, maxRec - 1)[:]
                    moves[move] += np.min(r) if turn == player else np.max(r)
                else:
                    moves[move] += 10 if winner == player else -10

                obj.unpack(pack)
            
        return moves


    def getMove(self, game: TicTacToe, player: int, maxRec: int) -> int:
        pack = deepcopy(game.pack())
                
        ai_moves = self.checkMove(game, player, player, maxRec)
        
        game.unpack(pack[:])
        
        if np.sum(np.where(ai_moves == np.max(ai_moves), 1, 0)) != 0:
            can_take = []
            legal_moves = game.getLegalMoves()
            max_moves = np.where(ai_moves == np.max(ai_moves), 1, 0)
            for i in range(9):
                if max_moves[i] and i in legal_moves:
                    can_take.append(i)
            if len(can_take) != 0:
                ai_move = np.random.choice(can_take)
            else:
                ai_move = np.random.choice(legal_moves)
        else:
            ai_move = np.argmax(ai_moves)

        return ai_move



if __name__=="__main__":
    game = TicTacToe()
    ai = Minimax()
    maxRec = 2
    while True:
        while True:
            move = input("Make move")
            if move == "q":
                exit()
            if game.makeMove(move):
                break

        winner = game.checkWinner()
        if winner:
            print("Player %s won" %(int(winner)))
            break

        while True:
            
            ai_move = ai.getMove(game, 2, maxRec)
            
            if game.makeMove(ai_move):
                break

        print(ai_move)
        game.drawBoard()
        winner = game.checkWinner()
        if winner:
            print("Player %s won" %(int(winner)))
            break

            


