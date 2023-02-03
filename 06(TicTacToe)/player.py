import random

class Player:
    def __init__(self,letter):
        #for letter X or O
        self.letter = letter
    
    def get_move(self,game): #next move based on the game
        pass

class Random_Comp_Player(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):   #a random move is played by the computer
        square = random.choice(game.available_moves())
        return square

class Human_Player(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_move = False
        value = None
        while not valid_move:
            square = input(f"{self.letter}'s turn. Input move(0-8)")
            
            #here we are trying to check the validity of our move by casting it to an intege0 otherwise invalidr
            #if the spot is empty then also the move is invalid

            try:
             value = int(square)
             if value not in game.available_moves():
                 raise ValueError
             valid_move = True
            except ValueError:
                print("Invalid input!!")
  
        return value 

