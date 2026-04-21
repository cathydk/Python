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
    beep = True

def main():
    user_sentence = input