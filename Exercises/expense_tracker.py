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

    # allow users to keep using tracker until they decide to quit
    while True:
        # handles when user wants to quit
        quit = input('Type in \'q\' when you want to quit the program: ')
        if quit == 'q':
            break
        # get category from user
        category = input('Enter in a category: ')
        # go through dictionary and only add categories that haven't been added
        for key, value in tracker.items():
            if key in tracker:
                add_amount = int(input('This category already exist, enter in how much you spent: '))
                tracker[category] = add_amount
        # get amount spent from user
        amount_spent = int(input('Enter in how much you spent: '))
        # add the user input to the dictionary; category = key, amount_spent = value
        tracker[category] = amount_spent
        print(tracker)