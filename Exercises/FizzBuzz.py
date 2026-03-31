'''2. FizzBuzz

Concepts: loops, conditionals (classic interview question)

Print numbers from 1 to 50:

If divisible by 3 → print "Fizz"
If divisible by 5 → print "Buzz"
If divisible by both → print "FizzBuzz"

👉 Challenge: Let the user choose the range'''

if __name__ == '__main__':

    # let user know what the program does
    print('FizzBuzz')
    print('If divisible by 3 → print "Fizz"')
    print('If divisible by 5 → print "Buzz"')
    print('If divisible by both → print "FizzBuzz"')

    # letting the user choose the range
    # convert user input from string to int
    min_range = int(input('Pick the number for the starting range: '))
    max_range = int(input('Pick the number for the ending range: '))

    # loop through the range the user inputted
    # start = min_range
    # stop = max_range+1 to include the max input, otherwise it would be one off
    for i in range(min_range, max_range+1):
        print(i)
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')