# Nate McCain
# April 8, 2017
# CS 424 Section 01 (Tuesday/Thursday Section)
# This program allows two players to play either Fifty or Pig. It first asks for the players' names, and then
# which game they would like to play. After a game is won or lost, the players are asked if they would like
# to play either Fifty or Pig, or if they wish to end the program (This loop continues until a player decides
# to quit). Any time a player chooses to quit, the program ends (with a call "sys.exit()").
# Python 3.5.1
# Object-Oriented Implementation

import random # Import the random.py library.
import sys # Import the sys.py library.

# Class to represent a single, six-sided die.
class die(object):
    # This method is to create an object instance of a die.
    # Its initial value is set to 1 to establish that value is of the integer type.
    # No parameters, and no return value.
    def __init__(self):
        self.value = 1

    # This mutator represents rolling a die.
    # It uses the random library to generate a random value between 1 and 6.
    # No parameters, and no return value.
    def rollDie(self):
        self.value = random.randint(1,6)

    # This accessor returns the current value of the die.
    # No parameters, and it only returns a copy of the die's value.
    def get_roll(self):
        result = int(self.value)
        return result
# End of class for a die.


# Class for a pair of dice that is only used for Fifty.
# This class inherits from the die class.
class dice(die):
    # This method creates two object instances of the die class.
    # The dice are initialized using the method written in the die class.
    # No parameters, and no return value.
    def __init__(self):
        self.one = die()
        self.two = die()

    # This mutator represents rolling the dice.
    # It calls to the die class method to roll each die.
    # No parameters, and no return value.
    def rollDice(self):
        self.one.rollDie()
        self.two.rollDie()

    # This accessor returns the points earned from rolling the dice.
    # No parameters. Returns an integer value.
    # Return "-1" if double 3's are rolled (to represent the score needing to be reset, "25" if double 6's
    # are rolled, and "5" if other doubles are rolled. Return '0' if no doubles are rolled.
    def return_result(self):
        oneResult = int(self.one.get_roll())
        twoResult = int(self.two.get_roll())
        
        # If doulbes are rolled
        if (oneResult == twoResult):
            # Double 3's
            if (oneResult == 3):
                print("You rolled double 3's. Your score is now zero.\n")
                return int(-1)
            
            # Double 6's
            elif (oneResult == 6):
                print("You rolled double 6's. You get 25 points.\n")
                return int(25)
            
            # Other doubles
            else:
                print("You rolled double ", oneResult, "'s. You get 5 points.\n")
                return int(5)
            
        # If doubles are not rolled.
        else:
            print("You rolled a ", oneResult, " and a ", twoResult, ". You get zero points.\n")
            return int(0)
# End of class for a pair of dice.


# Class for a player instance.
class player(object):
    # Initialize an instance of a player object.
    # The player's name is passed as a parameter, and their score is initialized to 0. No return value.
    def __init__(self, name):
        self.name = name
        self.score = 0
        
    # Mutator that changes a player's name (I don't use this in the program, but I figured it was good practice to write).
    # It takes in the name desired (only parameter), and sets it as the player's name.
    # No return value.
    def change_name(self, newName):
        self.name = newName
        
    # Mutator that changes a player's score.
    # It takes in the player's updated score, and sets it as the player's current score.
    # No return value.
    def change_score(self, newScore):
        self.score = newScore
        
    # Accessor that returns a copy of the player's name.
    # No parameters.
    def get_name(self):
        playerName = str(self.name)
        return playerName
    
    # Accessor that returns a copy of the player's score.
    # No parameters.
    def get_score(self):
        playerScore = int(self.score)
        return playerScore
# End of player class.


