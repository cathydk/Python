if __name__ == '__main__': # main function
    ######################################################VARIABLES####################################################
    # defining int variables
    x = 2
    y = 3
    z = 1
    a = 4
    b = 26
    c = 81
    d = 0
    e = 0
    f = 0
    
    # defining float variables
    x_float = 2.0
    
    # defining boolean variables
    is_up = True
    is_red = False
    
    ###############################################ARITHMETIC OPERATORS################################################
    # +,-,*,/,%,**,//
    x += 2 # x = x + 2
    print(x)
    
    y -= 2 # y = y - 2
    print(y)
    
    z *=2 # z = z * 2
    print(z)
    
    x /= 2
    print(x) # x = x / 2
    
    d = c % a # modulo(remainder)
    print(d)
    
    f = 2**3 # exponent
    print(f)
    
    e = c // a # integer division, rounds down to nearest integer
    print(e)
    
    #####################################################DATA TYPE&CONVERSION########################################
    print(type(4)) # returns the type of an object
    print(type(4.0))
    
    print(int(49.7)) # converting float to int
    print(float(49)) # converting int to float
    
    ##########################################COMPARISON OPERATORS&LOGICAL OPERATORS#################################
    # comparison operators: <,>,<=,>=,==,!=
    # logical operators: and, or, not
    # and: evaluates if both sides are true
    # or: evaluates if at least 1 side is true
    # not: inverses a boolean type
    age = 14
    is_teen = age > 12 and age < 20
    print(is_teen)
    not_teen = not(age > 12 and age < 20)
    print(not_teen)
    
    #######################################################STRING######################################################
    welcome_message = 'Hello, welcome in!'
    ask_name = ' What is your name?'
    cathy = 'cathy '
    
    print(welcome_message)
    print('glad to have you here')
    
    # +, combine strings
    print(welcome_message + ask_name)
    
    # *, repeat strings
    print('hi' * 5)
    print(cathy * 10)
    
    print(len(welcome_message)) # returns the length of an object
    
    print(str(100)) # int to string
    # string to float
    grams = '35.0'
    grams = float(grams)
    print(grams)
    
    # STRING METHODS
    # .title() capitalizes 1st letter of each word
    print('cathy khong'.title())
    
    # .islower() checks if lowercase
    print(cathy.islower())
    print('Cathy'.islower())
    
    # .count() count the occurences of string
    print('dog, cat, dog, chicken, dog, dog, fish'.count('dog'))
    
    # .split() returns a data container called a list that contains the words from the input string
    new_str = 'The cow jumped over the moon.'
    new_str_split = new_str.split()
    print(new_str)
    print(new_str_split)
    
    
    
    