from minimax import Minimax
from TicTacToe import TicTacToe

import numpy as np

import pygame


WHITE = (255, 255, 255)
BACKGROUND = (0, 0, 0)
GREY = (169,169,169)
BLUE = (0,0,255)
SKYBLUE = (135,206,235)

RED = (255,0,0)
SALMON = (250,128,114)

class Button:
    def __init__(self, screen, text, pos, size, color):
        self.rect = pygame.Rect(pos[0], pos[1], size[0], size[1])
        self.pos = pos
        self.size = size
        self.screen = screen
        self.text = text
        self.color = color

        self.myfont = pygame.font.SysFont('Comic Sans MS', 15)

    def draw(self):
        pygame.draw.rect(self.screen, GREY, pygame.Rect(self.pos[0]-3, self.pos[1]-3, self.size[0]+6, self.size[1]+6))
        pygame.draw.rect(self.screen, self.color, self.rect)
        textsurface = self.myfont.render(self.text, False, BACKGROUND)

        text_x = self.pos[0] + self.size[0]/(len(self.text))#4.0
        text_y = self.pos[1] + self.size[1]/4
        self.screen.blit(textsurface, (text_x, text_y))

    def checkIfOver(self):
        m_pos = pygame.mouse.get_pos()
        if m_pos[0] > self.pos[0] and m_pos[1] > self.pos[1]:
            if m_pos[0] < self.pos[0]+self.size[0] and m_pos[1] < self.pos[1]+self.size[1]:
                return True
        
        
        return False



class Game:
    def __init__(self):

        self.ai = Minimax()
        self.game = TicTacToe()
        self.maxRec = 5
        self.wins = [0,0]



        pygame.init()
        pygame.font.init()
        
        self.screen_size = (600,400)
        self.screen = pygame.display.set_mode(self.screen_size)
        
        self.reset_button = Button(self.screen, "Reset", [10,10], [100,40], WHITE)
        self.difficulty_button = Button(self.screen, "Change AI", [10,90], [100,40], WHITE)

        self.drawAll()
        


    def drawFrame(self):
        x_min = self.screen_size[0] - self.screen_size[1] + 50
        x_max = self.screen_size[0] - 50
        y_min = 50
        y_max = self.screen_size[1] - 50


        self.x_min, self.x_max, self.y_min, self.y_max = x_min, x_max, y_min, y_max
        self.dist = (x_max-x_min)/3.0
        dist = self.dist
        self.centers = []
        for j in range(3):
            center_y = y_min + (0.5 + j)*dist
            for i in range(3):
                center_x = x_min + (0.5 + i)*dist   
                self.centers.append([int(center_x), int(center_y)])


                

        pygame.draw.lines(self.screen, WHITE, True, [(x_min + dist, y_min), (x_min + dist, y_max)], 4)
        pygame.draw.lines(self.screen, WHITE, True, [(x_min + 2*dist, y_min), (x_min + 2*dist, y_max)], 4)

        pygame.draw.lines(self.screen, WHITE, True, [(x_min, y_min + dist), (x_max, y_min + dist)], 4)
        pygame.draw.lines(self.screen, WHITE, True, [(x_min, y_min + 2*dist), (x_max, y_min + 2*dist)], 4)



    def drawCross(self, square, is_last=False):
        center = self.centers[square]
        color = SKYBLUE if is_last else BLUE
        pygame.draw.lines(self.screen, color, True, [(center[0] - 0.25*self.dist, center[1] + 0.25*self.dist), (center[0] + 0.25*self.dist, center[1] - 0.25*self.dist)], 4)
        pygame.draw.lines(self.screen, color, True, [(center[0] + 0.25*self.dist, center[1] + 0.25*self.dist), (center[0] - 0.25*self.dist, center[1] - 0.25*self.dist)], 4)

    def drawCircle(self, square, is_last=False):
        center = self.centers[square]
        color = SALMON if is_last else RED
        pygame.draw.circle(self.screen, color, center, int(self.dist*0.33), 3)  

    
    def drawBoard(self):
        board = self.game.board

        self.screen.fill(BACKGROUND)
        self.drawFrame()
        for index, player in enumerate(board):
            if player == 1:
                is_last = True if self.game.playerMoves[0][0] == index and len(self.game.playerMoves[0]) == 3  else False
                self.drawCross(index, is_last)
            elif player == 2:
                is_last = True if self.game.playerMoves[1][0] == index and len(self.game.playerMoves[1]) == 3 else False
                self.drawCircle(index, is_last)
            else:
                continue

    def drawAiText(self):
        myfont = pygame.font.SysFont('Comic Sans MS', 15)
        text = "AI Level: %s" %(self.maxRec)
        textsurface = myfont.render(text, False, WHITE)
        self.screen.blit(textsurface, (10, 180))

    def drawWins(self):
        myfont = pygame.font.SysFont('Comic Sans MS', 15)
        text1 = "Wins:" 
        text2 = "Player: %d" %self.wins[0]
        text3 = "AI      : %d" %self.wins[1]
        textsurface = myfont.render(text1, False, WHITE)
        self.screen.blit(textsurface, (10, 210))

        textsurface = myfont.render(text2, False, WHITE)
        self.screen.blit(textsurface, (10, 230))

        textsurface = myfont.render(text3, False, WHITE)
        self.screen.blit(textsurface, (10, 245))

    

    def drawAll(self):
        self.drawBoard()
        self.reset_button.draw()
        self.difficulty_button.draw()
        self.drawAiText()
        self.drawWins()

        
    def getSquarePointedAt(self):
        m_pos = pygame.mouse.get_pos()
        if m_pos[0] > self.x_min and m_pos[0] < self.x_max and m_pos[1] > self.y_min and m_pos[1] < self.y_max:
            x = (m_pos[0] - self.x_min)//self.dist
            y = (m_pos[1] - self.y_min)//self.dist
            
            return True, int(x + 3*y)

        else:
            return False, None

    def changeAI(self):
        self.maxRec = (self.maxRec+1)%6
        self.maxRec = 1 if self.maxRec == 0 else self.maxRec
        

    def reset(self):
        self.game = TicTacToe()
        self.move_taken = False
        self.game_over = False
        self.drawAll()

    def run(self):
        running = True
        self.move_taken = False
        self.game_over = False
        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        self.reset()
                        
        
                if event.type == pygame.MOUSEBUTTONUP:

                    if self.reset_button.checkIfOver():
                        self.reset()
                    if self.difficulty_button.checkIfOver():
                        self.changeAI()

                    is_square, square = self.getSquarePointedAt()
                    if is_square and self.game.playerToMove == 0 and not self.game_over:
                        if self.game.makeMove(square):
                            print("hei")
                            #self.drawAll()
                            self.move_taken = True
                                               
            if self.game.playerToMove == 1 and not self.move_taken and not self.game_over:
                #ai_move = self.ai.getMove(self.game, 2, self.maxRec)
                ai_move = self.ai.findBestMove(self.game, 2, self.maxRec)
                self.game.makeMove(ai_move)
                #self.drawAll()
           
            self.drawAll() 
            pygame.display.update()




            winner = self.game.checkWinner()
            if winner and not self.game_over:
                print("Player %s won" %(int(winner)))
                self.game_over = True
                self.wins[int(winner-1)] += 1
            
            
            self.move_taken = False  

        




if __name__=="__main__":
    game = Game()
    game.run()

    
