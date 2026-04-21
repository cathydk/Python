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

def to_title_case(sentence):
    formatted_sentence = ''
    no_capitalize = ['and', 'the', 'of', 'in']
    sentence_list = sentence.split()

    for word in sentence_list:
        if word not in no_capitalize:
            formatted_sentence += word[0].upper()
            formatted_sentence += word[1:].lower()
            formatted_sentence += ' '
        else:
            formatted_sentence += word

    return formatted_sentence

def main():
    user_sentence = input('Enter in a sentence: ')
    formatted_title = to_title_case(user_sentence)
    print(formatted_title)

if __name__ == '__main__':
    main()