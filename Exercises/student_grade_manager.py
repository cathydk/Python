'''2. Student Grade Manager (Dictionary) ⭐

Concepts: dictionaries, conditionals, loops

Build a program that:

Lets you add students with grades
Lets you:
View all students
Get the average grade
Find the highest grade

👉 Example structure:

{"Alice": 90, "Bob": 85}

👉 Challenge:

Allow updating a student’s grade
Handle duplicate names'''

if __name__ == '__main__':

    # dictionary to hold student name and grade
    # key = name
    # value = grade
    gradebook = {}

    # let user know what the program does
    print('Student Grade Manager')
    print('---------------------')
    print('1. Add student & grade')
    print('2. View all students')
    print('3. Get average grade')
    print('4. Find the highest grade')
    print('5. Quit')

    # keep running program until the user wants to quit
    while True:
        # get user input on what they would like to do
        # user_input is a string
        # this has to be in the loop or the option the user chooses will be in an infinite loop***************************************************
        user_input = input('Please choose an option (EX. 1, 2, or 3...): ')

        # user input is 1
        if user_input == '1':
            # get student's name
            name = input('Please enter in the student\'s first name: ')
            # get student's grade
            # convert string to int***************************************************************
            grade = int(input('Please enter in the student\'s grade: '))
            # check if student's name is already in the dictionary 
            if name in gradebook:
                # if name is already in dictionary then user will be asked if they want to update the student's grade
                input_two = input('This student is already in the gradebook, would you like to update this student\s grade? (yes or no): ')
                # user wants to update student's grade
                if input_two == 'yes':
                    # use grade_update as value
                    # convert string to int***************************************************************
                    grade_update = int(input('What is the updated grade: '))
                    # add to dictionary; name = key, grade_update = value
                    gradebook[name] = grade_update
                # user doesn't want to update student's grade
                if input_two == 'no':
                    print(gradebook)
            # name isn't in dictionary
            else:
                # add name(key) and grade(value) to dictionary
                gradebook[name] = grade
        # user input is 2
        elif user_input == '2':
            # display dictionary
            print(gradebook)
        # user input is 3
        elif user_input == '3':
            # to hold value of all the grades added together***************************************************************
            # has to have a start, otherwise incorrect results and errors***************************************************************
            # don't use sum as a variable name, it overrides sum() function***************************************************************
            # total needs to be defined before calculation can commence***************************************************************
            total = 0
            # loop through dictionary***************************************************************
            for key, value in gradebook.items():
                # add all the values in the dictionary
                total = value + total
            # how many items are in the dictionary
            amount = len(gradebook)
            # handle 0 division***************************************************************
            if amount > 0:
                # calculate the average of the grades (value)
                average = total/amount
                # display average
                print('The average is {}'.format(average))
            else:
                print('There aren\'t any students in the gradebook')
        # user input is 4
        elif user_input == '4':
            # to hold highest grade
            highest = 0
            # loop through dictionary***************************************************************
            for key, value in gradebook.items():
                # compare the grades (value)
                if value > highest:
                    # if the current grade is higher set to highest
                    highest = value
            # display highest grade
            print('The highest grade is {}'.format(highest))
        # user input is 5
        elif user_input == '5':
            break
        # user input is invalid
        else:
            print('Input invalid')
            break