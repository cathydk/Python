'''1. Temperature Converter

Concepts: functions, math, user input

👉 Create two functions:
def celsius_to_fahrenheit(c):
def fahrenheit_to_celsius(f):

👉 Use formulas:
F = (C × 9/5) + 32  
C = (F − 32) × 5/9

👉 Example:
Input: 0°C → Output: 32°F
Input: 68°F → Output: 20°C

🔹 Hints:
Just return the calculated value
Don’t print inside the function (good practice)

🔹 Challenge:
Let the user choose which conversion to perform
Format output to 2 decimal places

Call your functions from main
Keep logic inside functions, not in if __name__ == '__main__' '''

# define function to convert celsius to fahrenheit
# c is being passed in
def celsius_to_fahrenheit(c):
    f = (c * (9/5)) + 32
    # return calculated value
    return f

# define function to convert fahrenheit to celsius
# f is being passed in
def fahrenheit_to_celsius(f):
    c = (f - 32) * (5/9)
    # return calculated value
    return c

# to call functions, display output, and get user input
def main():
    # display menu option
    print('1. Celsius -> Fahrenheit')
    print('2. Fahrenheit -> Celsius')

    # get user input on what they would like to do
    user_input = input('What would you like to do: ')

    # Celsius -> Fahrenheit
    if user_input == '1':
        # get user degree from user
        user_celsius = int(input('Enter in the Celsius degree: '))

        # calling celsius_to_fahrenheit(c) function
        # user_celsuis is being passed into the function
        # store returned value in c_to_f
        c_to_f = celsius_to_fahrenheit(user_celsius)

        # display output
        print('{}°C -> {}°F'.format(user_celsius, c_to_f))

    # Fahrenheit -> Celsius
    if user_input == '2':
        # get user degree from user
        user_fahrenheit = int(input('Enter in the Fahrenheit degree: '))

        # calling fahrenheit_to_celsius(f) function
        # user_fahrenheit is being passed into the function
        # store returned value in f_to_c
        f_to_c = fahrenheit_to_celsius(user_fahrenheit)

        # display output
        print('{}°F -> {}°C'.format(user_fahrenheit, f_to_c))

# only to call main()
if __name__ == '__main__':
    # calling main() function
    main()


'''
def celsius_to_fahrenheit(c):
    f = (c * (9/5)) + 32
    return f

def fahrenheit_to_celsius(f):
    c = (f - 32) * (5/9)
    return c

def main():
    print('1. Celsius -> Fahrenheit')
    print('2. Fahrenheit -> Celsius')

    user_input = input('What would you like to do: ')

    if user_input == '1':
        user_celsius = int(input('Enter in the Celsius degree: '))
        c_to_f = celsius_to_fahrenheit(user_celsius)
        print('{}°C -> {}°F'.format(user_celsius, c_to_f))
    if user_input == '2':
        user_fahrenheit = int(input('Enter in the Fahrenheit degree: '))
        f_to_c = fahrenheit_to_celsius(user_fahrenheit)
        print('{}°F -> {}°C'.format(user_fahrenheit, f_to_c))

if __name__ == '__main__':
    main()
'''