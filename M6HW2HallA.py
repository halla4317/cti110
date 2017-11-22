# Write a program that generates a random number in the range of 1 through 100
# 6 Nov 2017
# CTI-110 M6HW2-Random Number Guessing Game
# Hall, A

import random

# This command gives us the random numbers and also shows how many guesses the user gets

def main():

    guesses = 6
    guesses -= 1
    number = random.randint (1,100)
    win = False
    


# Main Function
    while guesses > 0:
        guess = int(input('Please....guess a number:'))

        if guess > number:
            print ('Your guess was too high, you have', guesses, 'left')
        elif guess < number:
            print ('Your guess was too low, you have', guesses, 'left')
        else:
            print ('Congrats, you guessed the correct number!')
            win = True
            guesses =0

        guesses -= 1

    if win == False:
        print('Sorry, you didnt guess the correct number. The number was', number)

    
        
            
main()    


