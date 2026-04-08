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
        # user_input is divisible by something other than 1 since it doesn't have a remainder^^^^^
        if user_input%i == 0:
            # so not prime
            is_prime = False
            # since already found a number that isn't prime, no need to continue
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
    # the upper bound of the outer loop is always n and the upper bound for the inner loop is n**0.5
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
        # when the inner for loop breaks i starts from the beginning again
        # When the inner loop breaks, It stops immediately for that num, Control goes back to the outer loop to pick the next num
        # Next iteration of the outer loop, A new inner loop starts for the new num, i always starts again from 2 for this new number**************************************
        # ✅ Important: i does not continue from the previous number. Every time the outer loop moves to a new num, the inner loop always starts fresh at 2
        for i in range(2, int(num**0.5) + 1):
            # Step 3a: Check if num is divisible by i
            # doing num % i because we want to find all the prime numbers up until the user_input**************************************
            # num goes all the way of to user_input, same concept as above, but with more numbers^^^^^
            if num % i == 0:
                # If divisible, num has a factor other than 1 and itself
                # Therefore, it's not prime
                is_prime = False
                # No need to check further, we can stop the inner loop
                break
        '''Outer loop picks a num.
            Inner loop starts with i = 2.
            If num is divisible by i, break → inner loop ends immediately → move to next num.
            If num is not divisible, i increments until i > sqrt(num) → then inner loop ends → number is prime → print.
            For each new num, the inner loop always starts at i = 2 again'''
        
        """
            Prime Number Checker – Detailed Flow (prints primes up to user_input)

            Outer Loop (num = 2 → user_input)
                |
                v
            Set num
                |
                v
            Inner Loop (i = 2 → int(sqrt(num)))
                    |
                    v
            Check: num % i == 0 ?
                    / \
                /   \
                Yes     No
                /        \
            is_prime=False  i increments by 1
            Break → inner loop ends
                    |
                    v
            After inner loop ends:
            if is_prime == True:
                Print num (prime)
            else:
                Do not print
                    |
                    v
            Back to Outer Loop → next num
            (i always starts at 2 for new num)**************************************
        """

        # -------------------------------
        # Step 4: If no divisors were found, num is prime
        # -------------------------------
        # only after the inner loop finishes, the program moves to this if statement
        # this check happens once per number num
        if is_prime:
            # Print the prime number
            # end=" " keeps all primes on the same line separated by spaces
            print(num, end=" ")
        
        # after checking and printing if prime the current num, the outer loop increments num and repeats the process.
        # inner loop starts again for the new num

'''
Prime Number Checker Timeline (user_input = 10)

Outer Loop num | int(√num) | Inner Loop i Values   | Condition (num % i == 0)                 | is_prime | Action
---------------|------------|----------------------|------------------------------------------|----------|-------
2              | 1          | — (range(2,2) empty) | —                                        | True     | Print 2 ✔
3              | 1          | — (range(2,2) empty) | —                                        | True     | Print 3 ✔
4              | 2          | 2                    | 4 % 2 == 0 ✅                           | False    | Break → Do not print
5              | 2          | 2                    | 5 % 2 != 0 ❌                           | True     | Print 5 ✔
6              | 2          | 2                    | 6 % 2 == 0 ✅                           | False    | Break → Do not print
7              | 2          | 2                    | 7 % 2 != 0 ❌                           | True     | Print 7 ✔
8              | 2          | 2                    | 8 % 2 == 0 ✅                           | False    | Break → Do not print
9              | 3          | 2, 3                 | 2: 9 % 2 != 0 ❌ <br> 3: 9 % 3 == 0 ✅ | False     | Break → Do not print
10             | 3          | 2, 3                 | 2: 10 % 2 == 0 ✅                       | False    | Break → Do not print

Notes:
- int(√num) is the upper bound of the inner loop.
- Inner loop checks divisibility for i in range(2, int(√num)+1)
- Break stops the inner loop immediately when a divisor is found.
- If no divisors found, is_prime remains True → number is printed.
'''