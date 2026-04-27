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
def add_expense(tracker):
def view_expenses(tracker):
def total_spending(tracker):
def category_total(tracker, category):
def save_data(tracker):
def load_data():
def main():

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

💻 Example of clean structure
def main():
    tracker = {}

    while True:
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Spending")
        print("4. Exit")

        choice = input("Choose: ")

        if choice == "1":
            add_expense(tracker)
        elif choice == "2":
            view_expenses(tracker)
        elif choice == "3":
            total_spending(tracker)
        elif choice == "4":
            break

if __name__ == '__main__':
    main()
'''