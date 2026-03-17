'''1. Even or Odd Checker

Concepts: conditionals, user input
Write a program that:

Takes a number as input

Prints whether it’s even or odd

👉 Challenge: Handle invalid input (like letters instead of numbers)'''

if __name__ == '__main__':
    
    # variable to exit loop
    # variable to check if input is an integer
    is_valid_input = False
    
    # will keep asking for user input until a valid input is given
    while is_valid_input == False:
        # asking for user input
        # input will be read as a string
        user_input_string = input('Enter a number: ')
        
        # handling invalid input
        try:
            # try to convert string to int if possible
            # if can't convert string to int then program will jump to except ValueError
            user_input_int = int(user_input_string)
            # checking to see if user input is odd or even
            if user_input_int%2 == 0:
                print('You entered an even number!')
            else:
                print('You entered an odd number!')
            is_valid_input = True
        # user did not input an integer value
        except ValueError:
            print('You did not enter a number, try again')