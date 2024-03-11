# File: CS112_A1_T2_Game 1_20230031.py
# Purpose: 100 Game. Two players start from 0 and alternatively add a number from 1 to 10 to the sum. The player who reaches 100 wins.
# Author: Ahmed Mohamed Ahmed
# ID: 20230031

# Welcome message and display game rules.
print('Welcome to 100 game.')
print('Two players start from 0 and alternatively add a number from 1 to 10 to the sum. The player who reaches 100 wins.')
print('Start Game.')

# Set number of coins.
n_coins = 0


# Game playing.
while n_coins < 100:
    # Switch between player 1 and player 2 Alternately.
    for player in range(1,3):
        while True:
            try:
                # If total coins is less than 91, The player can choose any number from 1 to 10 to reach 100 coins.
                if n_coins < 91:
                    # Get input from the player.
                    move = int(input('Player ' + str(player) + ' Please add number from 1 to 10: '))
                    # Check if the Integer is Not allowed.
                    while move < 1 or move > 10:
                        print('This Integer is Not allowed.')
                        move = int(input('Player ' + str(player) + ' Please add number from 1 to 10: '))
                    break
                # If total coins is between 90 and 99, The player can only choose numbers that lead to 100 coins.
                elif 90 < n_coins < 99:
                    # Get input from the player.
                    move = int(
                        input('Player ' + str(player) + ' Please add number from 1 to ' + str(100 - n_coins) + ': '))
                    # Check if the Integer is Not allowed.
                    while move < 1 or move > 100 - n_coins:
                        print('This Integer is Not allowed.')
                        move = int(input(
                            'Player ' + str(player) + ' Please add number from 1 to ' + str(100 - n_coins) + ': '))
                    break
                # If total coins = 99, The player must add 1 to reach 100 coins.
                else:
                    # Get input from the player.
                    move = int(input('Player ' + str(player) + ' Please add number 1: '))
                    # Check if the Integer is Not allowed.
                    while move != 1:
                        print('This Integer is Not allowed.')
                        move = int(input('Player ' + str(player) + ' Please add number 1: '))
                    break
            # Check if it is Not integer.
            except:
                print('This is Not Integer.')
                continue

        # Update total coins and display current count.
        n_coins += move
        print('Now we have '+str(n_coins)+'.')
        # Check if the current player is the winner.
        if n_coins == 100:
            print('Player '+str(player)+' is winner.')

            print('End Game.')
            break
