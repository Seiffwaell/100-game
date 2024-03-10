# File : CS112_A1_T2_1_20230187
# Purpose : Two players start from 0 and alternatively add a number from 1 to 10 to the sum and the player who reaches 100 wins.
# Author : Seif Wael Naem
# ID : 20230187

def main():
    while True:  # This loop will keep the game running until the players decide to exit
        current_number=0 # The initial number we will start with

        print("Welcome to the 100 game") # Welcoming message to the game 
        print()

        while current_number < 100: # While the current_number is still less than 100 so continue the game
            win = 0
            valid = 0
            while valid != 1:
                try:
                    play =  int(input("Player 1: Please choose a number from 1 to 10: ")) # Taking a number from the 1st player
                    print()
                    while play < 1 or play > 10 or current_number + play > 100: # Making the boundary of the play from 1 to 10 and checking if the total exceeds 100
                        play =  int(input("Player 1: Invalid Number , Please choose a number from 1 to 10: ")) # This message appears in case of the player didn't choose number between 1 and 10
                        print()
                    current_number += play # This step adds the number which the player chose to the current_number
                    print(f'Now we have number {current_number}') # This message shows the sum of the numbers that we've reached 
                    print()
                    if current_number >= 100: # Here the program checks if the current_number reaches 100 or not 
                        print("***** PLAYER 1 WINS *****") # If it reaches the 100 so player 1 wins and the game ends
                        win = 1
                        break
                    valid = 1
                except ValueError :
                    print('Invalid input , please select a valid number ')

            if win == 1:
                break

            valid = 0

            while valid != 1:
                try:
                    play =  int(input("Player 2: Please choose a number from 1 to 10: ")) # If the game doesn't end so player 2 will choose a number
                    print()
                    while play < 1 or play > 10 or current_number + play > 100 :
                        play =  int(input("Player 2: Invalid number , Please choose a number from 1 to 10: "))  
                        print()
                    current_number += play
                    print(f'Now we have number {current_number}') 
                    print()   
                    if current_number >= 100:
                        print("***** PLAYER 2 WINS *****")
                        win = 1
                        break
                    valid = 1
                except ValueError:
                    print('Invalid input , please select a valid number ')

            if win == 1:
                break
        
        play_again = input("Do you want to play again? (yes/no): ")  # Ask the players if they want to play again
        if play_again.lower() != "yes":
            print()
            print('***** THANKS FOR PLAYING *****')
            break  # If the players do not want to play again, break the loop and end the game

main()

