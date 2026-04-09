'''4. Hangman Lite

Concepts: loops, strings, conditionals

Pick a random word
Let the user guess letters
Show progress like:
_ a _ _ m a n

👉 Challenge:

Limit number of guesses
Track already guessed letters'''

# to use random.choice()*******************************
import random

if __name__ == '__main__':

    # list of possible words that can be picked
    words = ['apple', 'carrot', 'banana', 'celery', 'cheese', 'strawberry', 'blueberry' ]

    # keep track of the letters the user inputted
    letters_guessed = []

    # picking a random word*******************************
    word = random.choice(words)

    # let user know what program does
    print('Hangman')
    print('=======')
    print('You have 10 tries to guess the word')

    # loop through random word and display the amount of letters in the random word
    for char in word:
        # include end = ' ', so _ is all in the same line
        print('_', end = ' ')
    
    # to put 'Choose a letter:' on a new line
    print('')

    # for loop that stops at 10, since the user only has ten guesses
    for i in range(10):
        # to put a new line
        print(' ')
        # show user what they have already guessed so far
        print('These are the letters that you have guessed so far: {}'.format(letters_guessed))
        # get user's guess
        user_input = input('Choose a letter: ')
        # add user input into a list to keep track of the letters they have guessed
        letters_guessed.append(user_input)
        # loop through random word
        for char in word:
            # check if user guess is in the random word generated
            # do this by checking if current character in random word is in letters_guessed list,
            # which contains all the characters that the user has guessed
            if char in letters_guessed:
                # display character if character is in letters_guessed (user guessed correctly)
                print(char, end = ' ')
            else:
                # display _ if character is not in letters_guessed (user guessed incorrectly)
                print('_', end = ' ')
        # tp put a new line
        print(' ') 
        # check if all letters have been guessed*******************************
        # set all_guessed to True initially
        all_guessed = True
        # loop through random word
        for char in word:
            # if character not in letters_guessed, then user still needs to guess
            # user did not guess the character
            if char not in letters_guessed:
                all_guessed = False
                break
        # user guessed all the correct characters before all the attempts given
        if all_guessed:
            print('You guessed the word!')
            break