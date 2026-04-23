'''8. Find Missing Number

Concepts: functions, lists, loops

👉 Create a function:
def find_missing_number(numbers):

👉 What it should do
You’re given a list of numbers from 1 to n, but one number is missing
Return the missing number

👉 Example
Input: [1, 2, 4, 5]
Output: 3
Input: [2, 3, 1, 5]
Output: 4

🔹 Hints
Think: what numbers should be there?
Loop from 1 → n and check:
if i not in numbers:

🔹 Better Hint (more efficient)
Use math:
👉 Sum of numbers from 1 to n:
n * (n + 1) / 2
Expected sum − actual sum = missing number

🔹 Challenge
Don’t use in (forces better logic)
Handle unsorted lists
Handle larger inputs efficiently'''

# define function to find missing number in a list
# numbers is a list of string numbers*******************************************
def find_missing_number(numbers):
    # to hold sum of expected value if a number wasn't missing from the list
    expected_sum = 0
    # to hold sum of the numbers in the list
    actual_sum = 0
    # to hold missing number after calculation is performed
    missing_number = 0
    # to hold the numbers in int instead of string
    int_numbers_list = []

    # loop through list of string numbers
    for num in numbers:
        # convert string number to int number
        # add int number to int_numbers_list
        int_numbers_list.append(int(num))

    # sort the int_numbers_list from smallest to largest
    sorted_list = sorted(int_numbers_list)
    # largest_number is the number at the end of the sorted list
    # need the largest_number to know when to stop the loop
    largest_number = sorted_list[-1]

    # loop from 0 to largest_number+1 to include largest_number
    # no numbers will be left out
    '''EX. sorted_list -> [1, 2, 4, 5]
           largest_number -> 5
           i goes from 0 to 5'''
    for i in range(largest_number+1):
        # add all the numbers from 0 to largest_number+1
        expected_sum += i
    
    # add all the numbers in the sorted_list (one number is missing)
    actual_sum = sum(sorted_list)

    # calculate the missing number
    missing_number = expected_sum - actual_sum

    # return missing_number (int)
    return missing_number

# define function to get user input, create list, call function, and display output
def main():
    # get numbers from user (string)
    user_numbers = input('Enter in numbers: ')
    # create a list from that string, so now it's a list of string numbers, EX. ['1', '2', '4', '5']
    user_numbers_list = user_numbers.split()
    # call find_missing_number(numbers) function
    # user_numbers_list is a list of string numbers
    # missing_number is an int
    missing_number = find_missing_number(user_numbers_list)
    # display missing number
    print('The missing number is {}'.format(missing_number))

# to call main() function
if __name__ == '__main__':
    main()

'''
def find_missing_number(numbers):
    expected_sum = 0
    actual_sum = 0
    missing_number = 0
    int_numbers_list = []

    for num in numbers:
        int_numbers_list.append(int(num))

    sorted_list = sorted(int_numbers_list)
    largest_number = sorted_list[-1]

    for i in range(largest_number+1):
        expected_sum += i
    
    actual_sum = sum(sorted_list)

    missing_number = expected_sum - actual_sum

    return missing_number


def main():
    user_numbers = input('Enter in numbers: ')
    user_numbers_list = user_numbers.split()
    missing_number = find_missing_number(user_numbers_list)
    print('The missing number is {}'.format(missing_number))

if __name__ == '__main__':
    main()
    '''