import math , time
class AIPlayer :
    count = 0 
    def __init__(self , name , game) -> None:
        self.name  = name 
        self.game = game
        self.__scores = {
            "X" : 10,
            "O" : -10,
            "tie" : 0
        }
        self.__infinity = math.pow(10,100)
        # print(self.__infinity)

    def __str__(self):
        return  self.name 
    
    def checkWinner(self):
        if self.game.is_win():
            return self.game.player
        elif self.game.is_draw():
            return 'tie'
        else :
            return None
    

    def minmax(self,  depth , isMaximizing ):
        # self.game.draw()
        # print('depth ----- ' , depth , isMaximizing)

        result = self.checkWinner() ; 
        
        if (result ):
            return self.__scores[result]
        
        if isMaximizing:
            bestScore = -self.__infinity

            for i in range(3):
                for j in range(3):
                    #is the spot available
                    if self.game.board[i][j] == ' ':
                        self.game.board[i][j] = self.game.ai
                        score = self.minmax(depth + 1 , False)
                        self.game.board[i][j] = ' '
                        bestScore = max(score ,bestScore)


        else:
            bestScore = self.__infinity

            for i in range(3):
                for j in range(3):
                    #is the spot available
                    if self.game.board[i][j] == ' ':
                        self.game.board[i][j] = self.game.human
                        score = self.minmax(  depth + 1 , True)
                        self.game.board[i][j] = ' '
                        bestScore = min(score ,bestScore)

        return bestScore
    

    def playMove(self ):
        print('AI TURN  ...' , self.game.ai)
        time.sleep(2)

        bestScore = -self.__infinity
        bestMove = None 

        for i in range(3):
            for j in range(3):
                if self.game.board[i][j] == ' ' :
                    self.game.board[i][j]  = self.game.ai
                    score = self.minmax(   0 , False) 
                    self.game.board[i][j] = ' ' 

                    if(score > bestScore) :
                        print(bestScore , bestMove)
                        bestScore = score 
                        bestMove = (i,j)


        self.game.board[ bestMove[0] ][ bestMove[1] ] = self.game.ai