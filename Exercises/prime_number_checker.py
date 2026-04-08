'''3. Prime Number Checker

Concepts: loops, conditionals

Ask the user for a number
Check if it’s prime

👉 Hint:
Only check up to sqrt(n) (good habit for interviews)

👉 Challenge:
Print all prime numbers up to n'''

# A prime number is a whole number greater than 1 that has exactly two factors: 1 and itself

if __name__ == '__main__':

    # check if prime number
    # assume True at first
    is_prime = True

    # let user know what the program does and get user input
    # convert string to int
    user_input = int(input('Please enter in a number, I will check if it is a prime number: '))

    # edge case**************************************
    if user_input == 1:
        is_prime = False
    # check if user input is a prime number
    # user_input**0.5 = √user_input (square root)
    # pairs just repeat in reverse, so only need to check up to square root of user_input**************************************
    # EX. factors come in pairs: 36 = 1×36, 2×18, 3×12, 4×9, 6×6
    #     after sqrt(n), pairs repeat in reverse (9×4, 12×3, ...), so only check up to sqrt(n)
    # +1 to include boundary**************************************
    for i in range(2, int(user_input**0.5) + 1):
        # user_input is divisible by something other than 1 since it doesn't have a remainder
        if user_input%i == 0:
            # so not prime
            is_prime = False
            break
        else:
            # has a remainder so not divisible
            is_prime = True

    # display if user input is prime or not
    if is_prime == False:
        print('{} is not a prime number'.format(user_input))
    if is_prime == True:
        print('{} is a prime number'.format(user_input))