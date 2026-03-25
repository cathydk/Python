'''6. Multiplication Table Generator

Concepts: loops

Ask for a number
Print its multiplication table (e.g., up to 10)

👉 Challenge: Format it neatly like a grid'''

if __name__ == '__main__':
    
    # let user know what the program does
    print('Multiplication Table Generator')
    print('I will create a multiplication table based off of your input (up to 10)')
    
    # get user input
    user_input = input('Please enter a number: ')
    # convert string to int
    user_input_int = int(user_input)
    
    # loop through and calculate multiplication table
    # start = 1, stop = 11
    # stop at 11 to include 10
    for i in range(1, 11):
        # display multiplication table
        print('{} x {} = {}'.format(user_input_int, i, i * user_input_int))
        
    # grid format
    print('Here is the grid format for the multiplication table:')
    # i = row, j = column
    for i in range(1, 11):
        # stop at user_input_int+1 because we want to include user_input_int
        # stops at the number that the user inputed
        for j in range(1, user_input_int + 1):
            # i*j because row*column to get multiplication table
            # end = '', so that it prints row on the same line
            # '{:4}'.format(i * j) to format the grid so that the number aligns
            # 4 = total width
            # numbers will be right aligned automatically
            print('{:4}'.format(i * j), end = '')
        # prints a new line after finished with row
        print()