if __name__ == '__main__':
    ###########################################################LIST######################################################
    # List: data type for mutable ordered sequences of elements, can contain any mix and match data types
    # Defined using square brackets []
    # index going foward: 0, 1, 2, 3
    # index going backward: -1, -2, -3, -4
    random_list = [1, 3.4, 'a string', True]
    print(random_list)
    
    # Slicing: using indices to slice off parts of an objects like a string or a list
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    # the index to the left of the colon is where the slice begins, the slice continues up to the 2nd index
    # lower boung is inclusive, upper bound is exclusive
    q3 = months[6:9]
    print(q3)
    
    ##################################################MEMBERSHIP OPERATORS###############################################
    # in: evaluates if object on LEFT SIDE is INCLUDED IN object on RIGHT SIDE
    # not in: evaluates if object on LEFT SIDE is NOT INCLUDED IN object on RIGHT SIDE
    greeting = 'Hello there'
    print('her' in greeting, 'her' not in greeting)
    
    #############################################USEFUL FUNCTIONS&METHODS FOR LISTS######################################
    num_list = [3, 13, 64, 1, 9, 387, 2, 76, 49, 4, 1, 1, 1, 1]
    alpha_list = ['a', 'd', 'z', 'r', 'd', 'c', 'a']
    
    # USEFUL FUNCTIONS
    # len() returns how many elements are in a list
    print(len(num_list))
    
    # max() returns the greatest element of the list
    # the max element in a list of numbers is the largest number
    # the max element in a list of strings is elemnet that would occur last if the list were sorted alphabetically
    print(max(num_list))
    print(max(alpha_list))
    
    # min() returns the smallest element in a list
    # min is the opposite of max()
    print(min(num_list))
    print(min(alpha_list))
    
    # sorted() returns a COPY of a list in order from smallest to largest, leaving the original list unchanged
    sorted_num_list = sorted(num_list)
    print(sorted_num_list)
    print(num_list)
    
    # USEFUL METHODS
    # .join() string method that takes a list of strings as an argument
    # returns a string consisting of the list elements joined
    new_alpha_list = '*'.join(alpha_list)
    print(new_alpha_list)
    
    # .append() method that adds an element to the end of a list
    alpha_list.append('y')
    print(alpha_list)
    
    #########################################################TUPLES######################################################
    # Tuples: data type for immutable ordered sequences of elements
    # can't add or remove items from tuples
    # access items with indices
    Angkorwat = (13.4125, 103.867)
    print(Angkorwat)
    print(Angkorwat[0])
    # Tuples can be used to assign multiple variables in a compact way
    # parentheses () are optional when defining tuples
    dimensions = 52, 40, 100
    print(dimensions)
    length, width, height = dimensions # 3 variables are assigned from the content of the tuple dimensions (tuple unpacking) 
    print(length)
    print(width)
    print(height)
    print(length, width, height)
    
    ###########################################################SETS######################################################
    # Set is a data type for mutable unordered collections of unique elements
    # unordered fo there isn't a last element
    # operations you can perform with sets include mathematical sets
    # methods like union, intersection, and difference are easy to perform with sets
    num_set = set(num_list)
    print(num_list)
    print(num_set)
    print(len(num_set))
    print(1 in num_list)
    print(1 in num_set)
    num_set.add(100)
    print(num_set)
    
    # .pop() method that RANDOM elemen removed
    num_set.pop()
    print(num_set)
    
    ###########################################DICTIONARIES&IDENTITY OPERATORS###########################################
    # Dictionary is a data type for mutable objects that store mappings of UNIQUE KEYS to VALUES
    # dictionary keys are similar to list indices, keys ~> indices
    # >select elements from dictionary by putting the key in square brackets []
    # key:value
    # >dictionary[key] -> look up values
    # dictionaries can have keys of any immutable type, not just integers
    # it's not necessary for every key to have the same type
    elements = {'hydrogen':1, 'helium':2, 'carbon':6}
    print(elements)
    print(elements['carbon']) # >we can look up VALUES in the dictionary by using square brackets[] enclosing a KEY
    elements['lithium'] = 3 # insert 3 as a new value, 'lithium' is the key
    print(elements)
    
    print('mithril' in elements) # check whether a VALUE is in dictionary, use in to verify whether a KEY is in the dictionary before looking it up
    print(elements.get('dilithium')) # >.get() looks up VALUES in dictionary
    
    # IDENTITY OPERATORS
    # is: evaluates if both sides have the same identity
    # is not: evaluates if both sides have different identities
    x = elements.get('dilithium') # checks if a KEY returns None with the is operator
    is_null = x is None
    print(is_null)
    non_null = x is not None
    print(non_null)
    
    ######################################################COMPOUND DATA STRUCTURES#######################################
    # Compound data structures: containers in other containers
    
    # this dictionary maps keys to values that are also dictionaries
    elements = {'hydrogen':{'number':1, 'weight':1.00794, 'symbol':'H'},
                'helium':{'number':2, 'weight':4.002602, 'symbol':'He'}}
    helium = elements['helium'] # look up helium dictionary
    print(helium)
    
    hydrogen_weight = elements['hydrogen']['weight'] # look up hydrogen's weight
    print(hydrogen_weight)
    
    oxygen = {'number':8, 'weight':15.999, 'symbol':'O'} # create new oxygen dictionary
    print(oxygen)
    elements['oxygen'] = oxygen # assign 'oxygen' as a key to the elements dictionary
    print(elements)