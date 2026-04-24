'''9. Compress a String (Run-Length Encoding)

Concepts: functions, strings, loops

👉 Create a function:
def compress_string(text):

👉 What it should do
Take a string
Replace repeated characters with:
the character + count

👉 Example
Input: "aaabbc"
Output: "a3b2c1"
Input: "abcd"
Output: "a1b1c1d1"

🔹 Hints
Loop through the string one character at a time
Keep track of:
current character
count of repeats

👉 Think:
count = 1
Compare current character with the next one

🔹 Key idea
When the character changes:
Add previous character + count to result
Reset count

🔹 Edge Case
Don’t forget the last character group

👉 Common mistake:
Loop ends but last group isn’t added

🔹 Challenge
Return the original string if compressed version is not shorter
"abcd" → "abcd" (instead of "a1b1c1d1")

🔥 Bonus Challenge
Handle numbers in the string:
Input: "aa111bb"
Output: "a213b2"'''

# define function to compress string
# text is a string
def compress_string(text):
    # create dictionary to hold character and its count
    # character = key
    # count = value
    character_count = {}
    # create string to hold compressed string
    compressed_string = ''

    # loop through user text string
    for char in text:
        # if current character is in the dictionary
        if char in character_count:
            # then increment the value by 1
            character_count[char] += 1
        # if current character is not in the dictionary
        else:
            # then add character to dictionary with a value of 1
            character_count[char] = 1
    '''EX. text -> abcd
           character_count -> {'a': 1, 'b': 1, 'c': 1, 'd': 1}'''

    # loop through dictionary
    for key,value in character_count.items():
        # key is string
        # concatenate the character to compressed_string
        compressed_string += key
        # value is int
        # convert int to str to concatenate to string********************************
        # concatenate the count to compressed_string
        compressed_string += str(value)

    # if the length of the original string is less than the length of the compressed version
    if len(text) < len(compressed_string):
        # return original string
        return text
    # if the length of the original string is not less than the length of the compressed version
    else:
        # return the compressed string
        return compressed_string

# define function to get user input, call function, and display output
def main():
    # get user string input
    user_string = input('Enter in a string: ')
    # call compress_string(text) function
    # user_string is a string being passed in
    # counted_string contains the compressed string
    counted_string = compress_string(user_string)
    # display compressed string
    print(counted_string)

# to call main() function
if __name__ == '__main__':
    main()

'''
def compress_string(text):
    character_count = {}
    compressed_string = ''

    for char in text:
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1

    for key,value in character_count.items():
        compressed_string += key
        compressed_string += str(value)

    if len(text) < len(compressed_string):
        return text
    else:
        return compressed_string

def main():
    user_string = input('Enter in a string: ')
    counted_string = compress_string(user_string)
    print(counted_string)

if __name__ == '__main__':
    main()
    '''