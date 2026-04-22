'''
## **7. Word Counter (Top Word Finder)**

**Concepts:** functions, strings, dictionaries

👉 Create a function:
```python
def most_common_word(sentence):
```

---

## 👉 What it should do
* Take a sentence as input
* Return the **word that appears the most times**

---

## 👉 Example
```text
Input: "apple banana apple orange banana apple"
Output: "apple"
```

---

## 🔹 Hints
* Convert sentence into a list:
```python
words = sentence.split()
```
* Use a dictionary to count:
```python
word_count = {}
```

* Pattern:
```python
if word in word_count:
    word_count[word] += 1
else:
    word_count[word] = 1
```
* Track the word with the highest count

---

## 🔹 Challenge
* Ignore capitalization:
```text
"Apple apple APPLE" → "apple"
```
👉 Hint:
```python
sentence.lower()
```

---

## 🔹 Bonus Challenge
* Ignore punctuation:
```text
"apple, apple! banana." → "apple"
```

* If there’s a tie → return any OR return both
'''

# to remove punctuation from user string**************************************
import string
# to sort dictionary by frequency (value)**************************************
import operator

# define function to find most common word in user sentence
# sentence is a string
def most_common_word(sentence):
    # create dictionary to hold the words in sentence and the frequency that those words occur in sentence
    word_count = {}
    # create string to hold formatted sentence
    lowercase_no_punctuation = ''

    # make all the characters in sentence (string) lowercase
    sentence_lower = sentence.lower()

    # loop through lower case sentence string and remove punctuation
    for char in sentence_lower:
        # if current characer isn't '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~' **************************************
        # string.punctuation is a built-in constant from Python’s string module, it contains all common punctuation characters as a single string
        # string.punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
        if char not in string.punctuation:
            # then store character in lowercase_no_punctuation
            lowercase_no_punctuation += char

    # turn formatted string into list
    sentence_list = lowercase_no_punctuation.split()

    # loop through list
    for word in sentence_list:
        # if current word is in dictionary
        if word in word_count:
            # then add 1 to the value
            word_count[word] += 1
        # if current word is not in dictionary
        else:
            # then add that word to the dictionary with a value of 1
            word_count[word] = 1

    # sort dictionary from highest to lowest by frequency (value)**************************************
    sorted_dict = dict(sorted(word_count.items(), key=operator.itemgetter(1), reverse=True))

    # return first key from sorted_dict, which is the most frequent element**************************************
    return next(iter(sorted_dict))

# define function to get user input, call function, and display output
def main():
    user_sentence = input('Enter in a sentence: ')
    # calling most_common_word(sentence) function
    # user_sentence (string) is being passed in
    # common_word contains the first key from the dictionary, which is the most common word
    common_word = most_common_word(user_sentence)
    print('{} is the most common word'.format(common_word))

# to call main() function
if __name__ == '__main__':
    main()

'''
import string
import operator

def most_common_word(sentence):
    word_count = {}
    lowercase_no_punctuation = ''

    sentence_lower = sentence.lower()

    for char in sentence_lower:
        if char not in string.punctuation:
            lowercase_no_punctuation += char

    sentence_list = lowercase_no_punctuation.split()

    for word in sentence_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    sorted_dict = dict(sorted(word_count.items(), key=operator.itemgetter(1), reverse=True))

    return next(iter(sorted_dict))

def main():
    user_sentence = input('Enter in a sentence: ')
    common_word = most_common_word(user_sentence)
    print('{} is the most common word'.format(common_word))

if __name__ == '__main__':
    main()
    '''