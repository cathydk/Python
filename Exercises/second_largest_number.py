'''4. Find Second Largest Number

Concepts: lists, functions, problem-solving

👉 Create a function:
def second_largest(numbers):

👉 What it should do:
Return the second largest unique number

👉 Example:
Input: [10, 5, 8, 20]
Output: 10

🔹 Hints:
Option 1: Use set() to remove duplicates
Option 2: Track largest and second_largest manually

🔹 Edge Case:
Input: [10, 10, 8]
Output: 8

🔹 Challenge:
Handle list with fewer than 2 unique numbers
Return None or a message'''

# define function to find the second largest number from a list
# numbers is a list
def second_largest(numbers):
    # use set() to remove duplicate numbers from the list
    unique_numbers = set(numbers)

    # handles list with fewer than 2 unique numbers
    if len(unique_numbers) < 2:
        # ther isn't a second largest number
        return None
    # list has 2 or more unique numbers
    else:
        # output of sorted_list -> [20, 10, 8, 5]
        # sort list from highest to lowest
        sorted_list = sorted(unique_numbers, reverse = True)
        # return the second largest number
        return sorted_list[1]

# define function to call function and display output
def main():
    numbers_list = [10, 5, 8, 20]
    # call second_largest(numbers) function
    # secong_largest_number stores the second largest number from the unique numbers_list
    second_largest_number = second_largest(numbers_list)
    # display output
    print('The second largest number is: {}'.format(second_largest_number))

# to call main() function
if __name__ == '__main__':
    main()


'''
def second_largest(numbers):
    unique_numbers = set(numbers)

    if len(unique_numbers) < 2:
        return None
    else:
        sorted_list = sorted(unique_numbers, reverse = True)
        return sorted_list[1]

def main():
    numbers_list = [10, 5, 8, 20]
    second_largest_number = second_largest(numbers_list)
    print('The second largest number is: {}'.format(second_largest_number))

if __name__ == '__main__':
    main()
    '''