# Class for the game of Pig. This class composes an instance of two players, and one die.
class pig(object):
    # Initialization for an instance of the game of Pig. It composes two players, a die, and the score needed to win the game.
    # Parameters are the two players' names and the score needed to win the game.
    # No return values.
    def __init__(self, playerOneName, playerTwoName, winningScore):
        self.winningScore = winningScore
        self.pOne = player(str(playerOneName))
        self.pTwo = player(str(playerTwoName))
        self.cube = die()

    # This function acts as a roll for player one. It rolls the die, grabs a copy of the player's score,
    # and then changes the player's score according to the roll result.
    # No parameters, and no return value.
    def player_one_roll(self):
        print("Rolling the die for " + str(self.pOne.get_name()) + "\n")
        
        self.cube.rollDie()
        value = int(self.cube.get_roll()) # Copy of the die's roll result.
        score = int(self.pOne.get_score()) # Copy of the player's score.
        
        # If the player got really unlucky.
        if (value == 1 and score == 0):
            print(str(self.pOne.get_name()) + ", you rolled a 1 while your score was 0.")
            self.pOne.change_score(-1) # A player's score is reported as "-1" if they have lost the game.
            print(str(self.pOne.get_name()) + " has lost.\n")
            print(str(self.pTwo.get_name()) + ", you win the game with a score of ", int(self.pTwo.get_score()), " points.\n")
            return
        
        # If the player only has to reset their score due to rolling a 1.
        elif (value == 1 and score != 0):
            print(str(self.pOne.get_name()) + ", you rolled a 1, your score is now 0.\n")
            self.pOne.change_score(0)
            return
        
        # The player did not roll a 1.
        else:
            print(str(self.pOne.get_name()) + ", you rolled a ", int(value), ".\n")
            self.pOne.change_score(int(score + value))
            print("Your score is now ", int(self.pOne.get_score()), ".\n")
            return
        
    # End of function that rolls the die for player one.

    # This function acts as a roll for player two. It rolls the die, grabs a copy of the player's score,
    # and then changes the player's score according to the roll result.
    # No parameters, and no return value.
    def player_two_roll(self):
        print("Rolling the die for " + str(self.pTwo.get_name()) + "\n")
        
        self.cube.rollDie()
        value = int(self.cube.get_roll()) # Copy of the die's roll result.
        score = int(self.pTwo.get_score()) # Copy of the player's score.

        # If the player got really unlucky.
        if (value == 1 and score == 0):
            print(str(self.pTwo.get_name()) + ", you rolled a 1 while your score was 0.\n")
            self.pTwo.change_score(-1) # A player's score is reported as "-1" if they have lost the game.
            print(str(self.pTwo.get_name()) + " has lost.\n")
            print(str(self.pOne.get_name()) + ", you win the game with a score of ", int(self.pOne.get_score()), " points.\n")
            return

        # If the player only has to reset their score due to rolling a 1.
        elif (value == 1 and score != 0):
            print(str(self.pTwo.get_name()) + ", you rolled a 1, your score is now 0.\n")
            self.pTwo.change_score(0)
            return

        # The player did not roll a 1.
        else:
            print(str(self.pTwo.get_name()) + ", you rolled a ", int(value), ".\n")
            self.pTwo.change_score(int(score + value))
            print("Your score is now ", int(self.pTwo.get_score()), ".\n")
            return
    # End of function that rolls the die for player two.

    # Function that returns whether a player rolled a one, used by both players.
    # It has no parameters, and returns True if a 1 was rolled, False if not.
    def did_player_roll_a_one(self):
        if (int(self.cube.get_roll()) == 1):
            return True
        else:
            return False
    # End of function that returns whether a player rolled a one.

    # Function that returns whether player one has won the game.
    # It has no parameters, and returns True if player one's score is equal or greater to the score needed to win, false if not.
    def has_player_one_won(self):
        score = int(self.pOne.get_score())
        if (score >= int(self.winningScore)):
            return True
        else:
            return False
    # End of function that returns whether player one has won.
    
    # Function that returns whether player two has won the game.
    # It has no parameters, and returns True if player two's score is equal or greater to the score needed to win, false if not.
    def has_player_two_won(self):
        score = int(self.pTwo.get_score())
        if (score >= int(self.winningScore)):
            return True
        else:
            return False
    # End of function that returns whether player two has won.
    
    # Function that returns whether player one has lost the game.
    # It has no parameters, and returns True if player one's score == -1, False if not.
    def has_player_one_lost(self):
        score = int(self.pOne.get_score())
        if (score == int(-1)):
            return True
        else:
            return False
    # End of function that returns whether player one has lost the game.
    
    # Function that returns whether player two has lost the game.
    # It has no parameters, and returns True if player two's score == -1, False if not.
    def has_player_two_lost(self):
        score = int(self.pTwo.get_score())
        if (score == int(-1)):
            return True
        else:
            return False
    # End of function that returns whether player two has lost the game.

    # Function that asks a player one if they wish to continue rolling, end their turn, or quit the program.
    # No parameters, returns True if the player wants to roll again, False if not. Makes a sys.exit() call if
    # the player chooses to quit the program.
    def player_one_keep_rolling(self):
        decision = False
        while (decision == False):
            print("\n" + str(self.pOne.get_name()) + ", would you like to keep rolling?\n")
            print("You have ", int(self.pOne.get_score()), " points.\n")
            print("Enter 'r' to keep rolling, 'e' to end your turn, or 'q' to quit the program.\n")
            userInput = input()
            # Player one wants to keep rolling.
            if (userInput == 'r'):
                return True
            # Player one wants to end their turn.
            elif (userInput == 'e'):
                print("\n")
                return False
            # Player one wants to quit the program.
            elif (userInput == 'q'):
                print("Ending the program. " + str(self.pOne.get_name()) + " is a disgraceful quitter.\n")
                sys.exit()
            # Invalid input
            else:
                print("Please follow the instructions. \n")
    # End of function that asks player one if they want to keep rolling.

    # Function that asks a player two if they wish to continue rolling, end their turn, or quit the program.
    # No parameters, returns True if the player wants to roll again, False if not. Makes a sys.exit() call if
    # the player chooses to quit the program.
    def player_two_keep_rolling(self):
        decision = False
        while (decision == False):
            print("\n" + str(self.pTwo.get_name()) + ", would you like to keep rolling?\n")
            print("You have ", int(self.pTwo.get_score()), " points.\n")
            print("Enter 'r' to keep rolling, 'e' to end your turn, or 'q' to quit the program.\n")
            userInput = input()
            # Player two wants to keep rolling.
            if (userInput == 'r'):
                return True
            # Player two wants to end their turn.
            elif (userInput == 'e'):
                print("\n")
                return False
            # Player two wants to quit the program.
            elif (userInput == 'q'):
                print("Ending the program. " + str(self.pTwo.get_name()) + " is a disgraceful quitter.\n")
                sys.exit()
            # Invalid input
            else:
                print("Please follow the instructions.")
    # End of function that asks player two if they want to keep rolling.

    # Function that acts as a turn for player one.
    # No parameters, returns '1' if player one has won, "-1" if player one has lost, and '0' if the player has not won or lost.
    def player_one_turn(self):
        decision = False
        # This acts as the first part of a turn, as a player cannot choose to end a turn without rolling the die.
        while (decision == False):
            print(str(self.pOne.get_name()) + ", it is your turn.\n")
            print("Enter 'r' to roll, or 'q' to quit the program.\n")
            userInput = input()
            # Player one wants to roll the die.
            if (userInput == 'r'):
                print("\n")
                decision = True
            # Player one wants to quit the program.
            elif (userInput == 'q'):
                print("Ending the program. " + str(self.pOne.get_name()) + " is a disgraceful quitter.\n")
                sys.exit()
            # Incorrect input
            else:
                print("Please follow the instructions.\n")
                
        # If the player did not quit, execute the first roll.
        self.player_one_roll()
        winner = bool(self.has_player_one_won()) # Has player one won the game?
        # If player one has won the game
        if (winner == True):
            return int(1)
        loser = bool(self.has_player_one_lost()) # Has player one lost the game?
        # If player one has lost the game
        if (loser == True):
            return int(-1)
        
        # This loops after a player's first roll. The loop is exited if a player wins or loses the game, or if they choose to end their turn.
        keepGoing = bool(self.player_one_keep_rolling())
        
        while (keepGoing == True):
            self.player_one_roll()
            winner = bool(self.has_player_one_won()) # Has player one won the game?
            loser = bool(self.has_player_one_lost()) # Has player one lost the game?
            rolled_a_one = bool(self.did_player_roll_a_one()) # Did player one roll a one, meaning their turn is over?
            # If player one has won the game
            if (winner == True):
                return int(1)
            # If player one has lost the game
            elif (loser == True):
                return int(-1)
            # If player one rolled a one
            elif (rolled_a_one == True):
                return int(0)
            # Player one can keep rolling as they have not won, lost, or rolled a 1.
            else:
                keepGoing = bool(self.player_one_keep_rolling())
        # End of while loop.
        
        return int(0) # Returning 0 tells the calling function that the game is not yet over.
    # End of function that acts as a turn for player one.
    
    # Function that acts as a turn for player two.
    # No parameters, returns '1' if player two has won, "-1" if player two has lost, and '0' if the player has not won or lost.
    def player_two_turn(self):
        decision = False
        # This acts as the start of player two's turn, as the player cannot end a turn without rolling the die.
        while (decision == False):
            print(str(self.pTwo.get_name()) + ", it is your turn.\n")
            print("Enter 'r' to roll, or 'q' to quit the program.\n")
            userInput = input()
            # Player two wants to roll the die.
            if (userInput == 'r'):
                print("\n")
                decision = True
            # Player two wants to end the program.
            elif (userInput == 'q'):
                print("Ending the program. " + str(self.pTwo.get_name()) + " is a disgraceful quitter.\n")
                sys.exit()
            # Incorrect input
            else:
                print("Please follow the instructions.\n")
                
        # If the player did not quit, execute the first roll.
        self.player_two_roll()
        winner = bool(self.has_player_two_won()) # Has player two won the game?
        # If player two has won the game
        if (winner == True):
            return int(1)
        loser = bool(self.has_player_two_lost()) # Has player two lost the game?
        # If player two has lost the game
        if (loser == True):
            return int(-1)
        
        # This loops after a player's first roll. The loop is exited if the player chooses to end their turn, wins, or loses.
        keepGoing = bool(self.player_two_keep_rolling())
        
        while (keepGoing == True):
            self.player_two_roll()
            winner = bool(self.has_player_two_won()) # Has player two won the game?
            loser = bool(self.has_player_two_lost()) # Has player two lost the game?
            rolled_a_one = bool(self.did_player_roll_a_one()) # Did player two roll a 1, thus ending their turn?
            # If player two has won the game
            if (winner == True):
                return int(1)
            # If player two has lost the game
            elif (loser == True):
                return int(-1)
            # If player two rolled a 1
            elif (rolled_a_one == True):
                return int(0)
            # Player two can keep rolling, as they have not won or lost the game, or rolled a 1.
            else:
                keepGoing = bool(self.player_two_keep_rolling())
        # End of while loop.
        
        return int(0) # Returning 0 tells the calling function that the game is not yet over.
    # End of function that acts as a turn for player one.

    # Function that outputs a message declaring player one as the winner.
    # No parameters, and no return values.
    def declare_player_one_winner(self):
        print(str(self.pOne.get_name()) + " is the winner with ", int(self.pOne.get_score()), " points.\n")
        return
    # End of function that outputs a message declaring player one as the winner.

    # Function that outputs a message declaring player two as the winner.
    # No parameters, and no return values.
    def declare_player_two_winner(self):
        print(str(self.pTwo.get_name()) + " is the winner with ", int(self.pTwo.get_score()), " points.\n")
        return
    # End of function that outputs a message declaring player two as the winner.

    # Function that controlls the entire game of pig.
    # It calls all of the above functions in an order that simulates the entire game.
    # No parameters, and no return values.
    def lets_play_pig(self):
        # Makes sure that both players' have a score of zero before starting the game.
        self.pOne.change_score(0)
        self.pTwo.change_score(0)
        
        gameState = int(0) # When gameState is 0, the game can still continue.
        while (gameState == 0):
            # Start player one's turn
            gameState = int(self.player_one_turn())
            # If player one ended the game (by winning or losing), print the appropriate message and return to the calling function.
            if (gameState != 0):
                # If player one has won the game
                if (gameState == 1):
                    self.declare_player_one_winner()
                    return
                # If player one has lost the game
                else:
                    self.declare_player_two_winner()
                    return

            # Start player two's turn
            gameState = int(self.player_two_turn())
            # If player two has ended the game (by winning or losing), print the appropriate message and return to the calling function.
            if (gameState != 0):
                # If player two has won the game
                if (gameState == 1):
                    self.declare_player_two_winner()
                    return
                # If player two has lost the game
                else:
                    self.declare_player_one_winner()
                    return
        # End of while loop that holds the game. It keeps looping as long as the game is not over.
        
        return # Returns to the calling function. This isn't really needed, I just put it here out of habit.
    
    # End of function that controlls the entire game of pig.
