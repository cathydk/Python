'''Personal Expense Tracker (CLI App)

🧩 Core Features (MVP)
👉 Your app should:
Add an expense
    Category (food, gas, etc.)
    Amount
View all expenses
    Show categories + amounts
Show total spending
    Overall total
    Total per category
Save data (optional but strong)
    Save to a file (.txt or .json)
    Load data when program starts

🧠 Suggested Functions
Structure your program like this:
def save_data(tracker):
def load_data():

💡 Example Flow
Expense Tracker
---------------
1. Add Expense
2. View Expenses
3. Show Total
4. Exit

Choose an option: 1
Enter category: food
Enter amount: 15

Choose an option: 3
Total spending: $15
🧱 Data Structure
tracker = {
    "food": [10, 20],
    "gas": [40]
}

🚀 Make it stand out (pick 1–2)
⭐ Level Up Features
Prevent duplicate categories automatically
Show highest spending category
Add date tracking
Pretty output formatting
Error handling (invalid input)
'''

'''----------------------------------------------------------------------------------------------------------------------------------------------------------------'''
# define function that adds category and amount to dictionary
# tracker is a dictionary
def add_expense(tracker):
    # get category from user (string)
    category = input('Enter category: ')
    # get amount from user
    # convert string to int
    amount = int(input('Enter amount: '))

    # if category is not in the dictionary 
    if category not in tracker:
        # then add category and amount to dictionary
        # values is list because [amount]
        tracker[category] = [amount]
    # if category is in the dictionary
    else:
        # append amount to values which is a list
        tracker[category].append(amount)

'''----------------------------------------------------------------------------------------------------------------------------------------------------------------'''
# define function to display expenses (dictionary)
def view_expenses(tracker):
    print(tracker)

'''----------------------------------------------------------------------------------------------------------------------------------------------------------------'''
# define function to calculate total spending and total category spending
def total_spending(tracker):
    # to hold total spending
    total = 0
    # to hold total category spending
    total_per_category = 0

    # loop through dictionary
    for category in tracker:
        # sum(tracker[category]) adds all the number in the list for one category
        # total += sum(tracker[category]) adds all the categories together
        total += sum(tracker[category])

    # loop through dictionary
    for category in tracker:
        # sum(tracker[category]) adds all the number in the list for one category
        total_per_category = sum(tracker[category])
        # display total for current category
        print('Total for {} category: {}'.format(category, total_per_category))

    # display total
    print('Total: {}'.format(total))

'''----------------------------------------------------------------------------------------------------------------------------------------------------------------'''
def category_total(tracker, category):
    # to hold total category spending
    total_per_category = 0

    # sum(tracker[category]) adds all the number in the list for one category
    total_per_category = sum(tracker[category])
    # display total for current category
    print('Total for {} category: {}'.format(category, total_per_category))

'''----------------------------------------------------------------------------------------------------------------------------------------------------------------'''
def main():
    # create dictionary to hold category and amount
    # category (string) = key
    # amount (list of ints) = value
    tracker = {}

    while True:
        # display what program is and what options the user can choose from
        print('Personal Expense Tracker')
        print('========================')
        print('1. Add Expense')
        print('2. View Expenses')
        print('3. Total Spending')
        print('4. Category Spending')
        print('5. Exit')

        # get user input
        choice = input('Choose a number: ')

        # if user inputted 1
        if choice == '1':
            # calling add_expense(tracker) function
            # dictionary is being passed in
            add_expense(tracker)
        # if user inputted 2
        elif choice == '2':
            # calling view_expenses(tracker) function
            # dictionary is being passed in
            view_expenses(tracker)
        # if user inputted 3
        elif choice == '3':
            # calling total_spending(tracker)
            # dictionary is being passed in
            total_spending(tracker)
        # if user inputted 4
        elif choice == '4':
            # get category that user wants to see spending of
            category = input('Enter category: ')
            # calling category_total(tracker, category) function
            # dictionary (tracker) and string (category) being passed in
            category_total(tracker, category)
        # if user inputted 5
        elif choice == '5':
            # exit loop, program ends
            break

'''----------------------------------------------------------------------------------------------------------------------------------------------------------------'''
if __name__ == '__main__':
    # calling main() function
    main()