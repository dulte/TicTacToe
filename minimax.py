from TicTacToe import TicTacToe
from copy import copy, deepcopy
import numpy as np

import sys
sys.setrecursionlimit(100)

class Minimax:
    def __init__(self):
        pass
    """
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
        
    """
    def checkMoveV2(self, obj: TicTacToe, player: int, getMax: bool, maxRec: int) -> int:
        best = -1 if getMax else 1
        legal_moves = obj.getLegalMoves()

        winner = obj.checkWinner()
        if winner:
            return 10 if winner == player else -10
        else:
            if len(legal_moves) > 0 and maxRec > 0:
                for move in legal_moves:
                    pack = deepcopy(obj.pack())
                    obj.makeMove(move)

                    if getMax:
                        best = max([best,self.checkMoveV2(obj, player,not getMax, maxRec - 1)])
                    else:
                        best = min([best,self.checkMoveV2(obj, player,not getMax, maxRec - 1)])
                    
                    obj.unpack(pack)
            
            return best

    
    def findBestMove(self, obj: TicTacToe, player: int, maxRec: int) -> int:
        #If it is the AI's first turn, always place in center or corner
        if len(obj.playerMoves[1]) == 0:
            if obj.board[4] == 0:
                return 4
            else:
                return np.random.choice([0,2,6,8]) 

        legal_moves = obj.getLegalMoves()
        best = -1000
        best_move = legal_moves[0]
        for move in legal_moves:
            pack = deepcopy(obj.pack())
            obj.makeMove(move)

            value = self.checkMoveV2(obj, player, False, maxRec)
            obj.unpack(pack)
            print(value, move)

            if value > best:
                best = value
                best_move = move

        

        return best_move

        


    def getMove(self, game: TicTacToe, player: int, maxRec: int) -> int:
        pack = deepcopy(game.pack())
        

        #If it is the AI's first turn, always place in center or corner
        if len(game.playerMoves[1]) == 0:
            if game.board[4] == 0:
                return 4
            else:
                return np.random.choice([0,2,6,8])
                
        ai_moves = self.checkMove(game, player, player, maxRec)
        
        print(ai_moves)
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

            