# End of Pig class.



# Class for the game of Fifty. This class composes an instance of two players, and an instance of dice.
class fifty(object):
    # Initialization for an instance of the game of Fifty. It composes two players, one set of dice, and the score needed to win the game.
    # Parameters are the two players' names and the score needed to win the game.
    # No return values.
    def __init__(self, playerOneName, playerTwoName, winningScore):
        self.winningScore = winningScore
        self.pOne = player(str(playerOneName))
        self.pTwo = player(str(playerTwoName))
        self.cube = dice()

    # Function that rolls the dice for player one, and updates the player's score according to the roll result.
    # No parameters or return values.
    def player_one_roll(self):
        self.cube.rollDice()
        result = int(self.cube.return_result()) # Get the result of the roll from the dice class, which is made to only support this game.
        score = int(self.pOne.get_score()) # Get a copy of the player's score.
        
        # If player one's score must be reset to 0
        if (result == -1):
            self.pOne.change_score(0)
        # If player one earned 25 points from the roll
        elif (result == 25):
            self.pOne.change_score(score + result)
        # If player one earned 5 points from the roll
        elif (result == 5):
            self.pOne.change_score(score + result)
        # If a player earned 0 points, don't do anything.
        
        return # Return to the calling function.
    # End of function that rolls the dice for player one.

    # Function that rolls the dice for player two, and updates the player's score according to the roll result.
    # No parameters or return values.
    def player_two_roll(self):
        self.cube.rollDice()
        result = int(self.cube.return_result()) # Get the result of the roll from the dice class, which is made to only support this game.
        score = int(self.pTwo.get_score()) # Get a copy of the player's score.

        # If player two's score must be reset to 0
        if (result == -1):
            self.pTwo.change_score(0)
        # If player two earned 25 points from the roll
        elif (result == 25):
            self.pTwo.change_score(score + result)
        # If player two earned 5 points from the roll
        elif (result == 5):
            self.pTwo.change_score(score + result)
        # If player two earned 0 points, don't do anything.
        
        return # Return to the calling function.
    # End of function that rolls the dice for player two, and updates the player's score.

    # Function that compares player one's score to the score needed to win the game.
    # No parameters, returns True if player one has won, False if not.
    def has_player_one_won(self):
        if (int(self.pOne.get_score()) >= int(self.winningScore)):
            return True
        else:
            return False
    # End of function that returns whether player one has won the game.

    # Function that compares player two's score to the score needed to win the game.
    # No parameters, returns True if player two has won, False if not.
    def has_player_two_won(self):
        if (int(self.pTwo.get_score()) >= int(self.winningScore)):
            return True
        else:
            return False
    # End of function that returns whether player two has won the game.

    # Function that asks player one if they would like to roll the dice or quit the program.
    # No parameters, no return values.
    # If the player chooses to roll, the function returns to the caller. If the player chooses to quit
    # the program, sys.exit() is called.
    def ask_player_one_roll_or_quit(self):
        decision = False
        print(str(self.pOne.get_name()) + ", it is your turn.\n")
        print("You have ", int(self.pOne.get_score()), " points.\n")
        while (decision == False):
            print("Enter 'r' to roll, or 'q' to quit the program.\n")
            userInput = input()
            # If player one wishes to roll the dice
            if (userInput == 'r'):
                print(str(self.pOne.get_name()) + " chooses to roll.\n")
                decision = True
            # If player one wishes to quit the program.
            elif (userInput == 'q'):
                print("Ending the program. " + str(self.pOne.get_name()) + " is a disgraceful quitter.\n")
                sys.exit()
            # Incorrect input
            else:
                print("Please follow the instructions.\n")
        # End of while loop.
        
        return # Returns to the calling function.
    # End of function that only returns if player one wants to roll, exits if they choose to quit.

    # Function that asks player two if they would like to roll the dice or quit the program.
    # No parameters, no return values.
    # If the player chooses to roll, the function returns to the caller. If the player chooses to quit
    # the program, sys.exit() is called.
    def ask_player_two_roll_or_quit(self):
        decision = False
        print(str(self.pTwo.get_name()) + ", it is your turn.\n")
        print("You have ", int(self.pTwo.get_score()), " points.\n")
        while (decision == False):
            print("Enter 'r' to roll, or 'q' to quit the program.\n")
            userInput = input()
            # If player two wishes to roll the dice
            if (userInput == 'r'):
                print(str(self.pTwo.get_name()) + " chooses to roll.\n")
                decision = True
            # If player two wishes to quit the program
            elif (userInput == 'q'):
                print("Ending the program. " + str(self.pTwo.get_name()) + " is a disgraceful quitter.\n")
                sys.exit()
            # Incorrect input
            else:
                print("Please follow the instructions.\n")
        # End of while loop
        
        return # Returns to the calling function.
    # End of function that only returns if player two wants to roll, exits if they choose to quit.

    # Function that contains player one's turn.
    # No parameters, no return values.
    def player_one_turn(self):
        self.ask_player_one_roll_or_quit() # Ask to roll or quit.
        self.player_one_roll() # Execute a roll.
        return
    # End of function that contains player one's turn.

    # Function that contains player two's turn.
    # No parameters, no return values.
    def player_two_turn(self):
        self.ask_player_two_roll_or_quit() # Ask to roll or quit.
        self.player_two_roll() # Execute a roll.
        return
    # End of function that contains player two's turn.

    # Function that declares player one as the winner.
    # No parameters, no return values.
    def declare_player_one_winner(self):
        print(str(self.pOne.get_name()) + "wins with a score of ", int(self.pOne.get_score()), " points.\n")
        return
    # End of function that declares player one as the winner.

    # Function that declares player two as the winner.
    # No parameters, no return values.
    def declare_player_two_winner(self):
        print(str(self.pTwo.get_name()) + "wins with a score of ", int(self.pTwo.get_score()), " points.\n")
        return
    # End of function that declares player two as the winner.

    # Function that controlls the entire game of fifty.
    # It calls all of the above functions in an order that simulates the entire game.
    # No parameters, and no return values.
    def lets_play_fifty(self):
        # Makes sure that both players' have a score of zero before starting the game.
        self.pOne.change_score(0)
        self.pTwo.change_score(0)
        
        gameOver = False 
        while (gameOver == False):
            # Start player one's turn
            self.player_one_turn()
            gameOver = bool(self.has_player_one_won()) # Has player one won the game?
            # If player one has won the game
            if (gameOver == True):
                self.declare_player_one_winner()
                return

            # Start player two's turn
            self.player_two_turn()
            gameOver = bool(self.has_player_two_won()) # Has player two won the game?
            # If player two has won the game
            if (gameOver == True):
                self.declare_player_two_winner()
                return
        # End of while loop that continues if the game has not ended.
        
        return # Return to the calling function.
    
    # End of function that controlls the entire game of fifty.
