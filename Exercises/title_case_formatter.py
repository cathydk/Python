'''
## **6. Title Case Formatter**

**Concepts:** functions, strings, loops

👉 Create a function:
```python
def to_title_case(sentence):
```
---

## 👉 What it should do
* Take a sentence as input
* Return the sentence where:
  * The **first letter of each word is capitalized**
  * The rest of the letters are lowercase

---

## 👉 Example
```text
Input: "hello world from python"
Output: "Hello World From Python"
```
---

## 🔹 Hints
* Use:
```python
sentence.split()
```
to get all the words
* Loop through each word
* For each word:
  * Capitalize first letter
  * Lowercase the rest

👉 Think:
```python
word[0].upper() + word[1:].lower()
```
---

## 🔹 Challenge
* Handle empty strings (`""`)
* Handle extra spaces:
```text
"   hello   world   "
```
---

## 🔥 Bonus Challenge (more realistic)
Don’t capitalize small words like:
```
"and", "the", "of", "in"
```

👉 Example:
```text
Input: "the lord of the rings"
Output: "The Lord of the Rings"
```
'''

# define function to format string title
# sentence is a string
def to_title_case(sentence):
    # to hold formatted title
    formatted_sentence = ''
    # list to hold words that don't need to be capitalized if it's in the middle of the title
    no_capitalize = ['and', 'the', 'of', 'in']
    # use .split() to turn sentence (string) into a list
    sentence_list = sentence.split()

    # first word will always be capitalized, even if it is 'and', 'the', 'of', or 'in'
    # sentence_list[0:1] handles only the first word in the list*********************************
    for w in sentence_list[0:1]:
        # capitalize the first letter in the word
        formatted_sentence += w[0].upper()
        # make the trailing characters lowercase
        formatted_sentence += w[1:].lower()
        # adds a space in between word
        formatted_sentence += ' '

    # loop through sentence, starting at the second element in the list
    for word in sentence_list[1:]:
        # checks if current word is in no_capitalize list or not
        if word not in no_capitalize:
            # if current word is not in no_capitalize list
            # then capitalize the first letter of the word
            # make the trailing characters lowerecase
            # store it in formatted_sentence
            formatted_sentence += word[0].upper()
            formatted_sentence += word[1:].lower()
            # adds a space in between each word
            formatted_sentence += ' '
        else:
            # if current word is in no_capitalize list
            # then don't capitalize the first letter of the word
            # store it in formatted_sentence
            formatted_sentence += word
            # adds a space in between each word
            formatted_sentence += ' '

    # return formatted title (string)
    return formatted_sentence


# define function to get user input, call function, and display output
def main():
    user_sentence = input('Enter in a sentence: ')
    # user_sentence (string) is being passed in
    # formatted_title (string) holds the return value of to_title_case(sentence) function
    formatted_title = to_title_case(user_sentence)
    print(formatted_title)

# calls main() function
if __name__ == '__main__':
    main()


'''
def to_title_case(sentence):
    formatted_sentence = ''
    no_capitalize = ['and', 'the', 'of', 'in']
    sentence_list = sentence.split()

    for w in sentence_list[0:1]:
        formatted_sentence += w[0].upper()
        formatted_sentence += w[1:].lower()
        formatted_sentence += ' '

    for word in sentence_list[1:]:
        if word not in no_capitalize:
            formatted_sentence += word[0].upper()
            formatted_sentence += word[1:].lower()
            formatted_sentence += ' '
        else:
            formatted_sentence += word
            formatted_sentence += ' '

    return formatted_sentence

def main():
    user_sentence = input('Enter in a sentence: ')
    formatted_title = to_title_case(user_sentence)
    print(formatted_title)

if __name__ == '__main__':
    main()
    '''