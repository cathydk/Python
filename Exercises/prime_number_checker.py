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

    # print all prime numbers up to user_input
    for num in range(2, user_input + 1):
        # -------------------------------
        # Step 1: Loop through all numbers from 2 up to the user input
        # 2 is the first prime number, so we start here
        # range() goes up to user_input + 1 because the upper bound is exclusive
        # -------------------------------

        # Step 2: Assume the current number is prime
        is_prime = True
        # We start with True and will try to prove it False if we find a divisor

        # -------------------------------
        # Step 3: Check for divisors using sqrt optimization
        # We only need to check divisors from 2 up to sqrt(num)
        # Why? Because factors come in pairs, e.g. for 36: 
        # 1×36, 2×18, 3×12, 4×9, 6×6
        # After sqrt(36)=6, factor pairs just repeat in reverse (9×4, 12×3, ...)
        # So no need to check beyond sqrt(num) → more efficient
        # -------------------------------
        for i in range(2, int(num**0.5) + 1):
            # Step 3a: Check if num is divisible by i
            if num % i == 0:
                # If divisible, num has a factor other than 1 and itself
                # Therefore, it's not prime
                is_prime = False
                # No need to check further, we can stop the inner loop
                break

        # -------------------------------
        # Step 4: If no divisors were found, num is prime
        # -------------------------------
        if is_prime:
            # Print the prime number
            # end=" " keeps all primes on the same line separated by spaces
            print(num, end=" ")