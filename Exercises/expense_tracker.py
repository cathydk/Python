'''5. Expense Tracker (Dictionary) ⭐

Concepts: dictionaries, lists

Build a program that:

Lets users enter expenses like:
Food: 20
Transport: 10
Stores them in a dictionary
Calculates:
Total spending
Spending by category

👉 Example:

{"Food": [20, 15], "Transport": [10]}

👉 Challenge:

Show which category has the highest spending
Allow deleting an expense'''

if __name__ == '__main__':

    # dictionary to hold category and how much spent
    tracker = {}

    # let user know what program does
    print('Expense Tracker')
    print('---------------')
    print('1. Add an expense')
    print('2. Calculate total spending')
    print('3. Show spending by category')
    print('4. Show which category has the highest spending')
    print('5. Delete an expense')
    print('6. Quit')

    # allow users to keep using tracker until they decide to quit
    while True:

        # get what user chooses in the option menu
        user_choice = input('Choose an option: ')

        if user_choice == '1':
            # add an expense
            category = input('Enter in a category: ')
            # get amount spent from user
            amount_spent = int(input('Enter in how much you spent: '))

            if category not in tracker:
                # category not in dictionary yet, so add it to dictionary*****************************
                tracker[category] = [amount_spent]
            else:
                # category in dictionary, so append amount_spent to key which is a list*****************************
                tracker[category].append(amount_spent)

        elif user_choice == '2':
            # calculate total spending
            total = 0

            # loop through each category in dictionary
            for category in tracker:
                # sum(tracker[category]) adds all the number in the list for one category
                # total = total + sum(tracker[category]) adds all the categories together*****************************
                total = total + sum(tracker[category])

            print('Total spending: {}'.format(total))

        elif user_choice == '3':
            # show spending by category
            print(tracker)

        elif user_choice == '4': # CONTINUE HERE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! similar logic for adding all categories together
            # show which category has the highest spending
            print(tracker)
        elif user_choice == '5':
            # delete an expense
            print(tracker)
            delete_expense = input('What value would you like to delete: ')
        elif user_choice == '6':
            # user wants to quit
            break