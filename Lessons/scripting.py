#########################################################SCRIPTING#######################################################

if __name__ == '__main__':
    
    ############################################SCRIPTING WITH RAW INPUT#################################################
    
    # The input function takes in what the user types and stores it as a string
    name = input('Enter your name: ') # get input from user
    print('Hello there, {}!'.format(name.title()))
    
    # If you want to interpret the input as something other than a string,
    # you need to wrap the result with the new type to convert it from a string
    num = int(input('Enter an integer: '))
    print('hello ' * num)
    
    # We can interpret user input as a python expression using eval function
    result = eval(input('Enter an expression (ex. 2*3): ')) # evaluates a string as a line of python
    print(result)
    
    #################################################HANDLING ERRORS#####################################################
    
    # try: this is the only mandatory clause in a try statement. The code in this block is the 1st
    # thing that python runs in a try statement
    
    # except: if python runs into an exception while running the try block, it will jump to the
    # except block that handles the exception
    
    # else: if python runs into no exceptions while running the try block, it will run the code in this block after
    # running the try block
    
    # finally: before python leaves the try statement, it will run the code in this finally block under any conditions,
    # even if it's ending the program E.G. if python ran into an error while running code in the except or else block,
    # this finally block will still be executed before stopping the program
    
    # We can specify which error we want to handle in an except block
    try:
        #code
        print('in try block 1')
    except ValueError: # catches ValueError
        print('ValueError detected')
        #code
        
    # If we want to address more than 1 type of exception, we can include a parenthesized tuple after the except
    # with exceptions
    try:
        print('in try block 2')
    except(ValueError, KeyboardInterrupt):
        print('ValueError or KeyboardInterrupt detected')
        
    # If we want to execute different blocks of code depending on the exception, you can have multiple except blocks
    try:
        print('in try block 3')
    except ValueError:
        print('ValueError detected')
    except KeyboardInterrupt:
        print('KeyboardInterrupt detected')
        
   ################################################ACCESSING ERROR MESSAGES##############################################
        
   # When you handle an exception, you can still access its error messages
    try:
        print('in try block 4')
    except ZeroDivisionError as e:
        print('ZeroDivisionError occured: {}'.format(e))
    
    ###############################################READING & WRITING FILES###############################################
        
    # READING A FILE
    f = open('my_path/my_file.txt', 'r')
    file_data = f.read()
    f.close
    
    #                                                How to read a file
    # =============================================================================================================
    # 1) 1st open the file using open(). This requires a string that shows the path to the file. The open function
    #    returns a file object, which is a python object through which python interacts with the file itself.
    #    Here we assign this object to the variable f
    # 2) There are optional parameters you can specify in the open function. 1 is the mode in which we open the
    #    file. Here, we use r or read only. This is the default value for the mode argument.
    # 3) Use the read method to access the contents from the file object. This read method takes the text contained
    #    in a file and puts it into a string. Here we assign the string returned from this method into the variable
    #    file_data
    # 4) When finished with the file, use the close method
    
    # WRITING TO A FILE
    f = open('my_path/my_file.txt', 'w')
    f.write('hello')
    f.close()
    
    #                                            How to write to a file
    # ===========================================================================================================
    # 1) Open the file in writing ('w') mode. If file doesn't exist, python will create it for you. If you open
    #    an existing file in writing mode, ANY CONTENT THAT IT HAD CONTAINED PREVIOUSLY WILL BE DELETED. If
    #    you're interested in ADDING to an existing file, WITHOUT DELETING its content, you should use the append
    #    ('a') mode
    # 2) Use the write method to add text to the file
    # 3) Close the file when finished
    
    # with keyword allows you to open a file, do operations on it and automatically close it after the indented code
    # is executed in this case, reading from the file. Now, we don't have to call f.close(). You can only access
    # the file object, f, within the indented block
    # with open('my_path/my_file.txt', 'r') as f: IS SAME AS f = open('my_path/my_file.txt', 'r')
    with open('my_path/my_file.txt', 'r') as f:
        file_data = f.read()
        
    ############################################IMPORTING LOCAL SCRIPTS##################################################
    
    # If the script you want to import is in the same directory as your current script, you just type import followed
    # by the name of the file, without the .py extension
    import useful_functions
    
    # To access an object in another file, we need to use the name of the file followed by a dot, followed by the object
    import other_script
    print(other_script.num) # num is a variable
    
    import math
    print(math.factorial(4)) # factorial is a function
    
    # Alias for function
    useful_functions as uf
    
    # To avoid running executable statements in a script when it's imported as a module in another script include
    # these lines in an if __name__ == '__main__': block
    
    ################################################IMPORTING MODULES####################################################
    
    # 1) import an individual function or class from a module
    from module_name import object_name
    
    # 2) import multiple individual objects
    from module_name import first_object, second_object
    
    # 3) rename a module
    import module_name as new_name
    
    # 4) import an object from a module and rename it
    from module_name import object_name as new_name