'''5. Simple Contact Book

Concepts: dictionaries, loops

Create a program where users can:

Add a contact (name + phone number)
View all contacts
Search for a contact

👉 Challenge:

Prevent duplicate names
Allow updating an existing contact'''

if __name__ == '__main__':

    # create dictionary called contacts to hold contact information
    # name = key
    # phone number = value
    contacts = {}
    
    # let user know what program does and what options they can choose from
    print('Contact Book')
    print('----------------------------------------')
    print('1. Add a contact (name and phone number)')
    print('2. View all contacts')
    print('3. Search for a contact')
    print('4. Quit')

    # loop until user decides to quit
    while True:
        # get user input
        # user_input is a string***
        user_input = input('Please select an option (EX. 1, 2, 3, or 4): ')

        # adding a contact into dictionary
        if user_input == '1':
            # name is key
            name = input('Enter in the name: ')
            # number is value
            number = input('Enter in the phone number: ')
            # check to see if name (key) is already in the contacts dictionary
            if name in contacts:
                print('This contact already exist')
                update = input('Would you like to update this contact information (yes or no): ')
                if update == 'yes':
                    new_number = input('What is the new number: ')
                    # update new number
                    # insert a new value (new_number)
                    contacts[name] = new_number
                elif update == 'no':
                    # printing out dictionary
                    print(contacts)
            # name isn't already in contacts
            else:
                # insert new value (number)
                # dictionary[key] = value
                contacts[name] = number
        # viewing all contacts
        elif user_input == '2':
            print(contacts)
        # search for a specific contact
        elif user_input == '3':
            # search is used as a key to lookup value (phone number)
            search = input('Who would you like to search for: ')
            # using in to verify whether a key (search) is in the dictionary (contacts)
            if search in contacts:
                # search is key
                # contacts[search] will look up the value (phone number)
                print('The phone number for {} is {}'.format(search, contacts[search]))
            else:
                print('That contact does not exist')
        # end program
        elif user_input == '4':
            # exits loop and terminates program 
            break