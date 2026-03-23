'''4. Word Counter

Concepts: strings, lists

Ask the user to input a sentence
Count how many words are in it

👉 Challenge: Also count how many times each word appears'''

# to count frequency of word in list
from collections import Counter

if __name__ == '__main__':
    
    # tells the user what the program does
    print('I will count how many words are in your sentence')
    
    # asks user to input a sentence
    user_input = input('Please input a sentence: ')
    
    # use split method to convert user string to a list with each word as an item
    words = user_input.split()
    
    # the length of the words list is the amount of words in the sentence
    count = len(words)
    
    # print word count
    print('There are {} words in your sentence'.format(count))
    
    # count frequency of words in sentence
    # pass words list as a parameter to Counter
    # Counter returns a dictionary-like object where keys are the words and values are their counts
    word_count = Counter(words)
    print(word_count)
    
    