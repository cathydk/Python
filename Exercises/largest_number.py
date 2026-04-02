'''4. Find the Largest Number in a List

Concepts: lists, loops

Ask the user to input several numbers (comma-separated)
Find and print the largest number

👉 Challenge: Do it without using max()'''

if __name__ == '__main__':

    # let user know what the program does
    print('Largest Number Finder')

    # get user input
    user_input = input('Input several numbers (comma-separated); EX. 3,6,36,2,8 : ')
    print(user_input)
    
    # convert user input string to list of strings
    # using the .split() method to separate each number the user inputs
    # the method will separate each number once it encounters a ','
    # user_list is a list of strings****************************
    user_list = user_input.split(',')
    print(user_list)

    # organize list from min to max
    # sorted() function returns a copy of a list in order from smallest to largest
    # original list is unchanged
    # before we use the sorted() function we have to convert the strings to ints****************************
    # looping through user_list and converting string to int and storing in int_user_list
    int_user_list = []
    for i in user_list:
        int_user_list.append(int(i))
    print(int_user_list)
    sorted_list = sorted(int_user_list)
    print(sorted_list)

    # give user the largest number that they inputted
    print('The largest number you inputted was {}'.format(sorted_list[-1]))