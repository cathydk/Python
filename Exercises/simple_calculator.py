'''2. Simple Calculator

Concepts: functions, conditionals
Create a calculator that:

Takes two numbers and an operator (+, -, *, /)

Returns the result

👉 Challenge: Prevent division by zero'''

# x int
# y int
# operator string
def calculate(x,y, operator):
    # adding
    if operator == '+':
        return x+y
    # subtracting
    elif operator == '-':
        return x-y
    # multiplying
    elif operator == '*':
        return x*y
    # dividing
    elif operator == '/':
        try:
            return x/y
        # dividing by 0
        except:
            print('Denominator can\'t be 0')
            return 'undefined'
    # invalid operator detected
    else:
        print('invalid operator input')
        return 'invalid operator input'

if __name__ == '__main__':
    
    # lets the user know what the program does
    print('I will ask you for two numbers and an operator, I will then perform the calculation')
    
    # asking for first number
    # convert string to int
    x_input = int(input('Please enter a number: '))
    # asking for second number
    # convert string to int
    y_input = int(input('Please enter another number: '))
    # asking for operator
    operator_input = input('Please enter an operator (+, -, *, /): ')
    
    # calling calculate function, user input are the parameters
    calculation = calculate(x_input,y_input,operator_input)
    
    # displaying output
    print('{}{}{}={}'.format(x_input,operator_input,y_input,calculation))