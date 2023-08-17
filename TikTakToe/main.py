from  TikTakToeGame import TikTakToeGame as Game
from  HumanPlayer import HumanPlayer 
from  AIPlayer import AIPlayer 


if __name__== '__main__':
   game = Game()

   p1 = HumanPlayer('AI' , game)
   p2 = HumanPlayer('vikas' , game)


   while not game.is_draw():
            game.draw()

            current_player = p1 if game.player == 'X' else p2

            current_player.playMove()

            if game.is_win():
                game.draw()
                print("{} is the Winner!".format(current_player))
                break
            else:
                game.change_turn()
   else:
        print("Game over! It's a tie!")

   
