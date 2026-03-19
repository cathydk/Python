'''3. Number Guessing Game

Concepts: loops, random numbers

Generate a random number between 1–100

Let the user guess until they get it right

Give hints: “Too high” or “Too low”

👉 Challenge: Count how many attempts it takes'''

# import random module
import random

if __name__ == '__main__':
    
    # generating a random number between 1-100
    random_number = random.randint(1,100)
    
    # user did not guess the correct number yet
    is_correct = False
    # keep track of number of attempts guessed
    count = 0
    
    # keeps asking user to guess if the guess is incorrect
    while is_correct == False:
        # get user input
        user_input = int(input('Pick a number between 1-100: '))
        
        # user guessed the correct number
        if user_input == random_number:
            print('You guessed the correct number!')
            # add attempt to count
            count += 1
            # user guessed the correct number, set to True to exit loop
            is_correct = True
        # user guess was too low
        elif user_input < random_number:
            print('Your guess was too low')
            # add attempt to count
            count += 1
        # user guess was too high
        elif user_input > random_number:
            print('Your guess was too high')
            # add attempt to count
            count += 1
            
    # display how many tries the user attempted
    print('It took you {} tries to get the correct number!'.format(count))