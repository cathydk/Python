'''3. Password Strength Checker

Concepts: strings, conditionals

Ask the user for a password and check if it:

Is at least 8 characters
Contains a number
Contains a special character

👉 Output: "Strong" or "Weak"

👉 Challenge: Give specific feedback (e.g., “missing number”)'''

if __name__ == '__main__':

    # to check if password has number and special character
    has_num = False
    has_special = False
    special_chars = '!@#$%^&*()-_+=`~:;<>?'
    
    # let user know what the program does
    print('Password Strength Checker')

    # get user input
    user_input = input('Please enter in a password and I will let you know if it is strong or weak: ')

    # check if password contains a number and contains a special character
    # loop through the password and check to see if password has numbers and special characters
    for char in user_input:
        # checks if password has numbers
        # .isdigit() method checks if character is a number
        if char.isdigit():
            has_num = True
        # checks if password has special characters
        # checking char with the string special_chars
        if char in special_chars:
            has_special = True
        # don't need to loop any further since number and special char was found, so break 
        if has_num == True and has_special == True:
            break

    # check how long the user input is
    input_size = len(user_input)

    # let user know what is missing in password
    if input_size >= 8 and has_num == True and has_special == True:
        print('Strong')
    else:
        print('Weak')
    if input_size < 8:
        print('Password is shorter than 8 characters')
    if has_num == False:
        print('Missing number')
    if has_special == False:
        print('Missing special character')