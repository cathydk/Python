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
    # list (value) to hold how much user spent************************
    expense = []

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
            # get amount spent from user************************
            amount_spent = int(input('Enter in how much you spent: '))
            expense.append(amount_spent)
            # add the user input to the dictionary; category = key, expense = value************************
            tracker[category] = expense
        elif user_choice == '2':
            # calculate total spending
            print('Total spending: {}'.format(sum(expense)))
        elif user_choice == '3':
            # show spending by category
            print(tracker)
        '''elif user_choice == '4':
            # 
        elif user_choice == '5':
            # 
        elif user_choice == '6':
            # user wants to quit
            break'''