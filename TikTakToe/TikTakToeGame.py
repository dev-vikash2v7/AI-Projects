class TikTakToeGame:

    def __init__(self ) -> None:
       self.board =[ [' ' , ' ' , ' '] * 3]
       self.player = 'X' 
       self.__total_moves = 0  
       self.ai = 'X'
       self.human = 'O'
 
    def isValidMove( self , pos):
        if  0 <= pos < 9 and self.board[pos//3 ][pos%3] == ' ':
            return True
        return False
     

    def draw(self):
        for i in range(3):
         for j in range(3):
            print(self.board[i][j] , end='|')
         print()
         print("-+" * 3)
 

    def is_win(self ):
        player = self.player

        if (self.board[0][0] == player and self.board[0][1] == player and self.board[0][2] == player or \
        self.board[1][0] == player and self.board[1][1] == player and self.board[1][2] == player or \
        self.board[2][0] == player and self.board[2][1] == player and self.board[2][2] == player) or \
        (self.board[0][0] == player and self.board[1][0] == player and self.board[2][0] == player or \
        self.board[0][1] == player and self.board[1][1] == player and self.board[2][1] == player or \
        self.board[0][2] == player and self.board[1][2] == player and self.board[2][2] == player) or \
        (self.board[0][0] == player and self.board[1][1] == player and self.board[2][2] == player or \
        self.board[0][2] == player and self.board[1][1] == player and self.board[2][0] == player) :
            return True
        return False
    
    def is_draw(self):
        return self.__total_moves == 9
             

    def change_turn(self):
        self.__total_moves += 1
        self.player = "O" if self.player == 'X' else 'X'