# End of fifty class.


# Class that holds an instance of both games. This class acts as the controller for the entire project.
class projectOne(object):
    # Initialization for an instance of Pig and an instance of Fifty.
    # Parameters are the two players' names.
    # No return values.
    def __init__(self, playerOneName, playerTwoName):
        self.pigGame = pig(playerOneName, playerTwoName, 100)
        self.fiftyGame = fifty(playerOneName, playerTwoName, 50)

    # This function prints the instructions for playing Fifty.
    # No parameters, no return values.
    def print_instructions_for_fifty(self):
        print("Here are the instructions for Fifty.")
        print("Goal:")
        print("The goal of Fifty is to be the first player to reach 50 points. You get points by rolling doubles.")
        print("Play:")
        print("A turn consists of a player rolling a pair of dice (with the goal of rolling doubles), and scoring")
        print("the roll as described below. Play continues with each player taking one roll per turn. The first")
        print("player to score 50 or more points is declared the winner.")
        print("Scoring:")
        print("All doubles except 3's and 6's score 5 points. Double 6's are worth 25 points. Double 3's wipe")
        print("out the player's entire score, and the player must start again at 0. Non-double rolls are 0 points. \n")
        return
    # End of function that prints the instructions for playing Fifty.

    # This function prints the instructions for playing Pig.
    # No parameters, no return values.
    def print_instructions_for_pig(self):
        print("Here are the instructions for Pig.")
        print("Goal:")
        print("The goal of Pig is to be the first player to reach 100 points. You get points by rolling a single die")
        print("multiple times and adding the value on each roll of the die to your current score.")
        print("Play:")
        print("The first player rolls the die as many times as they want. The value of each throw is added onto")
        print("the score until the player decides to end his/her turn and passes the die to the next player. Play")
        print("continues until one player reaches 100.")
        print("Scoring:")
        print("The value of each throw is added to the current player's score. If the player rolls a 1, the player's")
        print("score goes back to 0, and their turn ends.")
        print("At one extreme, any player who gets a 1 on the first roll is immediately out. At the other extreme,")
        print("the first player could theoretically reach the winning score on the first turn, as long as they don't")
        print("roll a 1. If the player succeeds, the game ends there. \n")
        return
    # End of function that prints the instructions on how to play Pig.
    
    # Function that controlls the entire project. It asks what game the players wish to play, and executes according
    # to their answer.
    # No parameters, no return values.
    def project_one_controller(self):
        self.print_instructions_for_fifty()
        self.print_instructions_for_pig()
        
        infiniteLoop = True # Just keep looping until a player calls for the program to quit.
        while (infiniteLoop == True):
            print("Enter 'f' to play Fifty, 'p' to play Pig, or 'q' to quit the program.\n")
            userInput = input()
            # If the players pick to play Fifty
            if (userInput == 'f'):
                print("Please allow me to remind you of the rules for Fifty.\n")
                self.print_instructions_for_fifty()
                self.fiftyGame.lets_play_fifty()
            # If the players pick to play Pig
            elif (userInput == 'p'):
                print("Please allow me to remind you of the rules for Pig. \n")
                self.print_instructions_for_pig()
                self.pigGame.lets_play_pig()
            # If the players pick to end the program
            elif (userInput == 'q'):
                print("Goodbye")
                sys.exit()
            # Incorrect input
            else:
                print("Please follow the instructions.\n")
            
    # End of function that acts as the project's controller.
# End of project one class.

# This function acts as the program driver. It asks for the players' names, and creates an instance of the
# project class. The project instance is then calls to the project controller, and the program runs accordingly.
def main():
    print("Welcome to the boardgame collection! This program allows users to play either Fifty or Pig.\n")
    print("If at any point a player chooses to quit, the program will end. \n")
    print("Player one, please input your name and press enter.")
    pOneName = input()
    print("\nPlayer two, please input your name and press enter.")
    pTwoName = input()
    print("\n")
    myProject = projectOne(pOneName, pTwoName)
    myProject.project_one_controller()
    return
# End of driver function.

main() # Tells IDLE to call the driver function.
