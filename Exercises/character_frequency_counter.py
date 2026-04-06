'''1. Character Frequency Counter (Dictionary) ⭐

Concepts: dictionaries, strings, loops

Write a program that:

Takes a string input
Counts how many times each character appears

👉 Example:

Input: "hello"
Output: {'h': 1, 'e': 1, 'l': 2, 'o': 1}

👉 Hints:

Use a dictionary to store counts
Check: “Have I seen this character before?”

👉 Challenge: Ignore spaces and make it case-insensitive'''

if __name__ == '__main__':

    # dictionary to hold frequency of characters
    frequency = {}

    # let user know what program does
    print('Character Frequency Counter')

    # get user input
    user_input = input('Please enter in a string: ')

    # remove spaces from user input
    no_space_input = user_input.replace(' ', '')

    # loop through user input string
    for char in no_space_input:
        # checks if current character is in the dictionary or not
        # if the currenct character isn't in the dictionary then add it to the dictionary with frequency of 1
        if char not in frequency:
            # key = char
            # value = 1
            frequency[char] = 1
        # if the current character is in the dictionary then add 1 to the frequecy
        else:
            frequency[char] += 1
    
    # display dictionary
    print(frequency)