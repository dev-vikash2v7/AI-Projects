class HumanPlayer:
    count = 0 
    def __init__(self , name , game) -> None:
        self.game = game 
        self.name  = name 

        HumanPlayer.count += 1 

    def __str__(self):
        return  self.name
    
    def playMove(self  ):
        valid_move = False 

        while not valid_move:
                try:
                  position = int(input("{} turn - play move '{}' : ".format(self.name , self.game.player)))

                  if  not self.game.isValidMove(position):
                    raise IndexError
                  
                  valid_move = True

                except ValueError:
                    print('[WARNING] enter numeric value from 0-8 ')

                except IndexError:
                         print('[WARNING] index provided is not valid ')
                except Exception as e:
                    print('[error] : ' , e)


        self.game.board[position//3 ][position%3] = self.game.player
