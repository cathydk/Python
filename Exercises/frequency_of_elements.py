'''3. Count Frequency of Elements

Concepts: dictionaries, loops, functions

👉 Create a function:
def count_frequency(items):

👉 What it should do:
Take a list
Return a dictionary counting occurrences

👉 Example:
Input: [1, 2, 2, 3, 1, 1]
Output: {1: 3, 2: 2, 3: 1}

🔹 Hints:
Use a dictionary

Check:
if item in dict:
Otherwise initialize it

🔹 Challenge:
Return the most frequent element
Sort by frequency (highest → lowest)'''

# to sort dictionary by frequency (value)**************************************
import operator

# define function to count the frequency of an element
# items is a list
def count_frequency(items):
    # dictionary to hold elements and its frequency
    # elements are the key, and frequency is the value
    element_frequency = {}

    # loop through list of elements
    for item in items:
        # check if current item in list is in the dictionary element_frequency
        if item not in element_frequency:
            # if current item not in dictionary
            # then add it to the dictionary with a value of 1
            element_frequency[item] = 1
        else:
            # if current item is in dictionary
            # then increment the value of that element by 1
            element_frequency[item] += 1

    # return the dictionary
    return element_frequency


# define function to find the most frequent element in list
def most_frequent(elements):
    # call count_frequency(items) function
    # pass in elements list
    # element_count stores dictionary with the frequency of each element
    element_count = count_frequency(elements)

    # sort dictionary from highest to lowest by frequency (value)**************************************
    # sorted_dict output -> {2: 8, 3: 5, 1: 3}
    sorted_dict = dict(sorted(element_count.items(), key=operator.itemgetter(1), reverse=True))

    # return first key from sorted_dict, which is the most frequent element**************************************
    return next(iter(sorted_dict))

# define function to call functions and display output
def main():
    elements = [1, 2, 2, 3, 1, 1, 3, 3 ,3 ,3, 2, 2, 2, 2, 2, 2]

    # frequency is a dictionary
    frequency = count_frequency(elements)
    print(frequency)

    # frequent is an integer (first key from sorted dictionary)
    frequent = most_frequent(elements)
    print('{} is the most frequent element'.format(frequent))

# call main() function
if __name__ == '__main__':
    main()

'''
import operator

def count_frequency(items):
    element_frequency = {}

    for item in items:
        if item not in element_frequency:
            element_frequency[item] = 1
        else:
            element_frequency[item] += 1

    return element_frequency

def most_frequent(elements):
    element_count = count_frequency(elements)
    # sorted_dict output -> {2: 8, 3: 5, 1: 3}
    sorted_dict = dict(sorted(element_count.items(), key=operator.itemgetter(1), reverse=True))
    return next(iter(sorted_dict))

def main():
    elements = [1, 2, 2, 3, 1, 1, 3, 3 ,3 ,3, 2, 2, 2, 2, 2, 2]

    frequency = count_frequency(elements)
    print(frequency)

    frequent = most_frequent(elements)
    print('{} is the most frequent element'.format(frequent))

if __name__ == '__main__':
    main()
    '''