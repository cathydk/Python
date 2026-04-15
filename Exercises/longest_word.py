'''2. Find the Longest Word

Concepts: strings, loops, functions

👉 Create a function:
def longest_word(sentence):

👉 What it should do:
Take a sentence (string)
Return the longest word

👉 Example:
Input: "I love programming"
Output: "programming"

🔹 Hints:
Use .split() to turn sentence into a list
Keep track of the longest word as you loop

🔹 Challenge:
If tie → return the first longest word'''

# define function to find the longest word in user input
# sentence is a string
def longest_word(sentence):
    # turn user input from string to list with .split()
    sentence_list = sentence.split()
    # make the first word in the list the longest_word
    longest_word = sentence_list[0]

    # loop through list
    for word in sentence_list:
        # check if length of the current word is longer than the length of the current longest_word
        if len(longest_word) < len(word):
            # if the length of the current word is longer than the length of the current longest_word
            # then make longest_word the current word
            longest_word = word
    # return the longest_word
    return longest_word

# define function to call functions, get input, and display output
def main():
    # get user input
    user_input = input('Enter in a sentence: ')
    # call longest_word(sentence) function
    # pass in user_input to the function
    # store returned value in word
    word = longest_word(user_input)
    # display user input and the longest word from user input
    print('The longest word in your sentence: {} is {}'.format(user_input, word))

if __name__ == '__main__':
    # call main() function
    main()

'''
def longest_word(sentence):
    sentence_list = sentence.split()
    longest_word = sentence_list[0]

    for word in sentence_list:
        if len(longest_word) < len(word):
            longest_word = word
            
    return longest_word

def main():
    user_input = input('Enter in a sentence: ')
    word = longest_word(user_input)
    print('The longest word in your sentence: {} is {}'.format(user_input, word))

if __name__ == '__main__':
    main()
    '''