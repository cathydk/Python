if __name__ == '__main__':
    # Control Flow: the sequence in which your code is run
    
    ###############################################CONDITIONAL STATEMENTS################################################
    
    # if
    # statement is a conditional statement that runs or skips code based on whether
    # a condition is True or False
    phone_balance = 4
    bank_balance = 100
    print('phone balance: ' + str(phone_balance))
    print('bank balance: ' + str(bank_balance))
    if phone_balance < 5:
        phone_balance += 10
        bank_balance -= 10
    print('phone balance: ' + str(phone_balance))
    print('bank balance: ' + str(bank_balance))
    
    # if, elif, else
    # use identation to enclose blocks of code
    # >elif requires conditional statement
    # ^else doesn't require boolean expression
    season = 'fall'
    if season == 'spring':
        print('plant the garden')
    elif season == 'summer': # >requires conditional statement
        print('water')
    elif season == 'fall':
        print('harvest')
    elif season == 'winter':
        print('stay inside')
    else: # ^doesn't require conditional statement
        print('unrecognized season')
    
    ###########################################BOOLEAN EXPRESSIONS FOR CONDITIONS########################################
    
    # if statments sometimes use more complicated boolean expressions for their conditions
    
    # when we use a non-boolean object as a condition in an if statement in place of the boolean expression,
    # python will check for its truth value
    
    # the truth value of an object is considered True unless specified as False in documentation
    
    # Built-in objects that are considered False:
    # - constants defined to be false: None and False
    # - 0 of any numeric type: 0, 0.1, 0j, Decimal(0), Fraction(0.1)
    # - empty sequences and collections: '', (), [], {}, set(), range(0)
    
    # Example 1
    weight = 95
    height = 59
    if 18.5 <= weight/height**2 < 25:
        print('BMI Normal')
    else:
        print('BMI NOT Normal')
        
    # Example 2
    is_raining = True
    is_sunny = True
    if is_raining and is_sunny:
        print('rainbow')
        
    # Example 3
    subscribed = False
    location = 'USA'
    if (not subscribed) and (location == 'USA' or location == 'CAN'):
        print('send email')
        
    # Example 4
    # in this code, errors has the truth value True because it's a non-zero number,
    # so the error message is printed
    errors = 3
    if errors:
        print('{} errors to fix'.format(errors))
    else:
        print('No errors to fix.')
        
    #####################################################FOR LOOPS#######################################################
    
    # iterable: an object that can return 1 of its element at a time
    
    # Example 1
    cities = ['new york city', 'mountain view', 'chicago', 'los angeles']
    for city in cities: # city is the iteration variable, cities is the iterable
        print(city.title())
        
    # Example 2
    capitalized_cities = []
    for city in cities:
        capitalized_cities.append(city.title()) # create new list
    print(capitalized_cities)
    
    # range(start, stop, step) used for modifying list, used to create immutable sequence of numbers
    # start and step are optional
    print(range(4)) # 4 is stop -> 0,1,2,3
    print(range(2,6)) # 2 is start, 6 is stop -> 2,3,4,5
    print(range(1, 10, 2,)) # 1 is start, 10 is stop, 2 is step -> 1,3,5,7,9
    
    # Example with range()
    for i in range(3):
        print('Hello')
    
    ##################################################WHILE LOOPS########################################################
    
    # for loops are "definite iteration", the loop's body is run a predefined number of times
    
    # while loops are "indefinite iteration", loop repeats an unknown number of times and ends when a condition is met
    card_deck = [4,11,8,5,13,2,8,10]
    hand = []
    print('before entering loop')
    print(card_deck)
    print(hand)
    while sum(hand) < 17:
        hand.append(card_deck.pop())
        print('inside loop')
        print(card_deck)
        print(hand)
    print('exited loop')
    
    ###################################################BREAK,CONTINUE####################################################
    
    # sometimes we need more control over when a loop should end, or skip an iteration
    # in these cases, we use the break and continue keywords, which can be used in
    # both for and while loops
    
    # break: terminates a loop
    # continue: skips 1 iteration of a loop
    
    weight = 0
    items = []
    manifest = [12,4,25,2,68,32,4,1,2,3,1,2,50,2,10,2]
    for cargo_weight in manifest:
        print('current weight: {}'.format(weight))
        if weight >= 100:
            print('breaking from loop')
            break # terminates loop
        elif weight + cargo_weight > 100:
            print('skipping {}'.format(cargo_weight))
            continue # skips 1 iteration of loop
        else:
            print('adding {}'.format(cargo_weight))
            items.append(cargo_weight)
            weight += cargo_weight
    
    #################################################ZIP&ENUMERATE#######################################################
    
    # zip: returns an iterator that combines multiple iterables into 1 sequence of tuples
    # each tuple contains the elements in that position from all iterables
    print(list(zip(['a','b','c'],[1,2,3])))
    
    # unzip list into tuples
    same_list = [('a', 1), ('b', 2), ('c', 3)]
    letters, nums = zip(*same_list) # * is what unzips the list into tuples
    print(letters, nums)
    
    # enumerate: built in function that returns an iterator of tuples containing indices and values of a list
    more_letters = ['a','b','c','d','e']
    # use enumerate when you want the index along with each element of an iterable in a loop
    for i, letter in enumerate(more_letters):
        print(i, letter)
        
    ##################################################LIST COMPREHENSIONS################################################
    # Example 1
    uppercase_cities = []
    more_cities = ['new york city', 'mountain view', 'chicago', 'los angeles']
    for city in more_cities:
        uppercase_cities.append(city.title())
    print(uppercase_cities)
    
    # || (showing that the block of code above does the same exact thing as the line of code below)
    
    # the block of code above is equivalent to line below
    uppercase_cities = [city.title() for city in more_cities]
    print(uppercase_cities)
    
    # Example 2
    squares = [x**2 for x in range(9) if x%2 == 0]
    print(squares)
    
    # Example 3
    more_squares = [x**2 if x%2 == 0 else x+3 for x in range(9)]
    print(more_squares)