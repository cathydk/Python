'''1. Palindrome Checker

Concepts: strings, conditionals

Write a program that:

Takes a word as input
Checks if it reads the same forward and backward

👉 Example:

"racecar" → palindrome
"hello" → not a palindrome

👉 Challenge:
Ignore spaces and capitalization ("Race car" should count)'''

if __name__ == '__main__':

    # creating empty string
    # read user input backwards
    # and store into this variable
    string_backwards = ''

    # let the user know what the program does
    print('Enter in a string and I will let you know if it is a palindrome string')

    # get user input
    user_input = input('Please enter in a string: ')

    # convert user string to all lowercases
    user_input_lowercase = user_input.lower()

    # remove the spaces for the user input
    lowercase_no_space = user_input_lowercase.replace(' ','')

    # looping through the user input backwards, starting from the end of user input
    for chars in reversed(lowercase_no_space):
        # reading each character one by one and storing it in string_backwards
        string_backwards = string_backwards + chars

    # check if string_backwards matches user input
    if string_backwards == lowercase_no_space:
        # if it matches then user input is a palindrome
        print('The string you entered is a palindrome')
    else:
        # if it doesnt match then user input is not a palindrome
        print('The string you entered is not a palidrome')