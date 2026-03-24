'''5. To-Do List Program

Concepts: lists, loops

Let users:
Add tasks
View tasks
Remove tasks

👉 Challenge: Keep the program running until the user chooses to quit'''

if __name__ == '__main__':
    
    # list for tasks
    tasks = []
    
    # let users know what the program does
    print('To-Do List Program')
    
    # variable to check if user wants to quit program variable
    is_quit = False
    # let user knows how to quit program
    print('When you are finished with the program and want to quit, enter: q')
    
    # while the user has not entered in q to quit
    while is_quit == False:
        # get user input on whether they want to add, view, or remove tasks
        user_input_one = input('Would you like to add, view, or remove tasks? (EX. input format: add) ')
        # user inputed add
        if user_input_one == 'add':
            # get user input on what they would like to add to to-do list
            add_input = input('What would you like to add: ')
            # add user input to list
            tasks.append(add_input)
        # user inputed view
        if user_input_one == 'view':
            # display to-do list
            print(tasks)
        # user inputed remove
        if user_input_one == 'remove':
            # get user input on what they would like to remove from to-do list
            remove_input = input('What would you like to remove: ')
            # remove the task the user inputed
            tasks.remove(remove_input)
        # user inputed q
        if user_input_one == 'q':
            # user inputed q so they want to quit program, set is_quit to True
            is_quit = True